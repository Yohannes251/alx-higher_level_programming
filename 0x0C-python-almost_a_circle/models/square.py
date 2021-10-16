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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'size' in keys:
                self.size = kwargs['size']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y'] 

    def __str__(self):
        """Returns readable representation of object instance"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
