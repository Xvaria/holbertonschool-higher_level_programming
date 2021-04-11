#!/usr/bin/python3
'''list 10 commits of the repository rails by the user rails'''
import requests
from sys import argv


if __name__ == "__main__":
    html = requests.get("https://api.github.com/repos/{}/{}/commits".
                        format(argv[2], argv[1]))
    json = html.json()
    try:
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'), json[i].get('commit').
                                  get('author').get('name')))
    except:
        pass
