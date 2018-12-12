"""
Unittests for data cleaning
"""
import os
import random
import unittest
import csv
from clean import merge


class TestListFiles(unittest.TestCase):
    """ TestCase for listing csv files in folder """

    def test_csv(self):
        """ Test listing csv files. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        csv_files1 = merge.list_file_paths(data_folder)
        csv_files2 = []
        self.assertEquals(csv_files1, csv_files2)


if __name__ == '__main__':
    unittest.main()
