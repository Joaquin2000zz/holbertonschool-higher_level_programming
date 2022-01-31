#!/usr/bin/python3
"""
101-add_attribute
"""


def add_attribute(a, b, c):
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(a, b, c)
