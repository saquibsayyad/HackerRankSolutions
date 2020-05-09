# Counting Valleys

def countingValleys(n, s):
    level = 0
    valleys = 0
    oldSeaLevel = 0
    for i in s:
        if ( i is 'D'):
            oldSeaLevel = level
            level = level - 1
        elif( i is 'U'):
            oldSeaLevel = level
            level = level + 1
        if(level is 0 and oldSeaLevel < 0):
            valleys = valleys + 1 
    return valleys

print(countingValleys(12, 'DUDUDU'))
