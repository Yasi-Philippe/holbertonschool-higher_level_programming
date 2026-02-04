#!/usr/bin/env python3
"""Extending methods in a list"""


class VerboseList(list):
    """Class that extends a normal list"""

    def append(self, value):
        super().append(value)
        print("Added [{}] to the list.".format(value))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, value):
        try:
            super().remove(value)
            print("Removed [{}] from the list.".format(value))
        except ValueError:
            super().remove(value)

    def pop(self, index=-1):
        try:
            value_removed = super().pop(index)
            print("Popped [{}] from the list.".format(value_removed))
            return value_removed
        except IndexError:
            value_removed = super().pop(index)