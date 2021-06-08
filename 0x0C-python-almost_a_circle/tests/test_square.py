#!/usr/bin/python3

""" Unittest for Square class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_SquareS(unittest.TestCase):
    """ Class to test the Square class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def argume_test(self):
        square1 = Square(4)
        self.assertEqual(square1.id, 1)
        square2 = Square(7, 1, 2)
        self.assertEqual(square2.height, 7)
        self.assertEqual(square2.width, 7)
        self.assertEqual(square2.x, 1)
        self.assertEqual(square2.y, 2)
        self.assertEqual(square2.id, 2)

    def test_representation(self):
        square1 = Square(6, 1, 2, 3)
        self.assertEqual(str(square1), "[Square] (3) 1/2 - 6")

    def test_arguments(self):
        with self.assertRaises(TypeError) as error_msg:
            square1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                error_msg.exception))

    def update_test(self):
        square = Square(5)
        square.update(2)
        self.assertEqual(square.id, 2)
        square.update(x=3)
        self.assertEqual(square.x, 3)
        square.update(size=4, id=12, y=3)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.y, 3)
        square.update()
        self.assertEqual(square.size, 4)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.y, 3)

    def size_test(self):
        square1 = Square(3)
        self.assertEqual(square1.size, 3)
        square2 = Square(3, 2, 4, 2)
        self.assertEqual(square2.size, 3)

    def wrong_values(self):
        with self.assertRaises(TypeError) as error_msg:
            square1 = Square("Holberton", 2)
        self.assertEqual("width must be an integer", str(error_msg.exception))
        with self.assertRaises(TypeError) as error_msg:
            square3 = Square(1, 2, "Hey :D", 3)
        self.assertEqual("x must be an integer", str(error_msg.exception))
        with self.assertRaises(TypeError) as error_msg:
            square4 = Square(1, 2, 2, "World")
        self.assertEqual("y must be an integer", str(error_msg.exception))
        with self.assertRaises(ValueError) as error_msg:
            square5 = Square(0, 2)
        self.assertEqual("width must be > 0", str(error_msg.exception))

if __name__ == "__main__":
    unittest.main()
