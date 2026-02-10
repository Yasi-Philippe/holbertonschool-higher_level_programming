#!/usr/bin/python3
"""Script that prints a string to a text file"""


def write_file(filename="", text=""):
    """Function that writes a stirng to a text file and
    returns the characters written"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
