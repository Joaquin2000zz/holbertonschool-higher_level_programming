#!/usr/bin/python3
"""
11-student module
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
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key in dict(self.__dict__):
            if key in json:
                self.__dict__[key] = json[key]
