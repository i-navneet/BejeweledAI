import bejeweledSimulation
import valid_moves_bejeweled
import MCTS
import random_agent_for_choosing_move
import time
import numpy as np

def checkForOutput():
    RandomAgentScore = []
    SimulatedRandomAgentScore = []
    RandomAgentTime = []
    SimulatedRandomAgentTime = []
    MCTSAgentScore = []
    MCTSAgentTime =[]
    SimulatedMCTSScore = []
    SimulatedMCTSTime = []
    grid = np.zeros((8,8))
    for j in range(1000):
        initGrid(grid, 8, 6)
        if(len(valid_moves_bejeweled.valid_moves(grid, n)) == 0):
            continue
        initTime = time.time()
        RandomAgentScore.append(bejeweledSimulation.randomPath(deepcopy(grid), 8, 6, 40))
        RandomAgentTime.append(time.time() - initTime)
        initTime = time.time()
        SimulatedRandomAgentScore.append(bejeweledSimulation.simulatedRandomPath(deepcopy(grid), 8, 6, 40))
        SimulatedRandomAgentTime.append(time.time() - initTime)
        initTime = time.time()
        MCTSAgentScore.append(MCTS.MCTSAgent(deepcopy(grid), 8, 6, 40, 2, 10))
        MCTSAgentTime.append(time.time() - initTime)
        initTime = time.time()
        SimulatedMCTSScore.append(MCTS.simulatedMCTSAgent(deepcopy(grid), 8, 6, 40, 2, 10))
        SimulatedAgentTime.append(time.time() - initTime)
    print('Random Agent Score :' , RandomAgentScore)
    print('Simulated Agent Score :', SimulatedRandomAgentScore)
    print('MCTS Agent Score :', MCTSAgentScore)
    print('Simulated MCTS Score :', SimulatedMCTSScore)
    print('Random Agent Time :', RandomAgentTime)
    print('Simulated Agent Time :', SimulatedRandomAgentTime)
    print('MCTS Agent Time :', MCTSAgentTime)
    print('Simulated MCTS Time :', SimulatedMCTSTime)

        