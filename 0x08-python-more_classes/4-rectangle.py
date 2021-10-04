#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """This class implements a Rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns checked width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Checks the width value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns checked height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Checks the height value"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str = ""
        if self.__height < 0 or self.__width < 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str = str + "#"
                if j == self.__width - 1:
                    str = str + "\n"
                    break
        str = str[:len(str) - 1]
        return str

    def __repr__(self):
        rp = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return rp
