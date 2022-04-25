#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
print index content or error code in error case
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    text = r.text
    if "Error" in text:
        print("Error code: {}".format(text.split(' ')[1]))
