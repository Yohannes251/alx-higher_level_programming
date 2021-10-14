#!/usr/bin/python3
"""
This module contains a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator(self, name, value, attr_type):
        """Validates passed arguments"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if attr_type == 1:
            if value <= 0:
                raise ValueError(f'{name} must be > 0')
        if attr_type == 2:
            if value < 0:
                raise ValueError(f'{name} must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value, 1)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value, 1)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value, 2)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value, 2)
        self.__y = value

    def area(self):
        """Returns area of the Rectange instance"""
        return self.width * self.height
