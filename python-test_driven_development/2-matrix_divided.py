#!/usr/bin/python3
"""
Docstring for 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Docstring for matrix_divided
    :param matrix: Matrix as input
    :param div: Divisor input
    """

    err_msg = ("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        part_matrix = []
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(err_msg)
            part_matrix.append(round(j / div, 2))
        new_matrix.append(part_matrix)
    return new_matrix
