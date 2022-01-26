#!/usr/bin/python3
"""
3-say_my_name module
contain the say_my_name function which prints a message
@first_name @last_name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function. without return
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
