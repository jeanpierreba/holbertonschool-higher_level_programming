#!/usr/bin/python3

""" Module that contains a class that inherits from the last class
and have a defined methond to search the area """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from rectangle and have the area method """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()
