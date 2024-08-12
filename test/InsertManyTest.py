from test.StratumTestCase import StratumTestCase


class InsertManyTest(StratumTestCase):
    """
    Test cases for designation type insert_many.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_with_ignoring_columns(self):
        """
        Test with ignored columns.
        """
        rows = [{'field1': 1,
                 'field4': 4,
                 'field5': 5},
                {'field1': 11,
                 'field4': 14,
                 'field5': 15},
                {'field1': 21,
                 'field4': 24,
                 'field5': 25}]

        count1 = self._dl.tst_test_insert_many02(rows)
        self.assertEqual(3, count1)

        count2 = self._dl.execute_singleton1('select count(*) from TST_TEMPO')
        self.assertEqual(3, count2)

# ----------------------------------------------------------------------------------------------------------------------
