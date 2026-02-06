#!/usr/bin/python3
"""Shows whether an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Function that shows whether if an object is
    an instance of a specified class
    Return: Boolean
    """
    if type(obj) is a_class:
        return True
    else:
        return False
