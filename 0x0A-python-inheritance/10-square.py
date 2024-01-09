#!/usr/bin/python3
"""Implement a square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Implementation."""
    def __init__(self, size):
        Rectangle.integer_validator(self, 'size', size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__size, self.__size))
