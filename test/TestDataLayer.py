from pystratum_middle.BulkHandler import BulkHandler
from pystratum_mysql.MySqlDataLayer import MySqlDataLayer
from typing import Any
from typing import Dict
from typing import List


class TestDataLayer(MySqlDataLayer):
    """
    The stored routines wrappers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tst_constant01(self) -> Dict[str, Any]:
        """
        Test for constant.
        """
        return self.execute_sp_row1("call tst_constant01()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant01(self) -> str:
        """
        Test for magic constant.
        """
        return self.execute_sp_singleton1("call tst_magic_constant01()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant02(self) -> int:
        """
        Test for magic constant.
        """
        return self.execute_sp_singleton1("call tst_magic_constant02()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant03(self) -> str:
        """
        Test for magic constant.
        """
        return self.execute_sp_singleton1("call tst_magic_constant03()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant04(self) -> str:
        """
        Test for magic constant.
        """
        return self.execute_sp_singleton1("call tst_magic_constant04()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types01(self, p_param00: int | None, p_param01: int | None, p_param02: int | None, p_param03: int | None, p_param04: int | None, p_param05: float | None, p_param06: float | None, p_param07: float | None, p_param08: int | None, p_param09: str | None, p_param10: str | None, p_param11: str | None, p_param12: str | None, p_param13: int | None, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None, p_param26: str | None, p_param27: str | None) -> int:
        """
        Test for all possible types of parameters excluding LOB's.

        :param p_param00: Test parameter 00.
                          RDBMS data type: int(11)
        :param p_param01: Test parameter 01.
                          RDBMS data type: smallint(6)
        :param p_param02: Test parameter 02.
                          RDBMS data type: tinyint(4)
        :param p_param03: Test parameter 03.
                          RDBMS data type: mediumint(9)
        :param p_param04: Test parameter 04.
                          RDBMS data type: bigint(20)
        :param p_param05: Test parameter 05.
                          RDBMS data type: decimal(10,2)
        :param p_param06: Test parameter 06.
                          RDBMS data type: float
        :param p_param07: Test parameter 07.
                          RDBMS data type: double
        :param p_param08: Test parameter 08.
                          RDBMS data type: bit(8)
        :param p_param09: Test parameter 09.
                          RDBMS data type: date
        :param p_param10: Test parameter 10.
                          RDBMS data type: datetime
        :param p_param11: Test parameter 11.
                          RDBMS data type: timestamp
        :param p_param12: Test parameter 12.
                          RDBMS data type: time
        :param p_param13: Test parameter 13.
                          RDBMS data type: year(4)
        :param p_param14: Test parameter 14.
                          RDBMS data type: char(10) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param15: Test parameter 15.
                          RDBMS data type: varchar(10) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param16: Test parameter 16.
                          RDBMS data type: binary(10)
        :param p_param17: Test parameter 17.
                          RDBMS data type: varbinary(10)
        :param p_param26: Test parameter 26.
                          RDBMS data type: enum('a','b') character set utf8mb4 collation utf8mb4_general_ci
        :param p_param27: Test parameter 27.
                          RDBMS data type: set('a','b') character set utf8mb4 collation utf8mb4_general_ci
        """
        return self.execute_sp_none("call tst_parameter_types01(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param26, p_param27)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types02(self, p_param00: int | None, p_param01: int | None, p_param02: int | None, p_param03: int | None, p_param04: int | None, p_param05: float | None, p_param06: float | None, p_param07: float | None, p_param08: int | None, p_param09: str | None, p_param10: str | None, p_param11: str | None, p_param12: str | None, p_param13: int | None, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None, p_param18: bytes | None, p_param19: bytes | None, p_param20: bytes | None, p_param21: bytes | None, p_param22: str | None, p_param23: str | None, p_param24: str | None, p_param25: str | None, p_param26: str | None, p_param27: str | None) -> int:
        """
        Test for all possible types of parameters including LOB's.

        :param p_param00: Test parameter 00.
                          RDBMS data type: int(11)
        :param p_param01: Test parameter 01.
                          RDBMS data type: smallint(6)
        :param p_param02: Test parameter 02.
                          RDBMS data type: tinyint(4)
        :param p_param03: Test parameter 03.
                          RDBMS data type: mediumint(9)
        :param p_param04: Test parameter 04.
                          RDBMS data type: bigint(20)
        :param p_param05: Test parameter 05.
                          RDBMS data type: decimal(10,2)
        :param p_param06: Test parameter 06.
                          RDBMS data type: float
        :param p_param07: Test parameter 07.
                          RDBMS data type: double
        :param p_param08: Test parameter 08.
                          RDBMS data type: bit(8)
        :param p_param09: Test parameter 09.
                          RDBMS data type: date
        :param p_param10: Test parameter 10.
                          RDBMS data type: datetime
        :param p_param11: Test parameter 11.
                          RDBMS data type: timestamp
        :param p_param12: Test parameter 12.
                          RDBMS data type: time
        :param p_param13: Test parameter 13.
                          RDBMS data type: year(4)
        :param p_param14: Test parameter 14.
                          RDBMS data type: char(10) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param15: Test parameter 15.
                          RDBMS data type: varchar(10) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param16: Test parameter 16.
                          RDBMS data type: binary(10)
        :param p_param17: Test parameter 17.
                          RDBMS data type: varbinary(10)
        :param p_param18: Test parameter 18.
                          RDBMS data type: tinyblob
        :param p_param19: Test parameter 19.
                          RDBMS data type: blob
        :param p_param20: Test parameter 20.
                          RDBMS data type: mediumblob
        :param p_param21: Test parameter 21.
                          RDBMS data type: longblob
        :param p_param22: Test parameter 22.
                          RDBMS data type: tinytext character set utf8mb4 collation utf8mb4_general_ci
        :param p_param23: Test parameter 23.
                          RDBMS data type: text character set utf8mb4 collation utf8mb4_general_ci
        :param p_param24: Test parameter 24.
                          RDBMS data type: mediumtext character set utf8mb4 collation utf8mb4_general_ci
        :param p_param25: Test parameter 25.
                          RDBMS data type: longtext character set utf8mb4 collation utf8mb4_general_ci
        :param p_param26: Test parameter 26.
                          RDBMS data type: enum('a','b') character set utf8mb4 collation utf8mb4_general_ci
        :param p_param27: Test parameter 27.
                          RDBMS data type: set('a','b') character set utf8mb4 collation utf8mb4_general_ci
        """
        return self.execute_sp_none("call tst_parameter_types02(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param18, p_param19, p_param20, p_param21, p_param22, p_param23, p_param24, p_param25, p_param26, p_param27)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types03(self, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None) -> int:
        """
        Test for all possible types of parameters with maximum length.

        :param p_param14: Test parameter 14.
                          RDBMS data type: char(255) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param15: Test parameter 15.
                          RDBMS data type: varchar(4096) character set utf8mb4 collation utf8mb4_general_ci
        :param p_param16: Test parameter 16.
                          RDBMS data type: binary(255)
        :param p_param17: Test parameter 17.
                          RDBMS data type: varbinary(4096)
        """
        return self.execute_sp_none("call tst_parameter_types03(%s, %s, %s, %s)", p_param14, p_param15, p_param16, p_param17)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_bulk(self, bulk_handler: BulkHandler) -> int:
        """
        Test for designation type bulk.

        :param bulk_handler: The bulk handler for processing the selected rows.
        """
        return self.execute_sp_bulk(bulk_handler, "call tst_test_bulk()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_function(self, p_a: int | None, p_b: int | None) -> int:
        """
        Test for stored function wrapper.

        :param p_a: Parameter A.
                    RDBMS data type: int(11)
        :param p_b: Parameter B.
                    RDBMS data type: int(11)
        """
        return self.execute_singleton1("select tst_test_function(%s, %s)", p_a, p_b)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_insert_many01(self, rows: List[Dict[str, Any]]) -> int:
        """
        Test for designation insert_many.

        :param rows: The rows that must be inserted.
        """
        keys = ['field_int', 'field_smallint', 'field_mediumint', 'field_tinyint', 'field_bigint', 'field_int_unsigned', 'field_smallint_unsigned', 'field_mediumint_unsigned', 'field_tinyint_unsigned', 'field_bigint_unsigned', 'field_year', 'field_decimal', 'field_decimal0', 'field_float', 'field_double', 'field_binary', 'field_varbinary', 'field_char', 'field_varchar', 'field_time', 'field_timestamp', 'field_date', 'field_datetime', 'field_enum', 'field_set', 'field_bit']
        my_rows = list(tuple(row[key] for key in keys) for row in rows)
        sql = """
