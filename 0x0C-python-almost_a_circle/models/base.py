#!/usr/bin/python3
"""
module doc
"""
import json as js


class Base:
    """
    Base class doc
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor doc
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return js.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
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

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        return js.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        return cls.update(cls, None, dictionary)

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
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
