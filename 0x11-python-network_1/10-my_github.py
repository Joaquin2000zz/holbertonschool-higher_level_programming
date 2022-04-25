#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
get to github with your user and token
read a json taken from the response and display github id
"""
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) == 3):
        r = requests.get('https://api.github.com/user',
                         auth=(argv[1], argv[2]))
    try:
        print(r.json()['id'])
    except Exception as e:
        print(None)
