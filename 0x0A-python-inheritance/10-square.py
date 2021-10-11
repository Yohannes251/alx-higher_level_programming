#!/usr/bin/python3
"""
This module extends the Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square class"""
    def __init__(self, size):
        """Initializes attribute"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of the square"""
        return self.__size**2
