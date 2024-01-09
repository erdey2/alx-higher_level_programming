#!/usr/bin/python3
"""Save object to file."""
import json


def save_to_json_file(my_obj, filename):
    """Write json to a file."""
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dump(my_obj, file)
