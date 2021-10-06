#!/usr/bin/python3
"""
This module defines a class called Square
"""


class Square:
    """This class implements a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Intializes attributes"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of a square"""
        return self.__size**2

    def my_print(self):
        """Prints the square using # character"""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print(("\n"*self.__position[1])[:-1])
            print(((" "*self.__position[0] + "#"*self.__size + "\n")
                  * self.__size)[:-1])
