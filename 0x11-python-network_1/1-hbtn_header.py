#!/usr/bin/python3

from encodings import utf_8
from multiprocessing.connection import wait
import urllib.request
from sys import argv
import json

"""
sendins a http request with the urllib library 
and prints the X-Request-Id unique Hash of each Response
* acceding into the tuple of the list of tuples
* of the value of the dictionary with key '_headers'
* of the value of the dictionary with key 'headers'
* of the dictionary of an urlopen Response
"""


try:
    #url = 
    with urllib.request.urlopen(argv[1]) as Response:
        for Tuple in Response.__dict__['headers'].__dict__['_headers']:
            if (Tuple[0] == 'X-Request-Id'):
                print(Tuple[1])
except Exception as e:
    raise e
