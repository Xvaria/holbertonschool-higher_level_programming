#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 97 and i <= 122:
            i = i - 32
        i = chr(i)
        print("{}".format(i), end="")
    print()
