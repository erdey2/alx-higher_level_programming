#!/usr/bin/python3
"""print square module."""


def print_square(size):
    """A function that print a square of #."""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
