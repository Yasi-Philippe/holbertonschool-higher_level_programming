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


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        Initialization function.
        Initializes width and height as private attributes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Are function"""
        return self.__width * self.__height

    def __str__(self):
        """Function that returns a standard string of the object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        Initialization function.
        Initializes size as private attribute
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Area of a square"""
        return super().area()

    def __str__(self):
        """Function that returns a standard string of the object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
