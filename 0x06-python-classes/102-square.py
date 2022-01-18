#!/usr/bin/python3

"""square 9. compare 2 squares"""


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
        if type(n) is not int or type(n) is not float:
            raise TypeError("size must be an integer")
        if int(n) < 0:
            raise ValueError("size must be >= 0")
        self.__size = n

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __le__(self, other):
        """__le__ method which compare method which other method"""
        return self.__size <= other.__size

    def __lt__(self, other):
        """__lt__ method which compare method which other method"""
        return self.__size < other.__size

    def __ge__(self, other):
        """__ge__ method which compare method which other method"""
        return self.__size >= other.__size

    def __gt__(self, other):
        """__gt__ method which compare method which other method"""
        return self.__size > other.__size

    def __eq__(self, other):
        """__eq__ method which compare method which other method"""
        return self.__size == other.__size
