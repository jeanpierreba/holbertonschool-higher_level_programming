#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        separator = ""
        for j in i:
            print("{:s}{:d}".format(separator, j), end="")
            separator = " "
        print()
