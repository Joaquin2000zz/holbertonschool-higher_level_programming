#!/usr/bin/python3
"""
find_peak module
"""


def find_peak(list_of_integers):
    """
    find_peak
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
