#!/usr/bin/python3
"""Convert classes to json."""
import json


def class_to_json(obj):
    """Encode to json."""
    return json.dumps(obj.__dict__)
