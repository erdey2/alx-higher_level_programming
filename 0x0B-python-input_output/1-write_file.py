#!/usr/bin/python3
"""Write a string to text file."""


def write_file(filename="", text=""):
    """Write file to a given text file."""
    with(open(filename, 'w', encoding="utf-8")) as file:
        return file.write(text)
