#!/usr/bin/python3

""" Module contains a function that return True if object is an instance of, or
if the object is an instance of a class that inherited from
the specified class, otherwise return False """


def is_kind_of_class(obj, a_class):
    """ Function that returns True if obj is an instance of a_class
    or if obj is a class that inherited from a_class otherwise False"""

    return isinstance(obj, a_class)
