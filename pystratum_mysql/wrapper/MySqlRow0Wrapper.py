from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.Row0Wrapper import Row0Wrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlRow0Wrapper(MySqlWrapper, Row0Wrapper):
    """
    Wrapper method generator for stored procedures that are selecting 0 or 1 row.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_row0({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
