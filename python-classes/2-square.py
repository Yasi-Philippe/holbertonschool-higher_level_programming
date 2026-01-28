#!/usr/bin/python3
"""Square"""


class Square:
    """Class that defines a square, notably it's size"""
    def __init__(self, size=0):
        """Function that initializes the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
