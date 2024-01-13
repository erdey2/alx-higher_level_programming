#!/usr/bin/python3
"""Rectangle class implementation."""
from models.base import Base


class Rectangle(Base):
    """Rectangle a subclass of the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize instance variables."""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height


        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        if not isinstance(y, int):
            raise TypeError('y must be an integer)')
        if y < 0:
            raise ValueError('y must be  >= 0')
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y):
        self.__y = y
