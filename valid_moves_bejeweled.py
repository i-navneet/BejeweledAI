import random

def isValid(i,j,n):
    return i>=0 and j>=0 and i<n and j<n
    
def isSame(i,j,n,v,grid):
    return i>=0 and j>=0 and i<n and j<n and grid[i][j] == v

def valid_moves(grid,n):
    
    list_of_valid_moves = []
    
    
    
    for i in range(n):
        for j in range(n):
            
            original_value = grid[i][j]
            
            if(isValid(i,j-1,n)):
                
                previous_x_1 = i
                previous_y_1 = j-2
                
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    
                    previous_x_2 = i
                    previous_y_2 = j-3
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j-1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j-1))
                        
                        
                previous_x_1 = i-1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+1
                    previous_y_2 = j-1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j-1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j-1))
                            
                previous_x_1 = i-1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i-2
                    previous_y_2 = j-1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j-1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j-1))  
                            
                previous_x_1 = i+1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+2
                    previous_y_2 = j-1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j-1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j-1))                   
                        
            
            if(isValid(i,j+1,n)):
                
                previous_x_1 = i
                previous_y_1 = j+2
                
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    
                    previous_x_2 = i
                    previous_y_2 = j+3
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j+1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j+1))
                        
                        
                previous_x_1 = i-1
                previous_y_1 = j+1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+1
                    previous_y_2 = j+1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j+1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j+1))
                            
                previous_x_1 = i+1
                previous_y_1 = j+1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+2
                    previous_y_2 = j+1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j+1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j+1))  
                            
                previous_x_1 = i-1
                previous_y_1 = j+1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i-2
                    previous_y_2 = j+1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i,j+1) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i,j+1))
                            
            if(isValid(i-1,j,n)):
                previous_x_1 = i-2
                previous_y_1 = j
                
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    
                    previous_x_2 = i-3
                    previous_y_2 = j
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i-1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i-1,j))
                        
                        
                previous_x_1 = i-1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i-1
                    previous_y_2 = j+1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i-1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i-1,j))
                            
                previous_x_1 = i-1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i-1
                    previous_y_2 = j-2
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i-1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i-1,j))  
                            
                previous_x_1 = i-1
                previous_y_1 = j+1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i-1
                    previous_y_2 = j+2
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i-1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i-1,j))
                            
            if(isValid(i+1,j,n)):
                previous_x_1 = i+2
                previous_y_1 = j
                
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    
                    previous_x_2 = i+3
                    previous_y_2 = j
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i+1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i+1,j))
                        
                        
                previous_x_1 = i+1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+1
                    previous_y_2 = j+1
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i+1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i+1,j))
                            
                previous_x_1 = i+1
                previous_y_1 = j-1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+1
                    previous_y_2 = j-2
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i+1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i+1,j))  
                            
                previous_x_1 = i+1
                previous_y_1 = j+1
                        
                if(isSame(previous_x_1,previous_y_1,n,original_value,grid)):
                    previous_x_2 = i+1
                    previous_y_2 = j+2
                    
                    if(isSame(previous_x_2,previous_y_2,n,original_value,grid)):
                        
                        if (i,j,i+1,j) not in list_of_valid_moves:
                            list_of_valid_moves.append((i,j,i+1,j))                
                    
                    
            
    return list_of_valid_moves     
    
    
    
    
    
n = 4
no_of_type = 4

grid = [[3,3,1,1],[4,1,3,2],[1,2,3,3],[4,3,4,1]]

'''for i in range(n):
    for j in range(n):
        
        grid[i][j] = random.randint(1,4)'''
        
print(grid)  
l = valid_moves(grid,n)

print(l)

    