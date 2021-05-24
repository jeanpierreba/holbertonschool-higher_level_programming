#!/usr/bin/python3

""" This module adds of two integers """


def add_integer(a, b=98):
    """ Return the addition of a and b that must be integers or
    raise an Error depending on the case """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
