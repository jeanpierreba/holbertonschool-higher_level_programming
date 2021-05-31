#!/usr/bin/python3

""" Module that creates an object from a JSON file """

import json


def load_from_json_file(filename):
    """ Function that creates a object from 'filename' """

    with open(filename) as my_file:
        return json.load(my_file)
