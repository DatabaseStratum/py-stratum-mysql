from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.TableWrapper import TableWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlTableWrapper(MySqlWrapper, TableWrapper):
    """
    Wrapper method generator for printing the result set of stored procedures in a table format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_table({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
