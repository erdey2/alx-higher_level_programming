#!/usr/bin/python3
"""Write a string to text file."""


def write_file(filename="", text=""):
    """Write file to a given text file.
    Args:
        filename: the name of the file to be written in.
        text: the string to be write.
    Returns:
        the number of characters written.
    """
    with(open(filename, 'w', encoding="utf-8")) as file:
        return file.write(text)
