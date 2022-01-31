#!/usr/bin/python3
"""
8-base_geometry.py module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        init method
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        area method
        """
        return self.__size ** 2

    def __str__(self):
        """
        the str method
        """
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
