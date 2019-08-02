import unittest
from ddt import ddt, data, unpack
from src.exo_1_5 import one_away
from golf.exo_1_5 import _ as one_away_golf

@ddt
class OneAwayTestCase(unittest.TestCase):

    @data(
        ["pale", "ple"],
        ["pales", "pale"],
        ["pale", "bale"]
    )
    @unpack
    def test_is_one_away(self, s1, s2):
        self.assertTrue(one_away(s1, s2))
        self.assertTrue(one_away_golf(s1, s2))

    @data(
        ["pale", "bake"]
    )
    @unpack
    def test_is_not_one_away(self, s1, s2):
        self.assertFalse(one_away(s1, s2))
        self.assertFalse(one_away_golf(s1, s2))
