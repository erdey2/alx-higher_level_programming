#!/usr/bin/python3
"""base class module."""
import json


class Base(object):
    """Base class implementation."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            result = []
        else:
            result = json.dumps(list_dictionaries)
        return result
