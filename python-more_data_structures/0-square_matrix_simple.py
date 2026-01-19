#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for i in range(0, len(new_matrix)):
        sub_matrix = new_matrix[i][:]
        for j in range(0, len(sub_matrix)):
            sub_matrix[j] *= sub_matrix[j]
        new_matrix[i] = sub_matrix
    return new_matrix
