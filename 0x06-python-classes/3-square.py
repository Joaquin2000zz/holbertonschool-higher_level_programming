#!/usr/bin/python3

"""square 3"""


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

    def area(self):
        """area method"""
        return self.__size * self.__size
