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
    Rdict = r.json()
    if len(Rdict) == 2:
        try:
            print("[{}] {}".format(Rdict['id'], Rdict['name']))
        except Exception as e:
            print("Not a valid JSON")
    else:
        print("No result")
