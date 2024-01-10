#!/usr/bin/python3
"""Print with separator module."""


def text_indentation(text):
    """
    Prints the text with delimiters on the same line, adding indentation after them.

    Args:
        text: The text to be printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for separator in "?:.":
        text = (separator + "\n\n").join(
                [line.strip(" ") for line in text.split(separator)])
    print(text, end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
