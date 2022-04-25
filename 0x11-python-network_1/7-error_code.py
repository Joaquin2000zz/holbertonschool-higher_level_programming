#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
print index content or error code if x.status_code greater than 399
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if (r.status_code < 399):
       print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
