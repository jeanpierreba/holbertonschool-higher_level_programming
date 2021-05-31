#!/usr/bin/python3

""" Returns the JSON representation of an object """

import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of 'my_obj' """
    return json.dumps(my_obj)
