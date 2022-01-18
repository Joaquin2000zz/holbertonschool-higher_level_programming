#!/usr/bin/python3

"""square 2"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """method init"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
