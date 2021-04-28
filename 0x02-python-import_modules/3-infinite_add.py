#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    length = len(argv)
    for i in range(0, length):
        if i > 0:
            result += int(argv[i])
    print("{}".format(result))
