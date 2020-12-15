#!/usr/bin/python3
def no_c(my_string):
    a = 0
    s = my_string
    for i in my_string:
        if i == 'C' or i == 'c':
            s = s[:a] + s[a + 1:]
            a = a - 1
        a = a + 1
    return s
