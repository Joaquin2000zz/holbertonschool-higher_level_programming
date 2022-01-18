#!/usr/bin/python3

"""square 5"""


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
        """getter method"""
        return self.__size

    @size.setter
    def size(self, n):
        """setter method"""
        if type(n) is not int:
            raise TypeError("size must be an integer")
        if int(n) < 0:
            raise ValueError("size must be >= 0")
        self.__size = n

    def area(self):
        """area method"""
        return self.__size * self.__size

    def my_print(self):
        """print method"""
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
