#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
post an email taken from argv[2]
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data = {'email': argv[2]})
    print(r.text)
