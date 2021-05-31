#!/usr/bin/python3

""" Module to save an object into a file """

import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file, using a JSON representation """

    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
