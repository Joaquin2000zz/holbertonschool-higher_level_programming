#!/usr/bin/python3
"""
8-class_to_json module
"""
import json


def class_to_json(obj):
    """
    function that returns the dictionary description
    """
    return json.dumps(obj.__dict__)
