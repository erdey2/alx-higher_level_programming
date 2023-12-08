#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list2 = [[element ** 2 for element in row] for row in matrix]
    return list2
