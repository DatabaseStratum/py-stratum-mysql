from typing import Any, Dict

from pystratum_common.wrapper.Singleton0Wrapper import Singleton0Wrapper

from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


class MySqlSingleton0Wrapper(MySqlWrapper, Singleton0Wrapper):
    """
    Wrapper method generator for stored procedures that are selecting 0 or 1 row with one column only.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine: Dict[str, Any]) -> None:
        self._write_line('return self.execute_sp_singleton0({0!s})'.format(self._generate_command(routine)))

# ----------------------------------------------------------------------------------------------------------------------
