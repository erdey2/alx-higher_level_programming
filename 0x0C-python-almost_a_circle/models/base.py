#!/usr/bin/python3
"""base class module."""
import json
import os.path


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

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file."""
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r', encoding="utf-8") as file:
            list_str = file.read()
        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for i in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[i]))
        return list_ins
