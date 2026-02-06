#!/usr/bin/python3
"""
Shows whether an object is an instance of a
specified class or a precedent class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that shows whether if an object is
    an instance of a specified class
    Return: Boolean
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
