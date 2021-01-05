#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    c = []
    for i in range(list_length):
        try:
            c.append(my_list_1[a] / my_list_2[a])
        except TypeError:
            print("wrong type")
            c.append(0)
        except ZeroDivisionError:
            print("division by 0")
            c.append(0)
        except IndexError:
            print("out of range")
            c.append(0)
        finally:
            a += 1
    return(c)
