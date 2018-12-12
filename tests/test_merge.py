#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for data cleaning
"""
import os
import random
import unittest
import csv
from clean import merge


class TestListCsvFiles(unittest.TestCase):
    """ TestCase for listing csv files """

    def test_csv(self):
        """ Test listing csv files. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        csv_files = merge.list_file_paths(data_folder + '/source')
        self.assertEquals(len(csv_files), 3)


class TestMerge(unittest.TestCase):
    """ TestCase for csv file merging """

    def tearDown(self):
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        out = os.path.join(data_folder, 'test_merge')
        contents = os.listdir(out)

        for content in contents:
            path = os.path.join(out, content)
            if os.path.isfile(path):
                os.remove(path)


    def test_unicode(self):
        """ Test handling of non-ascii characters. """
        unicode_present = False
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        csv_files = merge.list_file_paths(data_folder + '/source')
        merged_file = os.path.join(os.getcwd(), 'tests/data/test_merge/merge-test-unicode.dat')
        data = merge.csv_to_dict(csv_files)
        merge.write_dict_to_dat(data, merged_file)
        with open(merged_file) as dat_file:
            if 'Rÿkßmusêum' in dat_file.read():
                unicode_present = True
        self.assertEquals(unicode_present, True)


    def test_order(self):
        """ Test retaining of order values. """
        csv_file = os.path.join(os.getcwd(), 'tests/data/source/1_%0.csv')
        merged_file = os.path.join(os.getcwd(), 'tests/data/test_merge/merge.dat')
        data_dict = merge.csv_to_dict([csv_file])
        merge.write_dict_to_dat(data_dict, merged_file)
        with open(merged_file) as dat_file:
            if '%0 10000856\r\n%0 10000858' in dat_file.read():
                unicode_present = True
        self.assertEquals(unicode_present, True)


if __name__ == '__main__':
    unittest.main()
