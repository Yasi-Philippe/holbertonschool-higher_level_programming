#!/usr/bin/python3
"""
Docstring for 3-text_indentation
"""


def text_indentation(text):
    """
    Docstring for text_indentation
    :param text: Input text to print
    """

    if not text:
        raise TypeError("text must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    for character in text:
        if character not in (".", "?", ":"):
            print(character, end="")
        else:
            print("{}\n".format(character))
