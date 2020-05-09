def rotLeft(a, d):
    n = len(a)
    b = []
    for i in range(d, d + n):
        if( i >= len(a)):
            b.append(a[i-n])
        else:
            b.append(a[i])
    return b

print(rotLeft([1, 2, 3, 4, 5], 4))
