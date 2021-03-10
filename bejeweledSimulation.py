import valid_moves_bejeweled
import numpy as np
#swaps two tiles
def swap(grid, source_x, source_y, dest_x, dest_y):
    temp = grid[source_x][source_y]
    grid[source_x][source_y] = grid[dest_x][dest_y]
    grid[dest_x][dest_y] = temp
#randomly intializes grid of tiles
def initGrid(grid, n, n_items):
    while(gridSolve(grid, n) != 0):
        for i in range(n):
            for j in range(n):
                grid[i][j] = np.random.randint(0, n_items)

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
            elif(temp >= 5):
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
            elif(temp >= 5):
                return 30
    return 0
#rearrange the grid to make all empty tiles come to top
def redrawGrid(grid, n):
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j] == -1:
                for k in range(i, 0, -1):
                    swap(grid, k, j, k - 1, j)
#reinitlalizes empty tiles at the top
def addTiles(grid, n, n_items):
    for i in range(n):
        j = 0
        while(j < n and grid[j][i] == -1):
            grid[j][i] = np.random.randint(0, n_items)
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

#gets simulated score for a swap between (source_x, source_y) and (dest_x, dest_y) without adding new tiles (please provide a deep copy of original grid for the function
def simulatedMove(grid, n, n_items, source_x, source_y, dest_x, dest_y):
    totalScore = 0
    swap(grid, source_x, source_y, dest_x, dest_y)
    totalScore = totalScore + gridSolve(grid, n)
    while(True):
        redrawGrid(grid, n)
        temp = gridSolve(grid, n)
        if(temp == 0):
            break
        totalScore = totalScore + 2 * temp
    return totalScore

def randomPathAgent(grid, n, n_items, n_moves):
    totalScore = 0
    solvableGrid = 0
    for j in range(1000):
        initGrid(grid, n, n_items)
        if(len(valid_moves_bejeweled.valid_moves(grid, n)) == 0):
            continue
        for i in range(n_moves):
            temp = valid_moves_bejeweled.valid_moves(grid, n)
            if(len(temp) == 0):
                break
            temp1 = temp[np.random.randint(0, len(temp))]
            del temp
            totalScore = totalScore + oneMove(grid, n, n_items, temp1[0], temp1[1], temp1[2], temp1[3])
        solvableGrid = solvableGrid + 1
    print(solvableGrid)
    return totalScore / solvableGrid
def randomPath(grid, n, n_items, n_moves):
    if(len(valid_moves_bejeweled.valid_moves(grid, n)) == 0):
        return 0
    totalScore = 0
    for i in range(n_moves):
        temp = valid_moves_bejeweled.valid_moves(grid, n)
        if(len(temp) == 0):
            break
        temp1 = temp[np.random.randint(0, len(temp))]
        del temp
        totalScore = totalScore + oneMove(grid, n, n_items, temp1[0], temp1[1], temp1[2], temp1[3])
    return totalScore
grid = np.zeros((8, 8))
print(randomPathAgent(grid, 8, 2, 20))

