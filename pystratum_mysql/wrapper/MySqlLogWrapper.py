from typing import Any, Dict

from pystratum_common.wrapper.LogWrapper import LogWrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlLogWrapper(MySqlWrapper, LogWrapper):
    """
    Wrapper method generator for stored procedures with designation type log.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine: Dict[str, Any]) -> None:
        self._write_line('return self.execute_sp_log({0!s})'.format(self._generate_command(routine)))

# ----------------------------------------------------------------------------------------------------------------------
