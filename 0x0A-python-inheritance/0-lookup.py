#!/usr/bin/python3

""" Module that returns a list of available attributes and methods """


def lookup(obj):
    """ Function that return the list of available attributes
    and methods """

    return dir(obj)
