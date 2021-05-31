#!/usr/bin/python3

""" Module to add all arguments to a python list
and then save them to a file """

from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

name_file = 'add_item.json'

if path.isfile(name_file):
    arguments = load_from_json_file(name_file)
else:
    arguments = []

for i in range(1, len(argv)):
    arguments.append(argv[i])

save_to_json_file(arguments, name_file)
