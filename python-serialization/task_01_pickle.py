#!/usr/bin/env python3
"""Script that make serialization of data using pickle"""


import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Function that displays the attributes of the object"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Function that serializes in pickle the object"""
        try:
            with open(filename, "wb") as my_file:
                pickle.dump(self, my_file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Function that deserializes an instance"""
        try:
            with open(filename, "rb") as my_file:
                return pickle.load(my_file)
        except Exception:
            return None
