#!/usr/bin/python3
"""Define an integer addition function. """


def add_integer(a, b=98):
    """ Adds two integers.
    Args:
    a: the first integer.
    b: the second integer, default 98.
    Raises:
        TypeError: if a, b are not int, float.
    Returns:
        The sum of the two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
