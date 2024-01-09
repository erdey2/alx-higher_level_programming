#!/usr/bin/python3
"""Implement a Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangel Implemented as a subclass of BaseGeometry."""
    def __init__(self, width, height):
        """Initialize the rectangle calss.
        args:
            width: the width of the rectangle
            height: the height of the rectangle.
        """
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
