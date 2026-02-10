#!/usr/bin/python3
"""Script that converts a class into JSON format"""


def class_to_json(obj):
    """
    Function class_to_json
    
    :param obj: Class to pass into JSON
    """
    return obj.__dict__
