import numpy as np
import bejeweledSimulation
import valid_moves_bejeweled
import time
from copy import deepcopy

class node:
    def __init__(self, grid, parent = None, children = None, x = 0, ni = 0, action = None, cost = 0, level = 0):
        self.parent = parent
        self.children = children
        self.grid = grid
        self.action = action
        self.cost = cost
        self.level = level
        self.ni = ni
        self.x = x
        self.isLeaf = True
    def backpropagate(self, score):
        temp = self
        while(temp != None):
            temp.ni = temp.ni + 1
            temp.x = temp.x + score
            temp = temp.parent
    def expansion(self, n, n_items):
        temp = []
        for i in valid_moves_bejeweled.valid_moves(self.grid, n):
            new_grid = deepcopy(self.grid)
            a = bejeweledSimulation.oneMove(new_grid, n, n_items, i[0], i[1], i[2], i[3])
            temp.append(node(new_grid, self, None, 0, 0, i, a + self.cost, self.level + 1))
        self.children = temp
        self.isLeaf = False
        return temp
    def delete(self):
        if self.children == None:
            del self
            return
        for i in self.children:
            i.delete()
        del self
    
def rollout(grid, n, n_moves, n_items):
    return bejeweledSimulation.randomPath(grid, n, n_items, n_moves)

def simulatedRollout(grid, n, n_moves, n_items):
    return bejeweledSimulation.simulatedRandomPath(grid, n, n_items, n_moves)

def MCTS(grid, n, n_items, n_moves, C, resource):
    root = node(deepcopy(grid))
    root.expansion(n, n_items)
    current = root
    initTime = time.time()
    while(time.time() - initTime <= resource):
        current = root
        while(not (current.isLeaf)):
            if(len(current.children) == 0):
                break
            max_ucb1 = 0
            for i in current.children:
                if current.ni == 0 or i.ni == 0:
                    current = i
                    break
                if i.x / i.ni + 2 * np.sqrt(np.log(current.ni) / i.ni) > max_ucb1:
                    max_ucb1 = i.x / i.ni + 1 * np.sqrt(C * np.log(current.ni) / i.ni)
                    current = i
        if(not current.isLeaf and len(current.children) == 0):
            current.backpropagate(current.cost)
            continue
        if(current.ni == 0):
            backval = rollout(current.grid, n, n_moves - current.level, n_items)
        else:
            if(len(current.expansion(n, n_items)) == 0):
                breakval = 0
            else:
                current = current.children[0]
                backval = rollout(current.grid, n, n_moves - current.level, n_items)
        current.backpropagate(backval + current.cost)
    max_avg = 0
    result = (-1, -1, -1, -1)
    for i in root.children:
        if i.ni == 0:
            result = i.action
            break
        if i.x / i.ni > max_avg:
            max_ucb = max_avg
            result = i.action
    #root.delete()
    return result

def MCTSAgent(grid, n, n_items, n_moves, C, resource):
    totalScore = 0
    for j in range(n_moves, 0, -1):
        action = MCTS(grid, n, n_items, j, C, resource)
        if(action == (-1, -1, -1, -1)):
            break
        totalScore = totalScore + bejeweledSimulation.oneMove(grid, n, n_items, action[0], action[1], action[2], action[3])
    return totalScore

def simulatedMCTS(grid, n, n_items, n_moves, C, resource):
    root = node(deepcopy(grid))
    root.expansion(n, n_items)
    current = root
    initTime = time.time()
    while(time.time() - initTime <= resource):
        current = root
        while(not (current.isLeaf)):
            if(len(current.children) == 0):
                break
            max_ucb1 = 0
            for i in current.children:
                if current.ni == 0 or i.ni == 0:
                    current = i
                    break
                if i.x / i.ni + 2 * np.sqrt(np.log(current.ni) / i.ni) > max_ucb1:
                    max_ucb1 = i.x / i.ni + 1 * np.sqrt(C * np.log(current.ni) / i.ni)
                    current = i
        if(not current.isLeaf and len(current.children) == 0):
            current.backpropagate(current.cost)
            continue
        if(current.ni == 0):
            backval = simulatedRollout(current.grid, n, n_moves - current.level, n_items)
        else:
            if(len(current.expansion(n, n_items)) == 0):
                breakval = 0
            else:
                current = current.children[0]
                backval = simulatedRollout(current.grid, n, n_moves - current.level, n_items)
        current.backpropagate(backval + current.cost)
    max_avg = 0
    result = (-1, -1, -1, -1)
    for i in root.children:
        if i.ni == 0:
            result = i.action
            break
        if i.x / i.ni > max_avg:
            max_ucb = max_avg
            result = i.action
    #root.delete()
    return result

def simulatedMCTSAgent(grid, n, n_items, n_moves, C, resource):
    totalScore = 0
    for j in range(n_moves, 0, -1):
        action = simulatedMCTS(grid, n, n_items, j, C, resource)
        if(action == (-1, -1, -1, -1)):
            break
        totalScore = totalScore + bejeweledSimulation.oneMove(grid, n, n_items, action[0], action[1], action[2], action[3])
    return totalScore
#grid = np.zeros((8, 8))
#bejeweledSimulation.initGrid(grid, 8, 6)
#print(MCTSAgent(grid, 8, 6, 20, 2, 10))