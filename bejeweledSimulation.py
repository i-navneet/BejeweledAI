import random
#swaps two tiles
def swap(grid, source_x, source_y, dest_x, dest_y):
    temp = grid[source_x][source_y]
    grid[source_x][source_y] = grid[dest_x][dest_y]
    grid[dest_x][dest_y] = temp
#randomly intializes grid of tiles
def initGrid(grid, n, n_items):
    for i in range(n):
        for j in range(n):
            grid[i][j] = random.randint(0, n_items - 1)

#return points obtained after swapping and makes the tiles empty
def gridSolve(grid, n):
    for i in range(n):
        for j in range(n):
            temp = 0
            k = j
            while(k < n and grid[i][j] == grid[i][k] and grid[i][k] >= 0):
                temp = temp + 1
                k = k + 1
            if(temp >= 3):
                for l in range(j, j + temp):
                    grid[i][l] = -1
            if(temp == 3):
                return 10
            elif(temp == 4):
                return 20
            elif(temp == 5):
                return 30
    for i in range(n):
        for j in range(n):
            temp = 0
            k = j
            while(k < n and grid[j][i] == grid[k][i] and grid[k][i] >= 0):
                temp = temp + 1
                k = k + 1
            if(temp >= 3):
                for l in range(j, j + temp):
                    grid[l][i] = -1
            if(temp == 3):
                return 10
            elif(temp == 4):
                return 20
            elif(temp == 5):
                return 30
    return 0
#rearrange the grid to make all empty tiles come to top
def redrawGrid(grid, n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if grid[j][i] == -1:
                for k in range(j, 0, -1):
                    swap(grid, j, i, k, j)
#reinitlalizes empty tiles at the top
def addTiles(grid, n, n_items):
    for i in range(n):
        j = 0
        while(j < n and grid[j][i] == -1):
            grid[j][i] = random.randint(0, n_items - 1)
            j = j + 1

def oneMove(grid, n, n_items, source_x, source_y, dest_x, dest_y):
    totalScore = 0
    swap(grid, source_x, source_y, dest_x, dest_y)
    totalScore = totalScore + gridSolve(grid, n)
    while(True):
        redrawGrid(grid, n)
        addTiles(grid, n, n_items)
        temp = gridSolve(grid, n)
        if(temp == 0):
            break
        totalScore = totalScore + 2 * temp
    return totalScore 