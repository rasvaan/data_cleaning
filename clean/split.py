#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Split Adlib

Split exported Adlib files in multiple csv files, each containing ids and one
type of value. After the values are cleaned, they can be exported again.
"""

__author__ = "Chris Dijkshoorn"
__version__ = "0.0.2"
__license__ = "MIT"


import os
import io
import csv
from xml.dom.minidom import parse


def split_dat():
    print('Started split dat script.')
    # file paths
    data_folder = os.path.join(os.getcwd(), 'data')
    source = os.path.join(data_folder, 'source', 'rijksmuseum_objects_adlib.dat')
    output_folder = os.path.join(data_folder, 'split')
    # ignore object number and alternate number
    ignore = ['IN', 'I3']
    # list tags with value
    topics = list_topics_dat(source, ignore)
    print('Listed {} topics'.format(topics))
    # write object numbers and values to csv files
    split_dat_in_csv(topics, source, output_folder)
    print('Done splitting.')


def list_topics_dat(source, ignore):
    topics = set([])
    # ignore seperators and lines with no tag
    ignore_topics = ignore + ['**', '  ']

    with io.open(source, 'r', encoding='utf-8') as file:
        # skip utf bomb
        file.read(1)
        for line in file:
            topics.add(line[:2])

    for ignore_topic in ignore_topics:
        topics.discard(ignore_topic)
    return topics


def split_dat_in_csv(topics, source, out):
    for topic in topics:
        # create csv file
        split_file = out + '/' + topic + '.csv'
        file = open(split_file, 'w')
        writer = csv.writer(file)
        writer.writerow(['id', topic.encode("utf-8")])
        add_dat_values(topic, source, writer)
        file.close()


def add_dat_values(topic, source, writer):
    with io.open(source, 'r', encoding='utf-8') as file:
        # skip utf bomb
        file.read(1)
        values = []
        tag = None
        ignore = False

        for line in file:
            line_start = line[:2]

            # record value
            if (line_start == topic):
                values.append(unicode.strip(line[3:]))
                tag = line_start
            # merge newline value without tag with previous entry
            if (line_start == '  ' and tag == topic):
                print(line)
                print('tag: {} topic: {}'.format(tag, topic))
                print('record: {} values: {}'.format(record_number, values))
                merge = unicode.strip(line[3:])
                values[-1] = values[-1] + ' ' + merge
            # record object number
            if (line_start == 'IN'):
                record_number = unicode.strip(line[3:])
            # record if alternate number (ignore in this case)
            if (line_start == 'i3'):
                ignore = True
            # upon encountering ** write to csv
            if (line_start == '**'):
                if (not ignore):
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


def split_xml():
    print('Started split XML script')
    # file paths
    os.chdir('data')
    source_file = 'source/rijksmuseum_objects_adlib.xml'
    output_folder = 'split'
    # parse xml
    dom = parse(file_path)
    print('Parsed file {}'.format(source_file))
    # list elements with value
    topics = list_topics_xml(dom)
    print('Listed {} topics'.format(topics))
    # write (id, value) to csv file
    split_in_csv(topics, dom, output_folder)


def list_topics_xml(dom):
    # Extract all XML elements that have relevant values (e.g. title)
    topics = set([])
    records = dom.getElementsByTagName('recordList').item(0).childNodes

    for record in records:
        for element in record.childNodes:
            if (element.nodeType == element.ELEMENT_NODE):
                topics.add(element.nodeName)
    return topics


def split_in_csv(topics, dom, out):
    for topic in topics:
        split_file = out + '/' + topic + '.csv'
        file = open(split_file, "wb")
        writer = csv.writer(file)
        writer.writerow(['id', topic])
        add_values_topic(topic, dom, writer)
        file.close()


def add_values_topic(topic, dom, writer):
    records = dom.getElementsByTagName('recordList').item(0).childNodes

    # for record in records:
    #     # get record identifier
    #     id = get_identifier(record)
    #     # get all nodes concerning the topic
    #     record.getElementsByTagName(topic)
    #     # write identifier and values to csv
    #     for value in values:
    #        writer.writerow([id, value])


if __name__ == "__main__":
    split_dat()
