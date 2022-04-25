#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
module which shows request content
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    body = r.__dict__['_content'].decode()
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    
