#!/usr/bin/env python3
"""Abstract class and subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Asbract class animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass Dog that barks"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass Cat that meows"""

    def sound(self):
        return "Meow"
