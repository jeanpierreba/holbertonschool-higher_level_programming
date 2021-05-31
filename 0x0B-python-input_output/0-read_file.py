#!/usr/bin/python3

""" This module will read the 'namefile'
and print it in the standard output """


def read_file(filename=""):
    """ Function to read and print the file """

    with open(filename) as my_file:
        read_file = my_file.read()
        print(read_file, end="")
