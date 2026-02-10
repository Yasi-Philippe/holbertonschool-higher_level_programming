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

    def to_json(self, attrs=None):
        """
        Function to_json: Retrieves a dictionary representation of
        a student instance
        :param self: Class Student
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        """
        Function reload_from_json: Replaces all attributes of the
        Student instance
        :param self: Class Student
        :param json: Dictionary input
        """
        json["first_name"] = self.first_name
        json["last_name"] = self.last_name
        json["age"] = self.age
