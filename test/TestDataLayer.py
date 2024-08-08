from pystratum_middle.BulkHandler import BulkHandler
from pystratum_mysql.MySqlDataLayer import MySqlDataLayer
from typing import Any
from typing import Dict
from typing import List


class TestDataLayer(MySqlDataLayer):
    """
    The stored routines wrappers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tst_constant01(self) -> Dict[str, Any]:
        """
        Test for constant.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_constant01()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant01(self) -> Any:
        """
        Test for magic constant.

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_magic_constant01()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant02(self) -> Any:
        """
        Test for magic constant.

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_magic_constant02()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant03(self) -> Any:
        """
        Test for magic constant.

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_magic_constant03()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant04(self) -> Any:
        """
        Test for magic constant.

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_magic_constant04()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types01(self, p_param00: int | None, p_param01: int | None, p_param02: int | None, p_param03: int | None, p_param04: int | None, p_param05: float | None, p_param06: float | None, p_param07: float | None, p_param08: int | None, p_param09: str | None, p_param10: str | None, p_param11: str | None, p_param12: str | None, p_param13: int | None, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None, p_param26: str | None, p_param27: str | None) -> int:
        """
        Test for all possible types of parameters excluding LOB's.

        :param int p_param00: Test parameter 00.
                              int(11)
        :param int p_param01: Test parameter 01.
                              smallint(6)
        :param int p_param02: Test parameter 02.
                              tinyint(4)
        :param int p_param03: Test parameter 03.
                              mediumint(9)
        :param int p_param04: Test parameter 04.
                              bigint(20)
        :param float p_param05: Test parameter 05.
                                decimal(10,2)
        :param float p_param06: Test parameter 06.
                                float
        :param float p_param07: Test parameter 07.
                                double
        :param int p_param08: Test parameter 08.
                              bit(8)
        :param str p_param09: Test parameter 09.
                              date
        :param str p_param10: Test parameter 10.
                              datetime
        :param str p_param11: Test parameter 11.
                              timestamp
        :param str p_param12: Test parameter 12.
                              time
        :param int p_param13: Test parameter 13.
                              year(4)
        :param str p_param14: Test parameter 14.
                              char(10) character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param15: Test parameter 15.
                              varchar(10) character set utf8mb4 collation utf8mb4_general_ci
        :param bytes p_param16: Test parameter 16.
                                binary(10)
        :param bytes p_param17: Test parameter 17.
                                varbinary(10)
        :param str p_param26: Test parameter 26.
                              enum('a','b') character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param27: Test parameter 27.
                              set('a','b') character set utf8mb4 collation utf8mb4_general_ci

        :rtype: int
        """
        return self.execute_sp_none("call tst_parameter_types01(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param26, p_param27)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types02(self, p_param00: int | None, p_param01: int | None, p_param02: int | None, p_param03: int | None, p_param04: int | None, p_param05: float | None, p_param06: float | None, p_param07: float | None, p_param08: int | None, p_param09: str | None, p_param10: str | None, p_param11: str | None, p_param12: str | None, p_param13: int | None, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None, p_param18: bytes | None, p_param19: bytes | None, p_param20: bytes | None, p_param21: bytes | None, p_param22: str | None, p_param23: str | None, p_param24: str | None, p_param25: str | None, p_param26: str | None, p_param27: str | None) -> int:
        """
        Test for all possible types of parameters including LOB's.

        :param int p_param00: Test parameter 00.
                              int(11)
        :param int p_param01: Test parameter 01.
                              smallint(6)
        :param int p_param02: Test parameter 02.
                              tinyint(4)
        :param int p_param03: Test parameter 03.
                              mediumint(9)
        :param int p_param04: Test parameter 04.
                              bigint(20)
        :param float p_param05: Test parameter 05.
                                decimal(10,2)
        :param float p_param06: Test parameter 06.
                                float
        :param float p_param07: Test parameter 07.
                                double
        :param int p_param08: Test parameter 08.
                              bit(8)
        :param str p_param09: Test parameter 09.
                              date
        :param str p_param10: Test parameter 10.
                              datetime
        :param str p_param11: Test parameter 11.
                              timestamp
        :param str p_param12: Test parameter 12.
                              time
        :param int p_param13: Test parameter 13.
                              year(4)
        :param str p_param14: Test parameter 14.
                              char(10) character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param15: Test parameter 15.
                              varchar(10) character set utf8mb4 collation utf8mb4_general_ci
        :param bytes p_param16: Test parameter 16.
                                binary(10)
        :param bytes p_param17: Test parameter 17.
                                varbinary(10)
        :param bytes p_param18: Test parameter 18.
                                tinyblob
        :param bytes p_param19: Test parameter 19.
                                blob
        :param bytes p_param20: Test parameter 20.
                                mediumblob
        :param bytes p_param21: Test parameter 21.
                                longblob
        :param str p_param22: Test parameter 22.
                              tinytext character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param23: Test parameter 23.
                              text character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param24: Test parameter 24.
                              mediumtext character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param25: Test parameter 25.
                              longtext character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param26: Test parameter 26.
                              enum('a','b') character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param27: Test parameter 27.
                              set('a','b') character set utf8mb4 collation utf8mb4_general_ci

        :rtype: int
        """
        return self.execute_sp_none("call tst_parameter_types02(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param18, p_param19, p_param20, p_param21, p_param22, p_param23, p_param24, p_param25, p_param26, p_param27)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_parameter_types03(self, p_param14: str | None, p_param15: str | None, p_param16: bytes | None, p_param17: bytes | None) -> int:
        """
        Test for all possible types of parameters with maximum length.

        :param str p_param14: Test parameter 14.
                              char(255) character set utf8mb4 collation utf8mb4_general_ci
        :param str p_param15: Test parameter 15.
                              varchar(4096) character set utf8mb4 collation utf8mb4_general_ci
        :param bytes p_param16: Test parameter 16.
                                binary(255)
        :param bytes p_param17: Test parameter 17.
                                varbinary(4096)

        :rtype: int
        """
        return self.execute_sp_none("call tst_parameter_types03(%s, %s, %s, %s)", p_param14, p_param15, p_param16, p_param17)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_bulk(self, bulk_handler: BulkHandler) -> int:
        """
        Test for designation type bulk.

        :param BulkHandler bulk_handler: The bulk handler for processing the selected rows.

        :rtype: int
        """
        return self.execute_sp_bulk(bulk_handler, "call tst_test_bulk()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_find_designation_type01(self) -> Dict[str, Any]:
        """
        Test for designation type.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_find_designation_type01()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_find_designation_type02(self) -> Dict[str, Any]:
        """
        Test for designation type.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_find_designation_type02()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_find_designation_type03(self) -> Dict[str, Any]:
        """
        Test for designation type.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_find_designation_type03()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_find_designation_type04(self) -> Dict[str, Any]:
        """
        Test for designation type.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_find_designation_type04()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_find_designation_type05(self) -> Dict[str, Any]:
        """
        Test for designation type.

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_find_designation_type05()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_function(self, p_a: int | None, p_b: int | None) -> Any:
        """
        Test for stored function wrapper.

        :param int p_a: Parameter A.
                        int(11)
        :param int p_b: Parameter B.
                        int(11)

        :rtype: Any
        """
        return self.execute_singleton1("select tst_test_function(%s, %s)", p_a, p_b)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_log(self) -> int:
        """
        Test for designation type log.

        :rtype: int
        """
        return self.execute_sp_log("call tst_test_log()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_max_allowed_packet(self, p_tmp_blob: bytes | None) -> Any:
        """
        Test for sending data larger than max_allowed_packet.

        :param bytes p_tmp_blob: The BLOB larger than max_allowed_packet.
                                 longblob

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_test_max_allowed_packet(%s)", p_tmp_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_multi(self) -> List[List[Dict[str, Any]]]:
        """
        Test for designation type multi.

        :rtype: List[List[Dict[str, Any]]]
        """
        return self.execute_sp_multi("call tst_test_multi()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none1(self, p_count: int | None) -> int:
        """
        Test for designation type none.

        :param int p_count: The number of iterations.
                            bigint(20)

        :rtype: int
        """
        return self.execute_sp_none("call tst_test_none1(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none2(self) -> int:
        """
        Test for designation type none.

        :rtype: int
        """
        return self.execute_sp_none("call tst_test_none2()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_none_with_lob(self, p_count: int | None, p_blob: bytes | None) -> int:
        """
        Test for designation type none with BLOB.

        :param int p_count: The number of iterations.
                            bigint(20)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: int
        """
        return self.execute_sp_none("call tst_test_none_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_percent_symbol(self) -> List[Dict[str, Any]]:
        """
        Test for stored function with percent symbols.

        :rtype: List[Dict[str, Any]]
        """
        return self.execute_sp_rows("call tst_test_percent_symbol()")

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row0a(self, p_count: int | None) -> Any:
        """
        Test for designation type row0.

        :param int p_count: The number of rows selected.
                            * 0 For a valid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)

        :rtype: Any
        """
        return self.execute_sp_row0("call tst_test_row0a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row0a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Any:
        """
        Test for designation type row0 with BLOB.

        :param int p_count: The number of rows selected.
                            * 0 For a valid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Any
        """
        return self.execute_sp_row0("call tst_test_row0a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1a(self, p_count: int | None) -> Dict[str, Any]:
        """
        Test for designation type row1.

        :param int p_count: The number of rows selected.
                            * 0 For an invalid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_row1a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict[str, Any]:
        """
        Test for designation type row1 with BLOB.

        :param int p_count: The number of rows selected.
                            * 0 For an invalid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Dict[str, Any]
        """
        return self.execute_sp_row1("call tst_test_row1a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows1(self, p_count: int | None) -> List[Dict[str, Any]]:
        """
        Test for designation type row1.

        :param int p_count: The number of rows selected.
                            * 0 For an invalid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)

        :rtype: List[Dict[str, Any]]
        """
        return self.execute_sp_rows("call tst_test_rows1(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> List[Dict[str, Any]]:
        """
        Test for designation type rows.

        :param int p_count: The number of rows selected.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: List[Dict[str, Any]]
        """
        return self.execute_sp_rows("call tst_test_rows1_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_index1(self, p_count: int | None) -> Dict:
        """
        Test for designation type rows_with_index.

        :param int p_count: The number of rows selected.
                            int(11)

        :rtype: Dict
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_index1(%s)", p_count)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    ret[row['tst_c01']][row['tst_c02']].append(row)
                else:
                    ret[row['tst_c01']][row['tst_c02']] = [row]
            else:
                ret[row['tst_c01']] = {row['tst_c02']: [row]}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_index1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict:
        """
        Test for designation type rows_with_index with BLOB.

        :param int p_count: The number of rows selected.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Dict
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_index1_with_lob(%s, %s)", p_count, p_blob)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    ret[row['tst_c01']][row['tst_c02']].append(row)
                else:
                    ret[row['tst_c01']][row['tst_c02']] = [row]
            else:
                ret[row['tst_c01']] = {row['tst_c02']: [row]}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_key1(self, p_count: int | None) -> Dict:
        """
        Test for designation type rows_with_key.

        :param int p_count: Number of rows selected.
                            int(11)

        :rtype: Dict
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_key1(%s)", p_count)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    if row['tst_c03'] in ret[row['tst_c01']][row['tst_c02']]:
                        raise Exception('Duplicate key for %s.' % str((row['tst_c01'], row['tst_c02'], row['tst_c03'])))
                    else:
                        ret[row['tst_c01']][row['tst_c02']][row['tst_c03']] = row
                else:
                    ret[row['tst_c01']][row['tst_c02']] = {row['tst_c03']: row}
            else:
                ret[row['tst_c01']] = {row['tst_c02']: {row['tst_c03']: row}}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_key1_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Dict:
        """
        Test for designation type rows_with_key with BLOB.

        :param int p_count: The number of rows selected.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Dict
        """
        ret = {}
        rows = self.execute_sp_rows("call tst_test_rows_with_key1_with_lob(%s, %s)", p_count, p_blob)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    if row['tst_c03'] in ret[row['tst_c01']][row['tst_c02']]:
                        raise Exception('Duplicate key for %s.' % str((row['tst_c01'], row['tst_c02'], row['tst_c03'])))
                    else:
                        ret[row['tst_c01']][row['tst_c02']][row['tst_c03']] = row
                else:
                    ret[row['tst_c01']][row['tst_c02']] = {row['tst_c03']: row}
            else:
                ret[row['tst_c01']] = {row['tst_c02']: {row['tst_c03']: row}}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0a(self, p_count: int | None) -> Any:
        """
        Test for designation type singleton0.

        :param int p_count: The number of rows selected.
                            * 0 For a valid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)

        :rtype: Any
        """
        return self.execute_sp_singleton0("call tst_test_singleton0a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Any:
        """
        Test for designation type singleton0 with BLOB..

        :param int p_count: The number of rows selected.
                            * 0 For a valid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Any
        """
        return self.execute_sp_singleton0("call tst_test_singleton0a_with_lob(%s, %s)", p_count, p_blob)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1a(self, p_count: int | None) -> Any:
        """
        Test for designation type singleton1.

        :param int p_count: The number of rows selected.
                            * 0 For an invalid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_test_singleton1a(%s)", p_count)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1a_with_lob(self, p_count: int | None, p_blob: bytes | None) -> Any:
        """
        Test for designation type singleton1 with BLOB.

        :param int p_count: The number of rows selected.
                            * 0 For an invalid test.
                            * 1 For a valid test.
                            * 2 For an invalid test.
                            int(11)
        :param bytes p_blob: The BLOB.
                             blob

        :rtype: Any
        """
        return self.execute_sp_singleton1("call tst_test_singleton1a_with_lob(%s, %s)", p_count, p_blob)

# ----------------------------------------------------------------------------------------------------------------------
