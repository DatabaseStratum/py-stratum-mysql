"""
PyStratum

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""
import os

from test.DataLayer import DataLayer
from test.StratumTestCase import StratumTestCase


class LabelTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Test labels.
        """
        ret = DataLayer.tst_test_label()
        dir_cur_file = os.path.dirname(os.path.abspath(__file__))
        path = os.path.realpath(dir_cur_file + "/etc/config.txt")
        with open(path) as f:
            lines = f.read().splitlines()
        for row in ret:
            label = row['tst_label']
            label += ' = '
            label += str(row['tst_id'])
            self.assertTrue(label in lines)

# ----------------------------------------------------------------------------------------------------------------------
