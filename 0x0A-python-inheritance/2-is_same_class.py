#!/usr/bin/python3

""" This module contain a function that returns True if an object is
exactly an instance of the specified class otherwise False """


def is_same_class(obj, a_class):
    """ Function that returns True if obj is a_class otherwise False """

    return True if type(obj) is a_class else False
