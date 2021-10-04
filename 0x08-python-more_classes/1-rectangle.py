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
