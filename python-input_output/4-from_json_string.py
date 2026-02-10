#!/usr/bin/python3
"""Script that returns a python object representing JSON format"""


import json


def from_json_string(my_str):
    """Function that returns an object taking JSON string as input"""
    return json.loads(my_str)
