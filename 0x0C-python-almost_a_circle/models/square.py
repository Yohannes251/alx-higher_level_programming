#!/usr/bin/python3
"""
This module contains Square class that extends Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes"""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        super().validator("width", value, 1)
        self._size = value
        

    def __str__(self):
        """Returns readable representation of object instance"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
