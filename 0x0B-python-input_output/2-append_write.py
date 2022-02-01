#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file
    returns the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
