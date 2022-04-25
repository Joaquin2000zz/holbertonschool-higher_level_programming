#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
module which shows request content
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    body = r.__dict__['_content'].decode()
    text = "Body response:\n\t- type: {}\n\t- content: {}".format(type(body),
                                                                  body)
    print(text)
