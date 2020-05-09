def displayPathtoPrincess(n,grid):
    pPos = getPrincesPosition(n,grid)
    mPos = [n//2, n//2]

    while(pPos[0] != mPos[0] and pPos[1] != mPos[1]):
        if(mPos[0] > pPos[0]):
            mPos[0] = mPos[0] - 1
            print('UP')
        elif(mPos[0] < pPos[0]):
            mPos[0] = mPos[0] + 1
            print('DOWN')

        if(mPos[1] > pPos[1]):
            mPos[1] = mPos[1] - 1
            print('LEFT')
        elif(mPos[1] < pPos[1]):
            mPos[1] = mPos[1] + 1
            print('RIGHT')

def getPrincesPosition(n, grid):
    lastIndex = n-1;
    if (grid[0][0] is 'p'):
        return [0,0]
    elif (grid[0][lastIndex] is 'p'):
        return [0,lastIndex]
    elif (grid[lastIndex][0] is 'p'):
        return [lastIndex,0]
    else:
        return [lastIndex,lastIndex]


grid = [['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', 'm', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'p']]
displayPathtoPrincess(5, grid)


# - - -
# - m -
# p - -
