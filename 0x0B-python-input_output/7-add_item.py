#!/usr/bin/python3
"""
7-add_item module
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    load = load_from_json_file("add_item.json")
    save_to_json_file(load + argv[1:], "add_item.json")
except Exception as a:
    save_to_json_file(argv[1:], "add_item.json")

