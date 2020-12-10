#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) > i:
        print("{} argument:".format(len(argv) - 1))
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i = i + 1
    else:
        print("{} arguments.".format(len(argv) - 1))
