#!/usr/bin/python3
"""Script that prints the content of a file"""


def read_file(filename=""):
    """Function that reads and prints the content of a file"""
    with open(filename, "r", encoding="UTF-8") as my_file:
        print(my_file.read())
