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
        for item in self:
            if type(item) is not int:
                raise ValueError("Must be a list of integers")
        print(sorted(self))
