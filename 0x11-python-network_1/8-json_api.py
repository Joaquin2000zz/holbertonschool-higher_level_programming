#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
read a json taken from the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {'q': argv[1] if len(argv) > 1 else ""}
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data=data)
    try:
        Rdict = r.json()
    except Exception as e:
        print("Not a valid JSON")
    if len(Rdict) == 2:
        print("[{}] {}".format(Rdict['id'], Rdict['name']))
    else:
        print("No result")
