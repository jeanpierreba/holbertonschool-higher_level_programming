#!/usr/bin/python3

""" Module that divides each element of a matrix of numbers by a number """


def matrix_divided(matrix, div):
    """ Returns a new matrix with the result of the division """

    if not matrix or \
       not isinstance(matrix, list) or \
       not all(isinstance(j, list) for j in matrix) or \
       not all(len(i) for i in matrix) or \
       not all([all(isinstance(x, (int, float)) for x in k) for k in matrix]):

        err_msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err_msg)

    len_rows = [len(l) for l in matrix]

    if len(set(len_rows)) != 1:
        err_msg = "Each row of the matrix must have the same size"
        raise TypeError(err_msg)

    if not isinstance(div, int) and not isinstance(div, float):
        err_msg = "div must be a number"
        raise TypeError(err_msg)

    if div == 0:
        err_msg = "division by zero"
        raise ZeroDivisionError(err_msg)

    result = [[round(i / div, 2) for i in j] for j in matrix]

    return result
