#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    stored_key = None
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            stored_key = key
    return stored_key
