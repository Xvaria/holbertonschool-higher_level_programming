#!/usr/bin/python3
'Load, add, save'
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    l = load_from_json_file("add_item.json")
except FileNotFoundError:
    l = []

a = len(argv)
for i in range(1, a):
    l.append(argv[i])
save_to_json_file(l, "add_item.json")
