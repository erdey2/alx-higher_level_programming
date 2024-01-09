#!/usr/bin/python3
"""Convert classes to json."""


def class_to_json(obj):
    """Encode to json."""
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()

    return dic
