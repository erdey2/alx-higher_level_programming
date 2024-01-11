#!/usr/bin/python3
"""set attribute module."""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it doesn't aready exist.
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = value
    else:
        if hasattr(obj, "set_attribute"):
            obj.set_attribute(name, value)
        else:
            raise TypeError("Cannot add attributes to this object")
        return obj
