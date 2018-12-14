#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Split Adlib

Split exported Adlib files in multiple csv files, each containing ids and one
type of value. After the values are cleaned, they can be exported again.
"""

__author__ = "Chris Dijkshoorn"
__version__ = "0.0.3"
__license__ = "MIT"


import os
import io
import csv
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='split.log',
    level=logging.INFO
)

def split_dat():
    logging.info('Started split dat script.')
    # file paths
    data_folder = os.path.join(os.getcwd(), 'data')
    source = os.path.join(data_folder, 'source', 'rma_adlib_tagged.dat')
    output_folder = os.path.join(data_folder, 'split')
    # ignore object number and alternate number
    ignore = ['I3']
    # list tags with value
    topics = list_topics_dat(source, ignore)
    logging.debug('Listed {} topics'.format(topics))
    # write object numbers and values to csv files
    split_dat_in_csv(topics, source, output_folder)
    logging.info('Done splitting.')


def list_topics_dat(source, ignore):
    topics = set([])
    # ignore seperators, object numbers and lines with no tag
    ignore_topics = ignore + ['**', 'IN', '  ']

    with io.open(source, 'r', encoding='utf-8-sig') as file:
        for line in file:
            topics.add(line[:2])

    for ignore_topic in ignore_topics:
        topics.discard(ignore_topic)
    return topics


def split_dat_in_csv(topics, source, out):
    file_count = 1
    sorted_topics = sorted(list(topics))

    for topic in sorted_topics:
        # create csv file
        file_name = '{}_{}.csv'.format(file_count, topic)
        split_file = os.path.join(out, file_name)
        file = open(split_file, 'w')
        writer = csv.writer(file)
        writer.writerow(['id', topic.encode('utf-8')])
        add_dat_values(topic, source, writer)
        file.close()
        file_count += 1


def add_dat_values(topic, source, writer):
    with io.open(source, 'r', encoding='utf-8-sig') as file:
        values = []
        tag = None
        record_number = None

        for line in file:
            line_start = line[:2]

            # record value
            if (line_start == topic):
                values.append(unicode.strip(line[3:]))
            # update current tag when line start is not empty
            if (not line_start == '  '):
                tag = line_start
            # merge newline value without tag with previous entry
            if (line_start == '  ' and tag == topic):
                merge = unicode.strip(line[3:])
                values[-1] = values[-1] + ' ' + merge
            # record object number
            if (line_start == 'IN'):
                record_number = unicode.strip(line[3:])
            # upon encountering ** write to csv
            if (line_start == '**'):
                # create new row for each value
                for value in values:
                    writer.writerow([
                        record_number.encode("utf-8"),
                        value.encode("utf-8")
                    ])
                # empty list of values and reset tag
                # (start over for following record)
                values = []
                tag = None
                record_number = None


if __name__ == "__main__":
    split_dat()
