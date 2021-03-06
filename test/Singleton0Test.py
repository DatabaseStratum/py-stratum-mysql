from pystratum_middle.exception.ResultException import ResultException

from test.StratumTestCase import StratumTestCase


class Singleton0Test(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type singleton0 must return null.
        """
        ret = self._dl.tst_test_singleton0a(0)
        self.assertIsNone(ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        Stored routine with designation type singleton0 must return 1 value.
        """
        ret = self._dl.tst_test_singleton0a(1)
        self.assertIsInstance(ret, (str, int, float))

    # ------------------------------------------------------------------------------------------------------------------
    def test3(self):
        """
        An exception must be thrown when a stored routine with designation type singleton0 returns more than 1 values.
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_singleton0a(2)

# ----------------------------------------------------------------------------------------------------------------------
