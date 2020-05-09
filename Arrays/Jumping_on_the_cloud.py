def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while(i < len(c)):
        if((i+2) < len(c) and c[i+2] is not 1):
            jumps = jumps + 1
            i = i + 1
        elif((i+1) < len(c) and c[i+1] is not 1):
            jumps = jumps + 1
        else:
            break
        i = i + 1
    return jumps

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]));
