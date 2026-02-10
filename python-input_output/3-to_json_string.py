#!/usr/bin/python3
"""Script that returns the JSON representation of a string"""


import json


def to_json_string(my_obj):
    """Function that returns a dictionary
    representing the data in JSON format"""
    return json.dumps(my_obj)
