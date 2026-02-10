#!/usr/bin/python3
"""Script that defines a class that can retrieve a JSON format
representation of  stdent instance"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Function __init__
        :param self: Class Student
        :param first_name: First name of the student
        :param last_name: Last name of the student
        :param age: Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function to_json: Retrieves a dictionary representation of
        a student instance
        :param self: Class Student
        """
        return self.__dict__
