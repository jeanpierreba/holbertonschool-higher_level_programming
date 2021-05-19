#!/usr/bin/python3
class Square:
    """Square class that defines attributes for a square object"""
    def __init__(self, size=0):
        """Initialize the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
