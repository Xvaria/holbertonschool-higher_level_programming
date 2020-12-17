def only_diff_elements(set_1, set_2):
    a = []
    for i in set_1:
        a.append(i)
        for j in set_2:
            if j == i:
                a.remove(i)
    for k in set_2:
        a.append(k)
        for l in set_1:
            if k == l:
                a.remove(k)
    return a
