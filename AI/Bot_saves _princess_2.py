def nextMove(n,r,c,grid):
    pPos = getPrincesPosition(n,grid)
    mPos = [r,c]
    
    #while(pPos[0] != mPos[0] or pPos[1] != mPos[1]):
    grid[mPos[0]][mPos[1]] = '-'
    if(mPos[0] > pPos[0]):
       mPos[0] = mPos[0] - 1
       return 'UP'
    elif(mPos[0] < pPos[0]):
       mPos[0] = mPos[0] + 1
       return 'DOWN'
    elif(mPos[1] > pPos[1]):
        mPos[1] = mPos[1] - 1
        return 'LEFT'
    elif(mPos[1] < pPos[1]):
        mPos[1] = mPos[1] + 1
        return 'RIGHT'
    grid[mPos[0]][mPos[1]] = 'p'

def getPrincesPosition(n, grid):
    for i in range(0, n):
        for j in range(0, n):
            if(grid[i][j] is 'p'):
                return [i,j]


grid = [['-', '-', '-', '-', '-'],
        ['-', 'm', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', 'p', '-'],
        ['-', '-', '-', '-', '-']]
nextMove(5, 1, 1, grid)
print(grid)
nextMove(5, 1, 1, grid)
print(grid)
nextMove(5, 1, 1, grid)
print(grid)
nextMove(5, 1, 1, grid)
print(grid)
nextMove(5, 1, 1, grid)
print(grid)
nextMove(5, 1, 1, grid)
print(grid)
# - - -
# - m -
# p - -
