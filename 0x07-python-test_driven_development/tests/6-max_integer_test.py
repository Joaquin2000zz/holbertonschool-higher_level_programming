#!/usr/bin/python3
"""
module with unit test which test the max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """
    test_max_integer function
    """
    def testMax(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1]), -1)
