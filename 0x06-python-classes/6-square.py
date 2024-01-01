#!/usr/bin/python3
"""create a square class"""


class Square:
    """ A class representing a square.

    Attributes:
        size (int): the size of the square.
        position (int): the x and y coordinate of the square.
        """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square object.
        Args:
        size (int): the size of the square.
        position (int): the x and y coordinate of the square.
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute."""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) != int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self._position = value

    def area(self):
        """Calculate the area of the square."""
        return self._size * self._size

    def my_print(self):
        """Display square information."""
        if self.size == 0:
            print()
        else:
            print('\n'*self._position[1], end='')
            for i in range(self._size):
                print(' '*self._position[0], end='')
                print('#'*self._size)
