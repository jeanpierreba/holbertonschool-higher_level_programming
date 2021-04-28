#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv)
    if arguments == 1:
        print("{} arguments.".format(arguments - 1))
    elif arguments == 2:
        print("{} argument:".format(arguments - 1))
    else:
        print("{} arguments:".format(arguments - 1))
    for i in range(0, arguments):
        if i > 0:
            print("{}: {}".format(i, argv[i]))
