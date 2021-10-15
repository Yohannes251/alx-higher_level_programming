#!/usr/bin/python3
"""
This module contains Square class that extends Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns readable representation of object instance"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
