#!/usr/bin/python3
"""Implement a BaseGeometry class."""


class BaseGeometry(object):
    """An empty BaseGeometry class """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        self._value = value


class Rectangle(BaseGeometry):
    """Rectangel Implemented as a subclass of BaseGeometry."""
    def __init__(self, width, height):
        """init - initialize the rectangle calss.
        args:
            width: the width of the rectangle
            height: the height of the rectangle.
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, height)
