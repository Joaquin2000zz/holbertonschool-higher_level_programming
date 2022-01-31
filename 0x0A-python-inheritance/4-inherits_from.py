#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from function
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
