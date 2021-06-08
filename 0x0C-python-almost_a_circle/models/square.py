#!/usr/bin/python3

""" Module that contains the class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that describes a Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the data """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """ Print the dimensions of the square """
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        ))

    def update(self, *args, **kwargs):
        """ Update arguments of each attribute """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().update(id=value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of dimensions of the square """
        dictionary = {'id': self.id, 'size': self.size,
                      'x': self.x, 'y': self.y}
        return dictionary
