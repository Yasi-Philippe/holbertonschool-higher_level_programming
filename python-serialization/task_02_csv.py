#!/usr/bin/env python3
"""Script that converts CSV Data into JSON"""


import csv
import json


def convert_csv_to_json(filename):
    """Function that takes a csv file and turns it into json"""
    try:
        with open(filename, "r", encoding="UTF-8") as my_file:
            data = list(csv.DictReader(my_file))
            return json.dumps(data)
    except Exception:
        return {}
