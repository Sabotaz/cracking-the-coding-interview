import unittest
from src.exo_1_4 import is_palindrome_permutation
from golf.exo_1_4 import _ as is_palindrome_permutation_golf

class PalindromePermutationTestCase(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_palindrome_permutation("tact coa"))
        self.assertTrue(is_palindrome_permutation_golf("tact coa"))

    def test_is_not_permutation(self):
        self.assertFalse(is_palindrome_permutation("ab cb"))
        self.assertFalse(is_palindrome_permutation_golf("ab cb"))
