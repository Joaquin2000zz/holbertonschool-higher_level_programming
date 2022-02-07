#!/usr/bin/python3
"""
module with unit test which test the Base module
"""
import unittest
from models.base import Base


class test_max_integer(unittest.TestCase):
    """
    test_max_integer function
    """
    def testBase(self):
        self.assertEqual(Base(), 1)
        self.assertEqual(Base(12), 12)

#>>> b1 = Base()
#>>> print(b1.id)
#1
#>>> b2 = Base()
#>>> print(b2.id)
#2
#>>> b3 = Base()
#>>> print(b3.id)
#3
#>>> b4 = Base(12)
#>>> print(b4.id)
#12
#>>> b5 = Base("holanda")
#>>> print(b5.id)
#no se xd

