#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Split Adlib

Split exported Adlib files in multiple csv files, each containing ids and one
type of value. After the values are cleaned, they can be exported again.
"""

__author__ = "Chris Dijkshoorn"
__version__ = "0.0.1"
__license__ = "MIT"


import os
import io
import csv
from xml.dom.minidom import parse


def split_dat():
    print('Started split dat script')
    # file paths
    os.chdir('data')
    source = 'source/rijksmuseum_objects_adlib.dat'
    output_folder = 'split'
    # list tags with value
    topics = list_topics_dat(source)
    print('Listed {} topics'.format(topics))
    # write object numbers and values to csv files
    split_dat_in_csv(topics, source, output_folder)


def list_topics_dat(source):
    topics = set([])

    with io.open(source, 'r', encoding='utf-8') as file:
        # skip utf bomb
        file.read(1)
        for line in file:
            topics.add(line[:2])
    # remove seperator
    topics.remove('**')
    # remove lines with no tag
    topics.remove('  ')
    # remove object number
    topics.remove('IN')
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

        for line in file:
            tag = line[:2]
            # record object number
            if (tag == 'IN'):
                record_number = unicode.strip(line[3:])
            # record values topic
            if (tag == topic):
                values.append(unicode.strip(line[3:]))
            # upon encountering ** write to csv
            if (tag == '**'):
                # create new row for each value
                for value in values:
                    print(record_number, value)
                    writer.writerow([
                        record_number.encode("utf-8"),
                        value.encode("utf-8")
                    ])
                # empty list of values (start over for following record)
                values = []


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
