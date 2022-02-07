#!/usr/bin/python3
"""
module doc
"""
import json as js
import os


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
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if not list_objs:
                f.write([])
            else:
                objList = []
                for i in list_objs:
                    objList.append(i.__dict__)
                f.write(Base.to_json_string(objList))

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
        if os.path.isfile(cls.__name__ + ".json") is False:
            return []
        ret = []
        with open(cls.__name__ + ".json", 'r', encoding='utf-8') as f:
            for line in f:
                print("*********************************************")
                print(Base.from_json_string(line))
                print("*********************************************")
                ret.append(Base.from_json_string(line))
            return ret
