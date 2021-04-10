#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests
from sys import argv


if __name__ == "__main__":
    html = requests.get(argv[1])
    if(html.status_code < 400):
        print("{}".format(html.text))
    else:
        print("Error code: {}".format(html.status_code))
