def sum2list(l1: list, l2: list):
    r = []
    for n1 in l1:
        c = []
        r.append(c)
        for n2 in l2:
            c.append(n1*n2)
    return r

mcc1 = sum2list(1, [3, 5, 6])
mcc2 = sum2list([1, 2], [3, 5, 6])
print(mcc1)
print(mcc2)