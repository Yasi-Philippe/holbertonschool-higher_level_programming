#!/usr/bin/env python3
"""Script that converts CSV Data into JSON"""


import csv
import json


def convert_csv_to_json(filename):
    """Function that takes a csv file and turns it into json"""
    data = []
    try:
        with open(filename, "r", encoding="UTF-8") as my_file:
            data_row = csv.DictReader(my_file)
            for row in data_row:
                data.append(row)
        with open("data.json", "w", enconding="UTF-8") as json_file:
            json.dump(data, json_file)
    except FileNotFoundError:
        pass
