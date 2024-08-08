from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.MultiWrapper import MultiWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlMultiWrapper(MySqlWrapper, MultiWrapper):
    """
    Wrapper method generator for stored procedures with designation type multi.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_multi({0!s})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
