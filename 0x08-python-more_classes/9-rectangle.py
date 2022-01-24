#!/usr/bin/python3

"""1-Rectangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init method"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter method"""
        return self.__height

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
                ret += str(self.print_symbol)
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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """square method"""
        return cls(size, size)
