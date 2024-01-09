#!/usr/bin/python3
"""Append a text module."""


def append_write(filename="", text=""):
    """ Append a text to a given string.
    Args:
        filename: the name of the file.
        text: the string to be written.
    Returns:
        the number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
