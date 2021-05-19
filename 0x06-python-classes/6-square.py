#!/usr/bin/python3

"""Square class that defines attributes for a square object"""


class Square:
    """Square class that defines attributes for a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a value to the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set a value to the position attribute"""
        if not isinstance(value, tuple) of len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print in the stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self._position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(' '*self.__position[0], '#'*self.__size))
