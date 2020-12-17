#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = my_list[:]
    b = 0
    for i in a:
        if i == 2:
            a[b] = replace
        b = b + 1
    return a
