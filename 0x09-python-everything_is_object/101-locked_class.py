#!/usr/bin/python3
"""
advanced
"""


class MyClass(object):
    """
    function which set the only name permited to create an instance class
    """

    __slots__ = ['first_name']

    def __init__(self, first_name):
        """
        init
        """
        pass
