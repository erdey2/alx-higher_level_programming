#!/usr/bin/python3
"""Rectangle Representation """


class Rectangle:
    """A Rectangle class with getters and setters.
    Attributes:
        width (int): the width of a rectangle.
        height (int): the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes the class with value.
        Args:
           width (int): the width of a rectangle.
           height (int): the height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get the current value of width."""
        return self.width

    @width.setter
    def width(self, value):
        """Set a new value to the width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """Get the current value of height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set a new value to the height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """Compute the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Compute the perimeter of the rectangel."""
        if (self._width == 0 or self._height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self._width + self._height)
        return perimeter

    def __str__(self):
        """display the string representation of the object."""
        rect = ''
        if self._width > 0 and self._height > 0:
            for i in range(self._height):
                rect += '#' * self._width + '\n'

        return rect[:-1]
