#!/usr/bin/python3
"""
sendins a http request with the urllib library
and prints the response decoded
* urlencode parsed a dictionarty to do a post request
* to pass to request.urlopen(post)
"""
from sys import argv
from urllib import parse
from urllib import request

if __name__ == "__main__":
    try:
        toParse = {'email': argv[2]}
        data = parse.urlencode(toParse).encode()
        post = request.Request(argv[1], data=data)
        with request.urlopen(post) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        raise 
