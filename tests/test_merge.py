#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for data cleaning
"""
import os
import random
import unittest
import csv
import filecmp
from clean import merge, split


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
        out_merge = os.path.join(data_folder, 'test_merge')
        contents_merge = os.listdir(out_merge)
        for content in contents_merge:
            path = os.path.join(out_merge, content)
            if os.path.isfile(path):
                os.remove(path)

        out_split = os.path.join(data_folder, 'test_split')
        contents_split = os.listdir(out_split)
        for content in contents_split:
            path = os.path.join(out_split, content)
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


    def test_round_trip(self):
        """ Test if splitting and merging results in the original file. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        # split files
        source_file = os.path.join(data_folder, 'source/two_objects.dat')
        out = os.path.join(data_folder, 'test_split')
        topics = split.list_topics_dat(source_file, [])
        split.split_dat_in_csv(topics, source_file, out)
        # merge file
        csv_files = merge.list_file_paths(data_folder + '/test_split')
        merged_file = os.path.join(os.getcwd(), 'tests/data/test_merge/merge-split.dat')
        data = merge.csv_to_dict(csv_files)
        merge.write_dict_to_dat(data, merged_file)
        # test if merged files are the same as original
        same = filecmp.cmp(source_file, merged_file, shallow=False)
        self.assertEquals(same, True)

if __name__ == '__main__':
    unittest.main()
