#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
module which shows x-request-id
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['x-request-id'])
