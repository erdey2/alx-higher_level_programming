#!/usr/bin/python3
"""Rectangle class implementation."""
from models.base import Base
import json


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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be an integer)')
        if y < 0:
            raise ValueError('y must be  >= 0')
        self.__y = y

    def area(self):
        """calculate area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """display rectanle using #."""
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """override the print object method."""
        result = f"""
        [{Rectangle.__name__}]({self.id})
        {self.x}/{self.y} - {self.width}/{self.height}
        """
        return result

    def update(self, *args, **kwargs):
        """update using args."""
        count = 0
        for arg in args:
            count += 1
        if count == 1:
            self.id = arg
        elif count == 2:
            self.__width = arg
        elif count == 3:
            self.__height = arg
        elif count == 4:
            self.__x = arg
        elif count == 5:
            self.__y = arg

        if kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():

                if i == 'id':
                    if j is not None:
                        self.id = j
                if i == 'width':
                    if j is not None:
                        self.__width = j

                if i == 'height':
                    if j is not None:
                        self.__height = j
                if i == 'x':
                    if j is not None:
                        self.__x = j
                if i == 'y':
                    if j is not None:
                        self.__y = j

    def to_dictionary(self):
        """convert rectangle instance to dictionary."""
        dictionary = {}
        for i in ['id', 'width', 'height', 'x', 'y']:
            dictionary[i] = getattr(self, i)
        return dictionary
