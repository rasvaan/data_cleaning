#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge CSV

Merge CSV files into one Adlib file that can be imported.
"""

__author__ = "Chris Dijkshoorn"
__version__ = "0.0.1"
__license__ = "MIT"


import os
import glob
import csv
import codecs


def merge_dat():
    print('Started merge csv script')
    # file paths
    os.chdir('data')
    source_folder = 'merge'
    merged_file = 'out/merged.dat'
    # get list of relvant files
    file_paths = list_file_paths(source_folder)
    # create dictionary for data
    data = csv_to_dict(file_paths)
    # create dat file
    write_dict_to_dat(data, merged_file)
    print('Finished merge script')


def list_file_paths(source_folder):
    print('Listing csv files in folder ' + source_folder)
    csv_files = []

    for file in glob.glob(source_folder + "/*.csv"):
        csv_files.append(file)
    return csv_files


def csv_to_dict(paths):
    print('Loading csv files into dictionary')
    dict = {"RM1" : {"IL":"artwork"}}

    for path in paths:
        file = codecs.open(path, 'r', 'utf-8')
        # add data to dict
        # for reader in readers:
        #     tag = reader[0]
        #     csv_reader = csv.reader(reader[1], delimiter=',', quotechar='"')
        #     for row in csv_reader:
        #         value = row[1]
        #         print(value)
        #         file.write(value)
    return dict


def write_dict_to_dat(dict, file):
    print('Writing dictionary to ' + file)
    file = codecs.open(file, 'w', 'utf-8')
    file.write(u'\ufeff')
    # write each value of each object to new dat
    # write_dict_to_dat(readers, file)
    # close files
    file.close()
    # close_readers = close_files(readers)



# def close_files(readers):
#     for reader in readers:
#         file = reader[1]
#         file.close()


if __name__ == "__main__":
    merge_dat()
