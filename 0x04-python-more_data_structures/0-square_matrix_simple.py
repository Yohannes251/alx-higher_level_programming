#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    mat_new = matrix[:]
    for i in range(0, len(mat_new)):
        mat_new[i] = (list(map(lambda x: x**2, mat_new[i])))
        i = i + 1
    return mat_new
