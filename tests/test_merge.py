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
        csv_files = merge.list_file_paths(data_folder + '/merge')
        self.assertEquals(len(csv_files), 3)


class TestMerge(unittest.TestCase):
    """ TestCase for csv file merging """

    def tearDown(self):
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        output_folder = os.path.join(data_folder, 'out')
        contents_output_folder = os.listdir(output_folder)
        for content in contents_output_folder:
            path = os.path.join(output_folder, content)
            if os.path.isfile(path):
                os.remove(path)


    def test_unicode(self):
        """ Test handling of non-ascii characters. """
        unicode_present = False
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        csv_files = merge.list_file_paths(data_folder + '/merge')
        merged_file = os.path.join(os.getcwd(), 'tests/data/out/merge-test-unicode.dat')
        data = merge.csv_to_dict(csv_files)
        merge.write_dict_to_dat(data, merged_file)
        with open(merged_file) as dat_file:
            if 'Rÿkßmusêum' in dat_file.read():
                unicode_present = True
        self.assertEquals(unicode_present, True)


    def test_order(self):
        """ Test retaining of order values. """
        order_retained = False
        csv_file = os.path.join(os.getcwd(), 'tests/data/merge/1_%0.csv')
        merged_file = os.path.join(os.getcwd(), 'tests/data/out/merge.dat')
        data_dict = merge.csv_to_dict([csv_file])
        merge.write_dict_to_dat(data_dict, merged_file)
        with open(merged_file) as dat_file:
            if '10000856\n%0 10000858' in dat_file.read():
                order_retained = True
        self.assertEquals(order_retained, True)


    def test_round_trip(self):
        """ Test if splitting and merging results in the original file. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        # split files
        source_file = os.path.join(data_folder, 'split/two_objects.dat')
        out = os.path.join(data_folder, 'out')
        topics = split.list_topics_dat(source_file, [])
        split.split_dat_in_csv(topics, source_file, out)
        # merge file
        csv_files = merge.list_file_paths(out)
        merged_file = os.path.join(os.getcwd(), 'tests/data/out/merge-split.dat')
        data = merge.csv_to_dict(csv_files)
        merge.write_dict_to_dat(data, merged_file)
        # test if merged files are the same as original
        same = filecmp.cmp(source_file, merged_file, shallow=False)
        self.assertEquals(same, True)

if __name__ == '__main__':
    unittest.main()
