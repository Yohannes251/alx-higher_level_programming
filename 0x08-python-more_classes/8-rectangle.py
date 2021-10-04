#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """This class implements a Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        stri = ""
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        if self.__height < 0 or self.__width < 0:
            return stri
        for i in range(self.__height):
            for j in range(self.__width):
                stri = stri + str(self.print_symbol)
                if j == self.__width - 1:
                    stri = stri + "\n"
                    break
        stri = stri[:len(stri) - 1]
        return stri

    def __repr__(self):
        """Returns a string representation of the object"""
        rp = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return rp

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""

        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1
