#!/usr/bin/python3
"""
10-student module
"""


class Student:
    """
    class Student that defines a student by
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        ret = {}
        if type(attrs) is list:
            for key in attrs:
                if key is not str:
                    return self.__dict__
                if key in self.__dict__:
                    ret[key] = self.__dict__[key]
        return ret
