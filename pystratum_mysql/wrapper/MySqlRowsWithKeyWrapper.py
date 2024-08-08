from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.RowsWithKeyWrapper import RowsWithKeyWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlRowsWithKeyWrapper(RowsWithKeyWrapper, MySqlWrapper):
    """
    Wrapper method generator for stored procedures whose result set must be returned using tree structure using a
    combination of unique columns.
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
