#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, n):
        if type(n) is not int:
            raise TypeError("size must be an integer")
        if int(n) < 0:
            raise ValueError("size must be >= 0")
        self.__size = n

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
