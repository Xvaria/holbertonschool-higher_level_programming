#!/usr/bin/python3
def uniq_add(my_list=[]):
    b = 0
    a = 0
    for i in my_list:
        a = a + i
        if my_list[b:].count(i) > 1:
            a = a - i
        b = b + 1
    return a
