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

class TestListTopics(unittest.TestCase):
    """ TestCase for listing topics in .dat file """

    def test_topics_one(self):
        """ Test listing topics from one record. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'one_object.dat')
        ignore = ['IN', 'I3']
        topics1 = split.list_topics_dat(source, ignore)
        topics2 = set([u'%0', u'BA', u'BE'])
        print(topics1, topics2)
        self.assertEquals(topics1, topics2)

    def test_topics_two(self):
        """ Test listing topics from two records. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'two_objects.dat')
        topics1 = split.list_topics_dat(source, [])
        topics2 = set([u'%0', u'BA', u'BE'])
        print(topics1, topics2)
        self.assertEquals(topics1, topics2)

    def test_topics_break(self):
        """ Test listing topics from file with line break. """
        data_folder = os.path.join(os.getcwd(), 'tests/data')
        source = os.path.join(data_folder, 'line_break.dat')
        topics1 = split.list_topics_dat(source, [])
        topics2 = set([u'%0', u'BE', u'TF'])
        print(topics1, topics2)
        self.assertEquals(topics1, topics2)



if __name__ == '__main__':
    unittest.main()
