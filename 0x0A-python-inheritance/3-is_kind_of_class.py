#!/usr/bin/python3
"""check kind of a given class."""


def is_kind_of_class(obj, a_class):
    """Check kind of a class.
    args:
    obj: the object to be checked.
    a_class: the class
    Return: true if it is an instance or subclass false otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
