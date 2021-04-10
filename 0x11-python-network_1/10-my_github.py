#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests
from sys import argv


if __name__ == "__main__":
    html = requests.get("https://api.github.com/user",
                        auth=requests.auth.HTTPBasicAuth(argv[1], argv[2]))
    json = html.json()
    print("{}".format(json.get('id')))
