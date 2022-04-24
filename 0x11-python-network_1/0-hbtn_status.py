#!/usr/bin/python3
"""
sending a http request with the urllib library and printing
* response type (bytes)
* raw information
* decoded information
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("UTF-8")))
