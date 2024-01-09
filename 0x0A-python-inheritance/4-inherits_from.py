#!/usr/bin/python3
"""Checks for subclass."""


def inherits_from(obj, a_class):
    """Check for subclass of a given object.
    args:
    obj: the object to be checked.
    a_class: the class
    Return: true if it is a subclass or false otherwise
    """

    return issubclass(obj, a_class)
