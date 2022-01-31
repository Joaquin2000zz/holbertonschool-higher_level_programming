#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from function
    """
    return not issubclass(a_class, type(obj))
