#!/usr/bin/python3
"""Square class module."""
from models.rectangle import Rectangle



class Square(Rectangle):
    """Square class implementation."""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the objects."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def area(self):
        """calculate area of the square."""
        return self.__size * self.__size

    def display(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()

    def __str__(self):
        """override the str method."""
        return f'[{Square.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}'
    
        
