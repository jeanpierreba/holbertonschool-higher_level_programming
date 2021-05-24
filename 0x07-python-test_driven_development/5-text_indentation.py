#!/usr/bin/python3

""" Module to add a new line when after some characters """


def text_indentation(text):
    """ Print the text with two new lines every time
    it find '.' ':' or '?' characters """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in ".:?":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])

    print("{}".format(text), end="")
