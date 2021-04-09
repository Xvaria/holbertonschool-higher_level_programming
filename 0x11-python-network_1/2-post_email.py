#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import urllib.request
from sys import argv

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))
