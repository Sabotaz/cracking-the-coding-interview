import unittest
from ddt import ddt, data, unpack
from src.exo_1_1 import uniq, uniq2, uniq3
from golf.exo_1_1 import _ as uniq_golf

@ddt
class UniqTestCase(unittest.TestCase):
    @data(uniq, uniq2, uniq3, uniq_golf)
    def test_uniq(self, method):
        self.assertTrue(method("abc d"))

    @data(uniq, uniq2, uniq3, uniq_golf)
    def test_not_uniq(self, method):
        self.assertFalse(method("aba"))
        self.assertFalse(method("  "))
