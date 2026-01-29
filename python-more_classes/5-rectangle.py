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
        if self.__width == 0 or self.__height == 0:
            area = 0
        else:
            area = 2 * (self.__width + self.__height)
        return (area)

    def __str__(self):
        """Returns a rectangle"""
        my_str = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                my_str += self.__width * "#"
                if i != self.__height - 1:
                    my_str += "\n"
        return my_str

    def __repr__(self):
        """Returns the width and the height of a rectangle in a string"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints a farewell message when an instance is deleted"""
        print("Bye rectangle...")
