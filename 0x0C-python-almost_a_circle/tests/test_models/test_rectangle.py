#!/usr/bin/python3
"""
module with unit test which test the Base module
"""
import unittest
from models.rectangle import Rectangle


class test_max_integer(unittest.TestCase):
    """
    test_max_integer function
    """

    def testRectangleiId(self):
        """
        test Rectamgle Id
        """
        self.assertEqual(Rectangle(10, 2, 0, 0, 12), 1)

    def testChangeValuesRectangle(self)
        """
        test chanege Rectangle values
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertRaises(ValueError, r1.update(89, 2, 3, -10), )

#>>> r1 = Rectangle(10, 2)
#    print(r1.id)
#1
#>>> r2 = Rectangle(2, 10)
#>>> print(r2.id)
#2
#>>> r3 = Rectangle(10, 2, 0, 0, 12)
#>>> print(r3.id)
#3
#>>> r4 = Rectangle("hola", "como", "estas", "todo", "bien")
#no se xd
#>>> from models.rectangle import Rectangle
#>>> Rectangle(10, "2")
#traceback (most recent call last):
#        ...
#TypeError: height must be an integer
#>>> r = Rectangle(10, 2)
#>>> r.width = -10
#traceback (most recent call last):
#        ...
#ValueError: width must be > 0
#>>> r = Rectangle(10, 2)
#>>> r.x = {}
#traceback (most recent call last):
#        ...
#ValueError: x must be > 0
#>>> Rectangle(10, 2, 3, -1)
#traceback (most recent call last):
#        ...
#ValueError: y must be > 0
>>> from models.rectangle import Rectangle
>>> r1 = Rectangle(10, 10, 10, 10)
>>> r1.update(89)
>>> print(r1)
[Rectangle] (89) 10/10 - 10/10
>>> r1 = Rectangle(10, 10, 10, 10)
>>> r1.update(89, 2)
>>> print(r1)
[Rectangle] (89) 10/10 - 2/10
>>> r1 = Rectangle(10, 10, 10, 10)
>>> r1.update(89, 2, 3)
>>> print(r1)
[Rectangle] (89) 10/10 - 2/3
>>> r1 = Rectangle(10, 10, 10, 10)
>>> r1.update(89, 2, 3, 4)
>>> print(r1)
[Rectangle] (89) 3/10 - 2/3
>>> r1 = Rectangle(10, 10, 10, 10)
>>> r1.update(89, 2, 3, 4, 5)
>>> print(r1)
[Rectangle] (89) 4/5 - 2/3