insert into `TST_TEMPO` (`tst_int`, `tst_smallint`, `tst_tinyint`, `tst_mediumint`, `tst_bigint`, `tst_decimal`, `tst_float`, `tst_double`, `tst_bit`, `tst_date`, `tst_datetime`, `tst_timestamp`, `tst_time`, `tst_year`, `tst_char`, `tst_varchar`, `tst_binary`, `tst_varbinary`, `tst_tinyblob`, `tst_blob`, `tst_mediumblob`, `tst_longblob`, `tst_tinytext`, `tst_text`, `tst_mediumtext`, `tst_longtext`)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.execute_sp_none("call tst_test_insert_many01()")

        return self.execute_many(sql, my_rows)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_insert_many02(self, rows: List[Dict[str, Any]]) -> int:
        """
        Test for designation insert_many.

        :param rows: The rows that must be inserted.
        """
        keys = ['field1', 'field4', 'field5']
        my_rows = list(tuple(row[key] for key in keys) for row in rows)
        sql = """
insert into `TST_TEMPO` (`tst_col1`, `tst_col4`, `tst_col5`)
values (%s, %s, %s)
        """

        self.execute_sp_none("call tst_test_insert_many02()")

        return self.execute_many(sql, my_rows)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_log(self) -> int:
        """
        Test for designation type log.
        """
        return self.execute_sp_log("call tst_test_log()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_max_allowed_packet(self, p_tmp_blob: bytes | None) -> str:
        """
        Test for sending data larger than max_allowed_packet.

        :param p_tmp_blob: The BLOB larger than max_allowed_packet.
                           RDBMS data type: longblob
        """
        return self.execute_sp_singleton1("call tst_test_max_allowed_packet(%s)", p_tmp_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_multi(self) -> List[List[Dict[str, Any]]]:
        """
        Test for designation type multi.
        """
        return self.execute_sp_multi("call tst_test_multi()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none1(self, p_count: int | None) -> int:
        """
        Test for designation type none.

        :param p_count: The number of iterations.
                        RDBMS data type: bigint(20)
        """
        return self.execute_sp_none("call tst_test_none1(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none2(self) -> int:
        """
        Test for designation type none.
        """
        return self.execute_sp_none("call tst_test_none2()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none_with_lob(self, p_count: int | None, p_blob: bytes | None) -> int:
        """
        Test for designation type none with BLOB.

        :param p_count: The number of iterations.
                        RDBMS data type: bigint(20)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_none("call tst_test_none_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_percent_symbol(self) -> List[Dict[str, Any]]:
        """
        Test for stored function with percent symbols.
        """
        return self.execute_sp_rows("call tst_test_percent_symbol()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row0a(self, p_count: int | None) -> Any:
        """
        Test for designation type row0.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        """
        return self.execute_sp_row0("call tst_test_row0a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row0a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Any:
        """
        Test for designation type row0 with BLOB.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_row0("call tst_test_row0a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1a(self, p_count: int | None) -> Dict[str, Any]:
        """
        Test for designation type row1.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        """
        return self.execute_sp_row1("call tst_test_row1a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict[str, Any]:
        """
        Test for designation type row1 with BLOB.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_row1("call tst_test_row1a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows1(self, p_count: int | None) -> List[Dict[str, Any]]:
        """
        Test for designation type row1.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        """
        return self.execute_sp_rows("call tst_test_rows1(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> List[Dict[str, Any]]:
        """
        Test for designation type rows.

        :param p_count: The number of rows selected.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_rows("call tst_test_rows1_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_index1(self, p_count: int | None) -> Dict:
        """
        Test for designation type rows_with_index.

        :param p_count: The number of rows selected.
                        RDBMS data type: int(11)
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_index1(%s)", p_count)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    ret[row['tst_c01']][row['tst_c02']].append(row)
                else:
                    ret[row['tst_c01']][row['tst_c02']] = [row]
            else:
                ret[row['tst_c01']] = {row['tst_c02']: [row]}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_index1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict:
        """
        Test for designation type rows_with_index with BLOB.

        :param p_count: The number of rows selected.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_index1_with_lob(%s, %s)", p_count, p_blob)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    ret[row['tst_c01']][row['tst_c02']].append(row)
                else:
                    ret[row['tst_c01']][row['tst_c02']] = [row]
            else:
                ret[row['tst_c01']] = {row['tst_c02']: [row]}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_key1(self, p_count: int | None) -> Dict:
        """
        Test for designation type rows_with_key.

        :param p_count: Number of rows selected.
                        RDBMS data type: int(11)
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_key1(%s)", p_count)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    if row['tst_c03'] in ret[row['tst_c01']][row['tst_c02']]:
                        raise Exception('Duplicate key for %s.' % str((row['tst_c01'], row['tst_c02'], row['tst_c03'])))
                    else:
                        ret[row['tst_c01']][row['tst_c02']][row['tst_c03']] = row
                else:
                    ret[row['tst_c01']][row['tst_c02']] = {row['tst_c03']: row}
            else:
                ret[row['tst_c01']] = {row['tst_c02']: {row['tst_c03']: row}}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_key1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict:
        """
        Test for designation type rows_with_key with BLOB.

        :param p_count: The number of rows selected.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_key1_with_lob(%s, %s)", p_count, p_blob)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    if row['tst_c03'] in ret[row['tst_c01']][row['tst_c02']]:
                        raise Exception('Duplicate key for %s.' % str((row['tst_c01'], row['tst_c02'], row['tst_c03'])))
                    else:
                        ret[row['tst_c01']][row['tst_c02']][row['tst_c03']] = row
                else:
                    ret[row['tst_c01']][row['tst_c02']] = {row['tst_c03']: row}
            else:
                ret[row['tst_c01']] = {row['tst_c02']: {row['tst_c03']: row}}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0a(self, p_count: int | None) -> int | None:
        """
        Test for designation type singleton0.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        """
        return self.execute_sp_singleton0("call tst_test_singleton0a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> int | None:
        """
        Test for designation type singleton0 with BLOB.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_singleton0("call tst_test_singleton0a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1a(self, p_count: int | None) -> int:
        """
        Test for designation type singleton1.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        """
        return self.execute_sp_singleton1("call tst_test_singleton1a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> bool:
        """
        Test for designation type singleton1 with BLOB.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int(11)
        :param p_blob: The BLOB.
                       RDBMS data type: blob
        """
        return self.execute_sp_singleton1("call tst_test_singleton1a_with_lob(%s, %s)", p_count, p_blob) not in [None, '']

# ----------------------------------------------------------------------------------------------------------------------
