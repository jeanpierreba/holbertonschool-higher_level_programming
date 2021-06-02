#!/usr/bin/python3

""" Module that contains a class 'MyList' that inherits a list """


class MyList(list):
    """ Class List that inherits from a list """

    def print_sorted(self):
        print(sorted(self))
