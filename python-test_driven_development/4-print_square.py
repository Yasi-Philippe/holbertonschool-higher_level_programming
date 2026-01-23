#!/usr/bin/python3
"""
Docstring for 4-print_square
"""


def print_square(size):
    """
    Docstring for matrix_divided
    :param size: Size of the square to print
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
