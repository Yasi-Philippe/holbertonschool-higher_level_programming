#!/usr/bin/python3
"""Script that saves a object in a file in JSON format"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes a pyhton object into a file in JSON format"""
    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
