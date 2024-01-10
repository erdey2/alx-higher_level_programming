#!/usr/bin/python3
"""display name module."""


def say_my_name(first_name, last_name=""):
    """Display a given name."""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    msg = f'My name is {first_name} {last_name}'
    print(msg)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
