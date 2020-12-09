#!/usr/bin/python3
c = 122
for i in range(2, 28):
    if i % 2 != 0:
        c = c - 32
    print("{}".format(chr(c)), end="")
    if c >= 65 and c <= 90:
        c = c + 32
    c = c - 1
