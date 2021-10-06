#!/usr/bin/python3
"""
This module defines a class called Square
"""


class Square:
    """This class implements a Square"""

    def __init__(self, size=0):
        """Intializes attributes"""

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size**2
