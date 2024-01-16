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
        return self.size * self.size

    def display(self):
        """display square with #."""
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()

    def __str__(self):
        """override the str method."""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    def update(self, *args, **kwargs):
        """update using variable number of arguments."""
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == 'id':
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == 'size':
                    self.size = j

                elif i == 'x':
                    self.x = j

                elif i == 'y':
                    self.y = j
