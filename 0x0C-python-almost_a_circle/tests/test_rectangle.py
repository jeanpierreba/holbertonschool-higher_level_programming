#!/usr/bin/python3

""" Unittest for Rectangle class """

import unittest
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """ Class to test the Rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.id, 1)
        rectangle2 = Rectangle(2, 3)
        self.assertEqual(rectangle2.id, 2)
        rectangle3 = Rectangle(3, 4)
        self.assertEqual(rectangle3.id, 3)
        rectangle4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle4.id, 12)
        rectangle5 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(rectangle5.id, 34)

    def test_dimensions(self):
        rectangle1 = Rectangle(8, 5)
        self.assertEqual(rectangle1.width, 8)
        self.assertEqual(rectangle1.height, 5)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)
        rectangle2 = Rectangle(3, 7, 1, 3)
        self.assertEqual(rectangle2.width, 3)
        self.assertEqual(rectangle2.height, 7)
        self.assertEqual(rectangle2.x, 1)
        self.assertEqual(rectangle2.y, 3)

    def test_arguments(self):
        with self.assertRaises(TypeError) as error_msg:
            rectangle1 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                error_msg.exception))
        two_arguments = s = ("__init__() missing 2 required positional" +
                             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as error_msg:
            rectangle2 = Rectangle()
        self.assertEqual(two_arguments, str(error_msg.exception))

    def test_inheritance(self):
        rectangle1 = Rectangle(9, 3)
        self.assertTrue(isinstance(rectangle1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def wrong_values(self):
        with self.assertRaises(TypeError) as error_msg:
            rectangle1 = Rectangle("Holberton", 2)
        self.assertEqual("width must be an integer", str(error_msg.exception))
        with self.assertRaises(TypeError) as error_msg:
            rectangle2 = Rectangle(2, "Hello!")
        self.assertEqual("height must be an integer", str(error_msg.exception))
        with self.assertRaises(TypeError) as error_msg:
            rectangle3 = Rectangle(1, 2, "Hey :D", 3)
        self.assertEqual("x must be an integer", str(error_msg.exception))
        with self.assertRaises(TypeError) as error_msg:
            rectangle4 = Rectangle(1, 2, 2, "World")
        self.assertEqual("y must be an integer", str(error_msg.exception))
        with self.assertRaises(ValueError) as error_msg:
            rectangle5 = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(error_msg.exception))

    def test_area(self):
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.area(), 15)
        r2 = Rectangle(10, 5)
        self.assertEqual(r2.area(), 50)
        r3 = Rectangle(2, 1, 0, 0, 12)
        self.assertEqual(r3.area(), 2)

        with self.assertRaises(TypeError) as error_msg:
            rectangle1 = Rectangle(3, 2)
            rectangle1.area("Betty")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                error_msg.exception))

    def update_test(self):
        rectangle1 = Rectangle(5, 5, 5, 5)
        rectangle1.update(60)
        self.assertEqual(rectangle1.id, 60)
        rectangle1.update(60, 4)
        self.assertEqual(rectangle1.width, 4)
        rectangle1.update(60, 4, 7)
        self.assertEqual(rectangle1.height, 7)
        rectangle1.update(60, 4, 7, 1)
        self.assertEqual(rectangle1.x, 1)
        rectangle1.update(60, 4, 7, 1, 2)
        self.assertEqual(rectangle1.y, 2)
        rectangle1.update()
        self.assertEqual(str(rectangle1), "[Rectangle] (60) 1/2 - 4/7")

if __name__ == "__main__":
    unittest.main()
