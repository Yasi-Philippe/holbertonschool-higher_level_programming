#!/usr/bin/env python3
"""Extending methods in a list"""


class CountedIterator:
    """Clss that counts how many times the iter function has been used"""

    def __init__(self, data):
        self._data = iter(data)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        fetched_item = next(self._data)
        self.counter += 1
        return fetched_item
