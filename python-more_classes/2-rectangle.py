#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Class defining a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of class. Height and width get initialized"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter function for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the perimeter"""
        return (2 * (self.__width + self.__height))
