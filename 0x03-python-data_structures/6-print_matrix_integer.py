#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        if len(list) == 0:
            print('')
        i = 0
        for c in list:
            if i == len(list) - 1:
                print("{:d}".format(c))
            else:
                print("{:d}".format(c), end=' ')
            i += 1
