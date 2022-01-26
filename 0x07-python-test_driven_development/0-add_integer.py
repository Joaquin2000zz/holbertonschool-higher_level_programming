#!/usr/bin/python3
"""0-add_integer that adds 2 integers
add_integer function
@a: first number
@b: second number
Return: a + b
"""


def add_integer(a, b=98):
    """add_integer function which returns a + b
    @a: first number
    @b: second number
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
        elif type(a) is float:
            a = int(a)

    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
        elif type(b) is float:
            b = int(b)
    return a + b
