from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.RowsWithIndexWrapper import RowsWithIndexWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlRowsWithIndexWrapper(RowsWithIndexWrapper, MySqlWrapper):
    """
    Wrapper method generator for stored procedures whose result set must be returned using tree structure using a
    combination of non-unique columns.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_execute_rows(self, context: BuildContext) -> None:
        """
        Builds the code for invoking the stored routine.

        :param context: The build context.
        """
        context.code_store.append_line(
                'rows = self.execute_sp_rows({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
