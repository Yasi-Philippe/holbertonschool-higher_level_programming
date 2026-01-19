#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        ax = 0
        ay = 0
    elif len(tuple_a) == 1:
        ax = tuple_a[0]
        ay = 0
    else:
        ax = tuple_a[0]
        ay = tuple_a[1]
    if len(tuple_b) == 0:
        bx = 0
        by = 0
    elif len(tuple_b) == 1:
        bx = tuple_b[0]
        by = 0
    else:
        bx = tuple_b[0]
        by = tuple_b[1]
    new_tuple = (ax + bx, ay + by)
    return new_tuple
