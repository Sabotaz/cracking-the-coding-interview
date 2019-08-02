import unittest
from src.exo_1_2 import is_permutation
from golf.exo_1_2 import _ as is_permutation_golf

class PermutationTestCase(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_permutation("aboode", "odobae"))
        self.assertTrue(is_permutation_golf("aboode", "odobae"))

    def test_is_not_permutation(self):
        self.assertFalse(is_permutation("aboode", "odibae"))
        self.assertFalse(is_permutation_golf("aboode", "odibae"))
