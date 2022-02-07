#!/usr/bin/python3
"""Module base"""
import json
import csv


class Base:
    """ base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization method"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ pass list to json representation"""

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object to file"""

        filename = f"{cls.__name__}.json"
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ json string to dict"""

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""

        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""

        filename = f"{cls.__name__}.json"
        list_ins = []

        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                list_ins.append(cls.create(**instances[i]))
            return list_ins
        except FileNotFoundError:
            return list_ins
