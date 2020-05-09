def rotLeft(a, d):
    for i in range(0, d):
        first = a[0]
        a.pop(0)
        a.append(first)
    return a

print(rotLeft([1, 2, 3, 4, 5], 4))
