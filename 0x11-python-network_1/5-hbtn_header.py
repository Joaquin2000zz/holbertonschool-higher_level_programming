#!/usr/bin/python3
"""
requests is the module and is used even to post data without encoding
module which shows x-request-id
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io')
    print(r.headers['x-request-id'])
