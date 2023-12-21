#!/usr/bin/python3
""" a square class """


class Square:
    """ this is a constructor (init) method
        Parameter:
        - __size: the size of the square.
        """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    """ calculate and display the area """
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        row = self.__size
        if row == 0:
            print()
        for i in range(row):
            for j in range(row):
                print('#', end='')
            print()
