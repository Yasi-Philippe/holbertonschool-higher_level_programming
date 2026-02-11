#!/usr/bin/python3
"""Script that constructs a Psacal Triangle"""


def pascal_triangle(n):
    """
    Function Pascal_triangle: Constructs a Pascal Triangle of size n
    Returns a list of lists containing each line of the triangle
    :param n: Size of triangle
    """
    if n <= 0:
        return []
    whole_list = [[1]]
    list_pre = [1]
    for i in range(n):
        new_list = [1]
        for j in range(i):
            new_list.append(list_pre[j] + list_pre[j + 1])
        new_list.append(1)
        whole_list.append(new_list)
        list_pre = new_list
    return whole_list
