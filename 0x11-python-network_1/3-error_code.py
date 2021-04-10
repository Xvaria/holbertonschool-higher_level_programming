#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import urllib.request
from sys import argv


try:
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))
except urllib.error.HTTPError as error:
    print("Error code: {}".format(error.code))
