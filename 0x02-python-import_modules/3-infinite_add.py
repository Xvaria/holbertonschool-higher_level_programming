#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    i = 1
    if len(argv) > 1:
        while i < len(argv):
            a = int(argv[i]) + a
            i = i + 1
    print("{}".format(a))
