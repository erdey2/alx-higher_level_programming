#!/usr/bin/python3
"""check object for equality."""


def is_same_class(obj, a_class):
    """check object instance.
    args:
        obj: the object to be checked
        a_class: class of the object

        Return: true if an object is an instance otherwise fasle.
        """

    if type(obj) is a_class:
        return True
    return False
