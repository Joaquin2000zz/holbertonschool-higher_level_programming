#!/usr/bin/python3

"""1-Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """init method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif int(width) < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif int(height) < 0:
            raise ValueError("height must be >= 0")
        else:
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
        if int(width) < 0:
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
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def perimeter(self):
        """perimeter method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """str method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ret = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ret += "#"
            if i is not self.__height - 1:
                ret += "\n"
        return ret

    def __repr__(self):
        """repr method"""
        return (type(self).__name__ + "(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """del method"""
        print("Bye rectangle...")
