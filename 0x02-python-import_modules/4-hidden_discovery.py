#!/usr/bin/python3
import hidden_4
import sys
if __name__ == "__main__":
    secret_names = dir(hidden_4)
    for i in secret_names:
        if i[0:2] != "__":
            print("{}".format(i))
