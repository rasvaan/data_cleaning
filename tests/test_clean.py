"""
Unittests for data cleaning
"""
import os
import random
import unittest
from clean import split


class TestClean(unittest.TestCase):
    """ TestCase for basic data cleaning functions """

    def test_clean(self):
        """ Split dat file. """
        split.split_dat()

if __name__ == '__main__':
    unittest.main()
