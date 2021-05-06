#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[square ** 2 for square in i] for i in matrix]
    return new_matrix
