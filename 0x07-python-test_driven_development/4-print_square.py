#!/usr/bin/python3
"""
4-print_square module
contains print_square function
it's provided an int which is the size of the square
"""


def print_square(size):

    """
    print_square function
    void function
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for height in range(0, size):
        for width in range(0, size):
            print('#', end='')
        print()
