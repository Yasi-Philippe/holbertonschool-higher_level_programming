#!/usr/bin/python3
"""Script that creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """
    Function: load_from_json_file
    :param filename: Description
    """
    try:
        with open(filename, "r+", encoding="UTF-8") as my_file:
            my_obj = json.load(my_file)
    except FileNotFoundError:
        my_obj = []
    return my_obj
