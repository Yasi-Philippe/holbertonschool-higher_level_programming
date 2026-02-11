#!/usr/bin/env python3
"""Script that make serialization of data"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialization of data to a specific file"""
    with open(filename, "w", encoding="UTF-8") as my_file:
        json.dump(data, my_file)

def load_and_deserialize(filename):
    """Deserialization of data to a specific file"""
    with open(filename, "r", encoding="UTF-8") as my_file:
        return json.load(my_file)
