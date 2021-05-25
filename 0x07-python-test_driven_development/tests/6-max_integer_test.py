#!/usr/bin/python3

""" Unittest for the max_integer module """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestCases for the max_integer function """

    def regular_test(self):
        """ Test with a normal list of ints """
        list_l = [2, 6, 3, 5, 1]
        result = max_integer(list_l)
        self.assertEqual(result, 6)

    def str_int_test(self):
        """ Test with strings and ints as arguments """
        list_l = ["String", "Holbie", 9]
        self.assertRaises(TypeError, max_integer, 1)

    def empty_test(self):
        """ Test when a list is empty """
        list_l = []
        result = max_integer(list_l)
        self.assertEqual(result, None)

    def negative_test(self):
        """ Test when the list have negative numbers """
        list_l = [-2, 3, 5, -8]
        result = max_integer(list_l)
        self.assertEqual(result, 5)

    def float_test(self):
        """ Test when the list have float numbers """
        list_l = [2.5, 3, 4.5, 7.2]
        result = max_integer(list_l)
        self.assertEqual(result, 7.2)
    
    def test_not_list(self):
        """ Test with a parameter that's not a list """
        self.assertRaises(TypeError, max_integer, 3)

    def str_test(self):
        """ Test with a list of only strings """
        list_l = ["Hello", "Holberton"]
        result = max_integer(list_l)
        self.assertEqual(result, "Hello")

    def none_test(self):
        """ Test a list with none as parameter """
        self.assertRaises(TypeError, max_integer, None)

if __name__ == "__main__":
    unittest.main()
