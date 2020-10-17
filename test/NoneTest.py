from test.StratumTestCase import StratumTestCase


class NoneTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test_sp1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        self._dl.tst_test_none1(0)

        ret = self._dl.tst_test_none2()
        self.assertEqual(0, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sp2(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        self._dl.tst_test_none1(1)

        ret = self._dl.tst_test_none2()
        self.assertEqual(1, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sp3(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        self._dl.tst_test_none1(20)

        ret = self._dl.tst_test_none2()
        self.assertEqual(20, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        self._dl.execute_none('drop temporary table if exists TMP_TMP')
        self._dl.execute_none('create temporary table TMP_TMP( c bigint )')
        ret = self._dl.execute_none('insert into TMP_TMP( c ) values(1)')
        self.assertEqual(1, ret, 'insert 1 row')
        ret = self._dl.execute_none('insert into TMP_TMP( c ) values(2), (3)')
        self.assertEqual(2, ret, 'insert 2 rows')
        ret = self._dl.execute_none('delete from TMP_TMP')
        self.assertEqual(3, ret, 'delete 3 rows')

# ----------------------------------------------------------------------------------------------------------------------
