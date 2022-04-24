#!/usr/bin/python3
"""
sending a http request with the urllib library and printing
* decoded information
* in case of error, prints the error code from x.__dict__['code'] value
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode())
    except Exception as e:
        print("Error code: {}".format(e.__dict__['code']))
