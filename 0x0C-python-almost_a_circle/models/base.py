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
        return str(result)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = '{}.json'.format(cls.__name__)
        items = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                items.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(items)

        with open(file_name, "w") as file:
            file.write(lists)
