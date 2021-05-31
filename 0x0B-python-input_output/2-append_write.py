#!/usr/bin/python3

""" Module to append text into a file """


def append_write(filename="", text=""):
    """ Function that appends the 'text' into the 'filename' """

    with open(filename, 'a') as my_file:
        return my_file.write(text)
