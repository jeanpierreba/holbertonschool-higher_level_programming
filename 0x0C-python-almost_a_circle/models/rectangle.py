#!/usr/bin/python3

""" Module that contains the Rectangle class that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Class that describes a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the data """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print the rectangle """
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """ Print dimensions of the rectangle """
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Update arguments of each attribute """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of dimensions of the Rectangle"""
        dictionary = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x, 'y': self.y}
        return dictionary
