from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.Row1Wrapper import Row1Wrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlRow1Wrapper(MySqlWrapper, Row1Wrapper):
    """
    Wrapper method generator for stored procedures that are selecting 1 row.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_row1({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
