#!/usr/bin/python3
class Square:

    def checker(self, x, y):
        if y is tuple:
            if len(y) != 2:
                raise TypeError("the tuple length must be 2")
            if y[0] is not int or y[1] is not int:
                raise ValueError("size must be >= 0")
            if y[0] < 0 or y[1] < 0:
                raise ValueError("size must be >= 0")
        if type(x) is not int:
            raise TypeError("size must be an integer")
        elif x < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0, position=(0, 0)):
        self.checker(size, position)
        self.__position = position
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, n):
        self.checker(n, None)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, x):
        self.checker(None, x)

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            if self.__position[1] > 0:
                for i in range(0, self.__position[1]):
                    print()
            for i in range(0, self.__size):
                if self.__position[0] > 0:
                    for k in range(0, self.__position[0]):
                        print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
