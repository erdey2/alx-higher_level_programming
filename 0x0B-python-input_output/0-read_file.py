#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """Read a file content."""
    with(open(filename, 'r')) as file:
        print(file.read(), end="")
    file.close()
