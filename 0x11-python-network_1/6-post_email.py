#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests
from sys import argv


if __name__ == "__main__":
    data = {"email": argv[2]}
    html = requests.post(argv[1], data)
    print("{}".format(html.text))
