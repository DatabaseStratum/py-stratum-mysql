from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.FunctionsWrapper import FunctionsWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlFunctionsWrapper(MySqlWrapper, FunctionsWrapper):
    """
    Wrapper method generator for stored functions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_singleton1({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
