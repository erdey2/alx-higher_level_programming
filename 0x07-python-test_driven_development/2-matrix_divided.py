#!/usr/bin/python3
"""test matrix divide module."""


def matrix_divided(matrix, div):
    """matrix division."""
    bug = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(bug)
    if not isinstance(matrix, list):
        raise TypeError(bug)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(bug)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(bug)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(bug)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
