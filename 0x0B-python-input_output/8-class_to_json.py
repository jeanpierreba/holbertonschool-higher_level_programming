#!/usr/bin/python3

""" Module that returns the dictionary description with
simple data structure """


def class_to_json(obj):
    """ Function that creates a dict description of obj """
    return obj.__dict__
