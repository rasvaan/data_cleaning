#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for data cleaning
"""
import os
import random
import unittest
import csv
from clean import split


class TestListTopics(unittest.TestCase):
    """ TestCase for listing topics in .dat file """

    def test_topics_one(self):
        """ Test listing topics from one record. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/one_object.dat')
        ignore = ['IN', 'I3']
        topics1 = split.list_topics_dat(source, ignore)
        topics2 = set([u'%0', u'BA', u'BE', u'MP', u'mP'])
        self.assertEquals(topics1, topics2)

    def test_topics_two(self):
        """ Test listing topics from two records. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/two_objects.dat')
        topics1 = split.list_topics_dat(source, [])
        topics2 = set([u'%0', u'BA', u'BE'])
        self.assertEquals(topics1, topics2)

    def test_topics_break(self):
        """ Test listing topics from file with line break. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/line_break.dat')
        topics1 = split.list_topics_dat(source, [])
        topics2 = set([u'%0', u'BA', u'TF'])
        self.assertEquals(topics1, topics2)

class TestOutputSplits(unittest.TestCase):
    """ TestCase for outputting split files """

    def tearDown(self):
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        out = os.path.join(data_folder, 'test_split')
        contents = os.listdir(out)

        for content in contents:
            path = os.path.join(out, content)
            if os.path.isfile(path):
                os.remove(path)

    def test_split_in_csv(self):
        """ Test csv creation. """
        topics = set([u'%0', u'BA', u'BE', u'MP', u'mP'])
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/one_object.dat')
        out = os.path.join(data_folder, 'test_split')
        split.split_dat_in_csv(topics, source, out)
        files1 = os.listdir(out)
        files2 = ['1_%0.csv', '2_BA.csv', '3_BE.csv', '4_MP.csv', '5_mP.csv']
        self.assertEquals(len(files1), len(files2))
        self.assertEquals(set(files1), set(files2))

    def test_add_values_one_record(self):
        """ Test outputting csv file of one record and topic. """
        topic = u'BE'
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/one_object.dat')
        out = os.path.join(data_folder, 'test_split')
        split_file = os.path.join(out, topic + '.csv')
        file = open(split_file, 'w')
        writer = csv.writer(file)
        split.add_dat_values(topic, source, writer)
        file.close()
        number_lines = sum(1 for line in open(split_file))
        self.assertEquals(number_lines, 1)

    def test_add_values_two_records(self):
        """ Test outputting csv file of two records and one topic. """
        topic = u'BE'
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/two_objects.dat')
        out = os.path.join(data_folder, 'test_split')
        split_file = os.path.join(out, topic + '.csv')
        file = open(split_file, 'w')
        writer = csv.writer(file)
        split.add_dat_values(topic, source, writer)
        file.close()
        number_lines = sum(1 for line in open(split_file))
        self.assertEquals(number_lines, 2)

    def test_add_line_break(self):
        """ Test outputting csv file of records with value containing line break. """
        topic = u'TF'
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/line_break.dat')
        out = os.path.join(data_folder, 'test_split')
        split_file = os.path.join(out, topic + '.csv')
        file = open(split_file, 'w')
        writer = csv.writer(file)
        split.add_dat_values(topic, source, writer)
        file.close()
        number_lines = sum(1 for line in open(split_file))
        self.assertEquals(number_lines, 2)

    def test_add_line_break_other(self):
        """ Test outputting csv file of records with value containing line break, but focussing on other value. """
        topic = u'BA'
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'source/line_break.dat')
        out = os.path.join(data_folder, 'test_split')
        split_file = os.path.join(out, topic + '.csv')
        file = open(split_file, 'w')
        writer = csv.writer(file)
        split.add_dat_values(topic, source, writer)
        file.close()
        number_lines = sum(1 for line in open(split_file))
        self.assertEquals(number_lines, 2)

if __name__ == '__main__':
    unittest.main()
