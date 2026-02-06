#!/usr/bin/python3
"""Script that lists all the attributes and methods of a class sorted"""


class MyList(list):
    """Class that sorts a list"""

    def print_sorted(self):
        """Function that returns a list of all the methods of an object sorted"""
        print(sorted(self))
