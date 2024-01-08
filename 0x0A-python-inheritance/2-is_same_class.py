#!/usr/bin/python
"""check object for equality."""

def is_same_class(obj, a_class):
    """return true if an object is an instance otherwise fasle."""
    if isinstance(obj, a_class):
        return True
    return False
