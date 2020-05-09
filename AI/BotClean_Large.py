def next_move(posr, posc, dimx, dimy, board):

    dirtLoc = findNearestDirt(posr, posc, dimx, dimy, board)

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

def findNearestDirt(r, c, x, y, grid):
    n = max(x, y)
    for k in range(1, n):
        for i in range(r-k, r+k+1):
            for j in range(c-k, c+k+1):
                if(i in range(0,x) and j in range(0,y) and grid[i][j] is 'd'):
                    return [i, j]
            


grid = [['-', 'd', '-', '-', '-'],
        ['b', 'd', '-', '-', '-'],
        ['-', '-', '-', 'd', '-'],
        ['-', '-', '-', 'd', '-'],
        ['-', '-', 'd', '-', 'd']]


next_move(1, 0, 5, 5, grid)

