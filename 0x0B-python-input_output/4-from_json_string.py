#!/usr/bin/python3
"""
4-from_json_string module
"""
import json
from io import StringIO as io


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
