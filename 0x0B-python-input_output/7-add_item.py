#!/usr/bin/python3
"""
7-add_item module
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


save_to_json_file(argv[1:], "add_item.json")
