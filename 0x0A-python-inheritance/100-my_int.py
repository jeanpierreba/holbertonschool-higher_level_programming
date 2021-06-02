#!/usr/bin/python3

""" Class that inherits from an int """


class MyInt(int):
    """ Function that have == and != inverted """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
