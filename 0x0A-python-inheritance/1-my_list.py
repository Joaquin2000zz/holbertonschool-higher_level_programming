#!/usr/bin/python3
"""
module with print_sorted
"""


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
