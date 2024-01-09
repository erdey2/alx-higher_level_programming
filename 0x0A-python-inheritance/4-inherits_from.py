#!/usr/bin/python3
"""Checks for subclass."""


def inherits_from(obj, a_class):
    """Check for subclass of a given object.
    args:
    obj: the object to be checked.
    a_class: the class
    Return: true if it is a subclass or false otherwise
    """

    return isinstance(obj, a_class) and type(obj) != a_class
