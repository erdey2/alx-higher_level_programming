#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """Read a file content."""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
    file.close()
