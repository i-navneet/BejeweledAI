import random
import bejeweledSimulation
def random_agent_for_choosing_move(valid_moves_list,grid,n,n_items):
    
    moves_and_simulated_score = {}
    simulated_total_score = []
    
    for i in range(len(valid_moves_list)):  #calculating simulatedMove
        
        source_x,source_y,dest_x,dest_y = valid_moves_list[i]
        
        simulated_score = bejeweledSimulation.simulatedMove(grid,n,n_items,source_x,source_y,dest_x,dest_y)
        
        simulated_total_score.append(simulated_score)
    
    n = len(simulated_total_score)    
    for i in range(1,n):  #presum
        
        simulated_total_score[i] = simulated_total_score[i] + simulated_total_score[i-1]
        
    random_number = random.randint(simulated_total_score[0],simulated_total_score[n-1])
    
        
    index = 0
    while(index<n):  #upperBound
        if(simulated_total_score[index] >= random_number):
            break
            
        index = index + 1
        
    result_source_x,result_source_y,result_dest_x,result_dest_y = valid_moves_list[index]
    
    return result_source_x,result_source_y,result_dest_x,result_dest_y,simulated_total_score[index]
    
    
    
    
    
