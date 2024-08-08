from pystratum_common.BuildContext import BuildContext
from pystratum_common.wrapper.BulkWrapper import BulkWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlBulkWrapper(MySqlWrapper, BulkWrapper):
    """
    Wrapper method generator for stored procedures with large result sets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: BuildContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        """
        context.code_store.append_line(
                'return self.execute_sp_bulk(bulk_handler, {0})'.format(self._generate_command(context.routine)))

# ----------------------------------------------------------------------------------------------------------------------
