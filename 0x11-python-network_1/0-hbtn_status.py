#!/usr/bin/python3
"""
sending a http request with the urllib library and printing
* response type (bytes)
* raw information
* decoded information
"""
from encodings import utf_8
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
    print(f'\t- utf8 content: {html.decode("UTF-8")}')
