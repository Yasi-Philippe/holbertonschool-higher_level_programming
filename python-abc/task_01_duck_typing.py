#!/usr/bin/env python3
"""Abstract class of Shape and its subclasses"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Asbract class shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Subclass Circle"""

    def __init__(self, radius=0):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """Subclass Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height


def shape_info(cls):
    print(cls.area())
    print(cls.perimeter())
