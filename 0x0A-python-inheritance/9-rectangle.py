#!/usr/bin/python3
"""Implement a BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangel Implemented as a subclass of BaseGeometry."""
    def __init__(self, width, height):
        """initialize the rectangle calss.
        args:
            width: the width of the rectangle
            height: the height of the rectangle.
        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

        
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
