"""
PyStratum

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""

from test.DataLayer import DataLayer
from test.StratumTestCase import StratumTestCase


class NoneTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test_sp1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        ret = DataLayer.tst_test_none(0)
        self.assertEqual(0, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sp2(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        ret = DataLayer.tst_test_none(1)
        self.assertEqual(1, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sp3(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        ret = DataLayer.tst_test_none(20)
        self.assertEqual(20, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        DataLayer.execute_none('drop temporary table if exists TMP_TMP')
        DataLayer.execute_none('create temporary table TMP_TMP( c bigint )')
        ret = DataLayer.execute_none('insert into TMP_TMP( c ) values(1)')
        self.assertEqual(1, ret, 'insert 1 row')
        ret = DataLayer.execute_none('insert into TMP_TMP( c ) values(2), (3)')
        self.assertEqual(2, ret, 'insert 2 rows')
        ret = DataLayer.execute_none('delete from TMP_TMP')
        self.assertEqual(3, ret, 'delete 3 rows')

# ----------------------------------------------------------------------------------------------------------------------
