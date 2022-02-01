#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    function which opens files to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
