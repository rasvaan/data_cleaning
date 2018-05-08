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
import csv
from xml.dom.minidom import parse


def main():
    print('Started split script')
    # file paths (later: read from args)
    source_file = 'rijksmuseum_objects_adlib.xml'
    output_folder = '../out'
    # parse xml
    dom = parse_file(source_file)
    print('Parsed file {}'.format(source_file))
    # list elements with value
    topics = list_topics(dom)
    print('Listed {} topics'.format(topics))
    # write (id, value) to csv file
    split_in_csv(topics, dom, output_folder)


def parse_file(file_path):
    os.chdir('data')
    return parse(file_path)


def list_topics(dom):
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
        file.close()


if __name__ == "__main__":
    main()
