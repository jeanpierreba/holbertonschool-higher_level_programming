#!/usr/bin/python3

""" Module with a class BaseGeometry that validate a value """


class BaseGeometry:
    """ Class with a public instance method that validate if
    value is integer """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
