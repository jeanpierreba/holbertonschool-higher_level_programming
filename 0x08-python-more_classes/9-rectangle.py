#!/usr/bin/python3

""" Module with definition of the class Rectangle """


class Rectangle:
    """ Class Rectangle defined with width, height, area, perimeter
    __str__, __repr__, number of instances, print symbol and staticmethod """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        perimeter_r = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter_r = 0
        return perimeter_r

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ''
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle_str += str(self.print_symbol)
                rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
