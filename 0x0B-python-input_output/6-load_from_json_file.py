#!/usr/bin/python3
"""read json module."""
import json


def load_from_json_file(filename):
    """Read from json file."""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
