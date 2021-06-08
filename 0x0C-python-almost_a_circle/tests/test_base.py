#!/usr/bin/python3

""" Unittest for Base class """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """ Class to test the Base class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_args(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)

    def test_numbers(self):
        base1 = Base(8)
        self.assertEqual(base1.id, 8)
        base2 = Base(-1)
        self.assertEqual(base2.id, -1)
        base3 = Base(12)
        self.assertEqual(base3.id, 12)
        base4 = Base(0)
        self.assertEqual(base4.id, 0)

    def test_instance(self):
        base1 = Base()
        self.assertTrue(isinstance(base1, Base))
        rectangle1 = Rectangle(1, 1)
        self.assertTrue(isinstance(rectangle1, Base))
        square1 = Square(1)
        self.assertTrue(isinstance(square1, Base))

    def test_to_json(self):
        list_none = None
        to_json = Base.to_json_string(list_none)
        self.assertEqual(to_json, "[]")
        self.assertEqual(type(to_json), str)

        list_empty = []
        to_json = Base.to_json_string(list_empty)
        self.assertEqual(to_json, "[]")
        self.assertEqual(type(to_json), str)

        dict_empty = [{}]
        to_json = Base.to_json_string(dict_empty)
        self.assertEqual(to_json, "[{}]")
        self.assertEqual(type(to_json), str)

        dict_ = [{'x': 4, 'y': 5}]
        to_json = Base.to_json_string(dict_)
        to_str = str(dict_)
        self.assertEqual(to_json, to_str.replace("'", "\""))
        self.assertEqual(type(to_json), str)

    def from_json_string(self):
        dict_ = [{'x': 3, 'y': 1}]
        to_json = Base.to_json_string(dict_)
        from_json = Base.from_json_string(to_json)
        self.assertEqual(dict_, from_json)
        self.assertEqual(type(to_json), str)
        self.assertEqual(type(from_json), list)

        list_empty = []
        to_json = Base.to_json_string(l1)
        from_json = Base.from_json_string(j1)
        self.assertEqual(from_json, [])
        self.assertEqual(type(to_json), str)
        self.assertEqual(type(from_json), list)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        str1 = str(r1)
        str2 = str(r2)
        self.assertEqual(str1, str2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(5, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        str1 = str(r1)
        str2 = str(r2)
        self.assertEqual(str1, str2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_square(self):
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        str1 = str(s1)
        str2 = str(s2)
        self.assertEqual(str1, str2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(2, 3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        str1 = str(s1)
        str2 = str(s2)
        self.assertEqual(str1, str2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

if __name__ == "__main__":
    unittest.main()
