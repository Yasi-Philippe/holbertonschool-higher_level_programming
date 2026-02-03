#!/usr/bin/python3
"""
Class of base geometry
"""


class BaseGeometry:
    """Base Gemotry Class"""

    def area(self):
        """Area function that returns an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that checks whether a specified value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
