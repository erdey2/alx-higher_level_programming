#!/usr/bin/python3
"""Class to json module."""


class Student():
    """Student class."""
    def __init__(self, first_name, last_name, age):
        """initialize instance variables."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert object to json."""
        return self.__dict__.copy()
