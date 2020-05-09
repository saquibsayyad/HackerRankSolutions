def repeatedString(s, n):
    times = s.count('a')
    repeat = n//len(s)
    extra = n%len(s)

    return repeat * times + s[0:extra].count('a')
    
print(repeatedString('a', 1000000000000))
