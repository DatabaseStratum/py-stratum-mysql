import sys
import unittest
from io import StringIO

from pystratum_mysql.MySqlDefaultConnector import MySqlDefaultConnector
from test.TestDataLayer import TestDataLayer


class StratumTestCase(unittest.TestCase):
    def __init__(self, method_name):
        """
        Object constructor.
        """
        super().__init__(method_name)

        params = {'host':     'localhost',
                  'user':     'test',
                  'password': 'test',
                  'database': 'test'}

        self._dl: TestDataLayer = TestDataLayer(MySqlDefaultConnector(params))
        """
        The generated data layer.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def setUp(self):
        self._dl.connect()

        self.held, sys.stdout = sys.stdout, StringIO()

    # ------------------------------------------------------------------------------------------------------------------
    def tearDown(self):
        sys.stdout = self.held
        self._dl.disconnect()

# ----------------------------------------------------------------------------------------------------------------------
