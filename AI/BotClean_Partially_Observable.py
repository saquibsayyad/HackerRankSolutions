def next_move(posr, posc, board):

    dirtLoc = findNearestDirt(posr, posc, board)

    if(dirtLoc is None):
        prevState = findPrevState()
        if (prevState is None):
            dirtLoc = findNextInvisibleSpace(posr, posc, board)
            saveState(dirtLoc[0], dirtLoc[1])
        else:
            dirtLoc = prevState

    if(dirtLoc[0] is posr and dirtLoc[1] is posc):
        print("CLEAN")
    elif(posc > dirtLoc[1]):
        posc = posc - 1
        print('LEFT')
    elif(posc < dirtLoc[1]):
        posc = posc + 1
        print('RIGHT')
    elif(posr > dirtLoc[0]):
       posc = posr - 1
       print('UP')
    elif(posr < dirtLoc[0]):
       posr = posr + 1
       print('DOWN')

def saveState(i, j):
        f = open("state", "w")
        f.write(str(i))
        f.write(str(j))
        f.close()

def findPrevState():
    try:
        f = open("state", "r")
        i = f.read(1)
        j = f.read(1)
        f.close()
        return [int(i), int(j)]
    except IOError:
        return None
    

def findNextInvisibleSpace(x, y, grid):
    for i in range(y, len(grid)):
        for j in range(x, len(grid)):
            if(grid[i][j] == 'o'):
                return [i,j]
        

def findNearestDirt(r, c, grid):
    n = len(grid)
    for k in range(1, n):
        for i in range(r-k, r+k+1):
            for j in range(c-k, c+k+1):
                if(i in range(0,n) and j in range(0,n) and grid[i][j] is 'd'):
                    return [i, j]



saveState(9,9)
print(findPrevState())

##grid = [['-', 'd', '-', '-', '-'],
##        ['b', 'd', '-', '-', '-'],
##        ['-', '-', '-', 'd', '-'],
##        ['-', '-', '-', 'd', '-'],
##        ['-', '-', 'd', '-', 'd']]
##
##
##next_move(1, 0, grid)

