#!/usr/bin/python3
class Square:
    """ Definition of the Square class
    Private instance attribute: size
    Instantiation with size (no type/value verification) """

    def __init__(self, size):
        """ Initializing the data """
        self.__size = size
