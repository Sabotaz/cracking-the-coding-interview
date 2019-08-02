import unittest
from ddt import ddt, data
from src.exo_1_1 import uniq, uniq2, uniq3

@ddt
class UniqTestCase(unittest.TestCase):
    @data("abc d")
    def test_uniq(self, value):
        self.assertTrue(uniq(value))

    @data("aba", "  ")
    def test_not_uniq(self, value):
        self.assertFalse(uniq(value))

    @data("abc d")
    def test_uniq2(self, value):
        self.assertTrue(uniq2(value))

    @data("aba", "  ")
    def test_not_uniq2(self, value):
        self.assertFalse(uniq2(value))
    @data("abc d")
    def test_uniq3(self, value):
        self.assertTrue(uniq3(value))

    @data("aba", "  ")
    def test_not_uniq3(self, value):
        self.assertFalse(uniq3(value))
