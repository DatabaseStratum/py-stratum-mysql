import os
import re
from configparser import ConfigParser
from typing import Any, Dict

from pystratum_backend.StratumIO import StratumIO
from pystratum_common.backend.CommonConstantWorker import CommonConstantWorker
from pystratum_common.helper.Util import Util

from pystratum_mysql.backend.MySqlWorker import MySqlWorker


class MySqlConstantWorker(MySqlWorker, CommonConstantWorker):
    """
    Class for creating constants based on column widths, and auto increment columns and labels for MySQL databases.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: StratumIO, config: ConfigParser):
        """
        Object constructor.

        :param io: The output decorator.
        """
        MySqlWorker.__init__(self, io, config)
        CommonConstantWorker.__init__(self, io, config)

        self._columns: Dict[str, Any] = {}
        """
        All columns in the MySQL schema.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_old_columns(self) -> None:
        """
        Reads from file constants_filename the previous table and column names, the width of the column,
        and the constant name (if assigned) and stores this data in old_columns.
        """
        if os.path.exists(self._constants_filename):
            with open(self._constants_filename, 'r') as file:
                line_number = 0
                for line in file:
                    line_number += 1
                    if line != "\n":
                        prog = re.compile(r'\s*(?:([a-zA-Z0-9_]+)\.)?([a-zA-Z0-9_]+)\.'
                                          r'([a-zA-Z0-9_]+)\s+(\d+)\s*(\*|[a-zA-Z0-9_]+)?\s*')
                        matches = prog.findall(line)

                        if matches:
                            matches = matches[0]
                            schema_name = str(matches[0])
                            table_name = str(matches[1])
                            column_name = str(matches[2])
                            length = str(matches[3])
                            constant_name = str(matches[4])

                            if schema_name:
                                table_name = schema_name + '.' + table_name

                            if constant_name:
                                column_info = {'table_name':    table_name,
                                               'column_name':   column_name,
                                               'length':        length,
                                               'constant_name': constant_name}
                            else:
                                column_info = {'table_name':  table_name,
                                               'column_name': column_name,
                                               'length':      length}

                            if table_name in self._old_columns:
                                if column_name in self._old_columns[table_name]:
                                    pass
                                else:
                                    self._old_columns[table_name][column_name] = column_info
                            else:
                                self._old_columns[table_name] = {column_name: column_info}

                        else:
                            raise RuntimeError("Illegal format at line {0} in file {1}".
                                               format(line_number, self._constants_filename))

    # ------------------------------------------------------------------------------------------------------------------
    def _get_columns(self) -> None:
        """
        Retrieves metadata about all table columns in the MySQL schema.
        """
        rows = self._dl.get_all_table_columns()
        for row in rows:
            # Enhance row with the actual length of the column.
            row['length'] = self.derive_field_length(row)

            if row['table_name'] in self._columns:
                if row['column_name'] in self._columns[row['table_name']]:
                    pass
                else:
                    self._columns[row['table_name']][row['column_name']] = row
            else:
                self._columns[row['table_name']] = {row['column_name']: row}

    # ------------------------------------------------------------------------------------------------------------------
    def _enhance_columns(self) -> None:
        """
        Enhances old_columns as follows:
        If the constant name is *, it is replaced with the column name prefixed by prefix in uppercase.
        Otherwise, the constant name is set to uppercase.
        """
        if self._old_columns:
            for table_name, table in sorted(self._old_columns.items()):
                for column_name, column in sorted(table.items()):
                    table_name = column['table_name']
                    column_name = column['column_name']

                    if 'constant_name' in column:
                        if column['constant_name'].strip() == '*':
                            constant_name = str(self._prefix + column['column_name']).upper()
                            self._old_columns[table_name][column_name]['constant_name'] = constant_name
                        else:
                            constant_name = str(self._old_columns[table_name][column_name]['constant_name']).upper()
                            self._old_columns[table_name][column_name]['constant_name'] = constant_name

    # ------------------------------------------------------------------------------------------------------------------
    def _merge_columns(self) -> None:
        """
        Preserves relevant data in old_columns into columns.
        """
        if self._old_columns:
            for table_name, table in sorted(self._old_columns.items()):
                for column_name, column in sorted(table.items()):
                    if 'constant_name' in column:
                        try:
                            self._columns[table_name][column_name]['constant_name'] = column['constant_name']
                        except KeyError:
                            # Either the column or table is not present anymore.
                            self._io.warning('Dropping constant {0} because column is not present anymore'.
                                             format(column['constant_name']))

    # ------------------------------------------------------------------------------------------------------------------
    def _write_columns(self) -> None:
        """
        Writes table and column names, the width of the column, and the constant name (if assigned) to
        constants_filename.
        """
        content = ''
        for _, table in sorted(self._columns.items()):
            width1 = 0
            width2 = 0

            key_map = {}
            for column_name, column in table.items():
                key_map[column['ordinal_position']] = column_name
                width1 = max(len(str(column['column_name'])), width1)
                width2 = max(len(str(column['length'])), width2)

            for _, column_name in sorted(key_map.items()):
                if table[column_name]['length'] is not None:
                    if 'constant_name' in table[column_name]:
                        line_format = "%s.%-{0:d}s %{1:d}d %s\n".format(int(width1), int(width2))
                        content += line_format % (table[column_name]['table_name'],
                                                  table[column_name]['column_name'],
                                                  table[column_name]['length'],
                                                  table[column_name]['constant_name'])
                    else:
                        line_format = "%s.%-{0:d}s %{1:d}d\n".format(int(width1), int(width2))
                        content += line_format % (table[column_name]['table_name'],
                                                  table[column_name]['column_name'],
                                                  table[column_name]['length'])

            content += "\n"

        # Save the columns, width and constants to the filesystem.
        Util.write_two_phases(self._constants_filename, content, self._io)

    # ------------------------------------------------------------------------------------------------------------------
    def _get_labels(self) -> None:
        """
        Gets all primary key labels from the MySQL database.
        """
        tables = self._dl.get_label_tables(self._label_regex)
        for table in tables:
            rows = self._dl.get_labels_from_table(table['table_name'], table['id'], table['label'])
            for row in rows:
                self._labels[row['label']] = row['id']

    # ------------------------------------------------------------------------------------------------------------------
    def _fill_constants(self) -> None:
        """
        Merges columns and labels (i.e. all known constants) into constants.
        """
        for table_name, table in sorted(self._columns.items()):
            for _, column in sorted(table.items()):
                if 'constant_name' in column:
                    self._constants[column['constant_name']] = column['length']

        for label, label_id in sorted(self._labels.items()):
            self._constants[label] = label_id

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def derive_field_length(column: Dict[str, Any]) -> int | None:
        """
        Returns the width of a field based on column.

        :param column: The column of which the field is based.
        """
        types_length = {'tinyint':    column['numeric_precision'],
                        'smallint':   column['numeric_precision'],
                        'mediumint':  column['numeric_precision'],
                        'int':        column['numeric_precision'],
                        'bigint':     column['numeric_precision'],
                        'decimal':    column['numeric_precision'],
                        'float':      column['numeric_precision'],
                        'double':     column['numeric_precision'],
                        'char':       column['character_maximum_length'],
                        'varchar':    column['character_maximum_length'],
                        'binary':     column['character_maximum_length'],
                        'varbinary':  column['character_maximum_length'],
                        'tinytext':   column['character_maximum_length'],
                        'text':       column['character_maximum_length'],
                        'json':       column['character_maximum_length'],
                        'mediumtext': column['character_maximum_length'],
                        'longtext':   column['character_maximum_length'],
                        'tinyblob':   column['character_maximum_length'],
                        'blob':       column['character_maximum_length'],
                        'mediumblob': column['character_maximum_length'],
                        'longblob':   column['character_maximum_length'],
                        'bit':        column['character_maximum_length'],
                        'timestamp':  16,
                        'year':       4,
                        'time':       8,
                        'date':       10,
                        'datetime':   16,
                        'inet6':      39,
                        'enum':       None,
                        'set':        None}

        if column['data_type'] in types_length:
            return types_length[column['data_type']]

        raise Exception("Unexpected type '{0!s}'.".format(column['data_type']))

# ----------------------------------------------------------------------------------------------------------------------
