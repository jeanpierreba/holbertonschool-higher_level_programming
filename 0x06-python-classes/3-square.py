#!/usr/bin/python3

"""Square class that defines attributes for a square object"""


class Square:
    """Square class that defines attributes for a square object"""
    def __init__(self, size=0):
        """Initialize the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
