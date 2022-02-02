#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a string
    """
    flag = 0
    newContent = ""
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            newContent += line
            if search_string in line:
                newContent += new_string
        f.seek(0)
        f.write(newContent)
