#!/usr/bin/python3

"""Square class that defines attributes for a square object"""


class Square:

    """Square class that defines attributes for a square object"""

    def __init__(self, size=0):
        """Initialize the data"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a value to the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
