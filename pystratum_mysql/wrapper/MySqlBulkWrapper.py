from pystratum_common.wrapper.CommonBulkWrapper import CommonBulkWrapper
from pystratum_common.wrapper.helper import WrapperContext

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlBulkWrapper(MySqlWrapper, CommonBulkWrapper):
    """
    Wrapper method generator for stored procedures with large result sets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: WrapperContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The loader context.
        """
        context.code_store.append_line(
                'return self.execute_sp_bulk(bulk_handler, {0})'.format(
                    self._generate_command(context.pystratum_metadata)))

# ----------------------------------------------------------------------------------------------------------------------
