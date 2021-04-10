#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests
from sys import argv

if __name__ == "__main__":
    html = requests.get(argv[1])
    header = html.headers.get("X-Request-Id")
    print("{}".format(header))
