#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    data = {'q': q}
    html = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        json = html.json()
        if json:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
        except:
            print("Not a valid JSON")
