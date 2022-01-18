#!/usr/bin/python3

"""square 4"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """setter method"""
        return self.__size

    @size.setter
    def size(self, n):
        """getter method"""
        if type(n) is not int:
            raise TypeError("size must be an integer")
        if int(n) < 0:
            raise ValueError("size must be >= 0")
        self.__size = n

    def area(self):
        """area method"""
        return self.__size * self.__size
