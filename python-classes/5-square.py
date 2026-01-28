#!/usr/bin/python3
"""Square"""


class Square:
    """Class that defines a square, notably it's size"""
    def __init__(self, size=0):
        """Function that initializes the class with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Function getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function setter of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Function that prints the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.__size * "#")
