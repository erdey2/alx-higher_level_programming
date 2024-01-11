#!/usr/bin/python3
"""add attribute to object."""


def add_attribute(obj, name, value):
    """Implement add_attribute."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
setattr(obj, name, value)
