from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.Singleton1Wrapper import Singleton1Wrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlSingleton1Wrapper(Singleton1Wrapper, MySqlWrapper):
    """
    Wrapper method generator for stored procedures that are selecting 1 row with one column only.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_singleton1({0!s})'.format(str(self._generate_command(context.routine))))

# ----------------------------------------------------------------------------------------------------------------------
