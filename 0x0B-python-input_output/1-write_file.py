#!/usr/bin/python3

""" This module will write text into a file """


def write_file(filename="", text=""):
    """ Function that write 'text' into 'filename' """

    with open(filename, 'w') as my_file:
        return my_file.write(text)
