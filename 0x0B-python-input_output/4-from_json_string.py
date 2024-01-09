#!/usr/bin/python3
"""decode json module."""
import json


def from_json_string(my_str):
    """Convert json to python object."""
    return json.loads(my_str)
