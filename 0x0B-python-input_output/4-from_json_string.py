#!/usr/bin/python3

""" Returns an object represented in JSON string """

import json


def from_json_string(my_str):
    """ Function to return an object from JSON string """
    return json.load(my_str)
