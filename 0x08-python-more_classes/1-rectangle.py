#!/usr/bin/python3

"""1-Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """init method"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter method"""
        return self.width

    @width.setter
    def width(self, width):
        """setter method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(height):
        """getter method"""
        return self.height

    @height.setter
    def height(self, height):
        """setter method"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
