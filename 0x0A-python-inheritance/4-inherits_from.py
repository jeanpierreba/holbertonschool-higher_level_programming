#!/usr/bin/python3

""" Module that seeks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class. """


def inherits_from(obj, a_class):
    """ Function that returns True if obj is an instance of a class that
    inherited from a_class """

    return False if type(obj) == a_class else isinstance(obj, a_class)
