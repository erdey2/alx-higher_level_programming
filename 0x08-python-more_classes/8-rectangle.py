#!/usr/bin/python3
"""Rectangle Representation """


class Rectangle:
    """A Rectangle class with getters and setters.
    Attributes:
        width (int): the width of a rectangle.
        height (int): the height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the class with value.
        Args:
           width (int): the width of a rectangle.
           height (int): the height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the current value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a new value to the width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the current value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a new value to the height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangel."""
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """display the string representation of the object."""
        rect = ''
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rect += Rectangle.print_symbol * self.__width + '\n'

        return rect[:-1]

    def __repr__(self):
        """Return the string representation of an object."""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """It is called when an instance is removed."""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
