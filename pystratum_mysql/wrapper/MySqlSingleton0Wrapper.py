from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.Singleton0Wrapper import Singleton0Wrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlSingleton0Wrapper(MySqlWrapper, Singleton0Wrapper):
    """
    Wrapper method generator for stored procedures that are selecting 0 or 1 row with one column only.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_singleton0({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
