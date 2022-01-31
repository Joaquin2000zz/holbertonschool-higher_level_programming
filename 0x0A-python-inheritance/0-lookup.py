#!/usr/bin/python3
"""
module with lookup
"""


def lookup(obj):
    """
    returns a list of available attributes and methods of an object
    """
    return dir(obj)
