#!/usr/bin/python3
""" a square class """


class Square:
    """ this is a constructor (init) method
        Parameter:
        - __size: the size of the square.
        - __position: the position of the square
        Returns: None
        """
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 position integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 position integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 position integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ calculate and display the area """
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
                for i in range(self.__size):
                    for k in range(self.__position[0]):
                        print(" ", end="")
                    print("#" * (self.__size))
