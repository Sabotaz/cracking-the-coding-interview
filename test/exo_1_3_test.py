import unittest
from src.exo_1_3 import URLify
from golf.exo_1_3 import _ as URLify_golf

class URLifyTestCase(unittest.TestCase):
    def test_URLify(self):
        self.assertEquals(URLify(list("Mr John Smith    "), 13), list("Mr%20John%20Smith"))
        self.assertEquals(URLify_golf(list("Mr John Smith    "), 13), list("Mr%20John%20Smith"))
