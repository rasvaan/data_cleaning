"""
Unittests for thesaurus analysis
"""
import os
import random
import unittest
from clean import split


class TestClean(unittest.TestCase):
    """ TestCase for basic data cleaning functions """

    def test_clean(self):
        """ Clean. """
        split.main()

if __name__ == '__main__':
    unittest.main()
