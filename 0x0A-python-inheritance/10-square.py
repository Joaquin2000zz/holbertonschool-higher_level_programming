#!/usr/bin/python3
"""
8-base_geometry.py module
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator method
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        init method
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area method
        """
        return self.__width * self.__height

    def __str__(self):
        """
        the str method
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(BaseGeometry):
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
