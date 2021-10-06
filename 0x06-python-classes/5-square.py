#!/usr/bin/python3
"""
This module defines a class called Square
"""


class Square:
    """This class implements a Square"""

    def __init__(self, size=0):
        """Intializes attributes"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of a square"""
        return self.__size**2

    def my_print(self):
        """Prints the square using # character"""
        if self.__size == 0:
            print("")
        else:
            print((("#"*self.__size + "\n") * self.__size)[:-1])
