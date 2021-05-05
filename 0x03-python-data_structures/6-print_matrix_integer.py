#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        separator = ""
        for j in i:
            print("{}{}".format(separator, j), end="")
            separator = " "
        print()
