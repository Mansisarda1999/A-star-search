#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: Shyam Makwana (smakwana), Mansi Sarda (msarda), Jiale Guan (guanjia)
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#

import sys
import numpy as np
from queue import PriorityQueue
ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

def for_row(state):                                       ## here we are taking all the row movements which is left and right shift for 
    suc_for_row = []                                      ## each row and the total successors for row movements are 10
    import copy
    for i in range(5):
        temp = state[i][0]
        ind=0
        #print(f"left move for {i}")
        a = copy.deepcopy(state)
        while ind<len(state)-1:
            a[i][ind] = state[i][ind+1]
            ind+=1
        a[i][4] = temp
        suc_for_row.append(a)
        #print(a)
        #print(f"Right move for {i}")

        a = copy.deepcopy(state)
        temp = state[i][-1]
        ind=0
        a = copy.deepcopy(state)
        while ind<len(state)-1:
            a[i][ind+1] = state[i][ind]
            ind+=1
        a[i][0] = temp

        suc_for_row.append(a)
        
    return suc_for_row

def for_col(m):                                   ## Here we are doing all column movements hence total movements are 10 for Up and Down
    suc_for_col = []
    import copy
    for i in range(len(m[0])):
        a = copy.deepcopy(m)
        temp = m[0][i]
        ind =1
        while ind<len(a):
            a[ind-1][i] = m[ind][i]
            ind+=1

        a[ind-1][i] = temp
        #print(f"Up move for {i}")
        suc_for_col.append(a)
        #print(a)

        a = copy.deepcopy(m)
        temp = m[4][i]
        ind =0
        while ind<len(a)-1:
            a[ind+1][i] = m[ind][i]
            ind+=1

        a[0][i] = temp
        suc_for_col.append(a)

    return suc_for_col


def outerclockwise(board):                      ## Here we are doing outer clockwise movement
    ROWS=5
    
    
    temp = board[0][4]
    board[0] = [board[1][0], *board[0][0:4]] 

    temp1 = board[4][4]
    i = 4
    while i > 0:
        board[i][4] = board[i-1][4]
        i -= 1
    board[1][4] = temp

    temp = board[4][0]
    board[4] = [*board[4][1:], board[4][4]] 
    board[4][3] = temp1

    for i in range(ROWS-1):
        board[i][0] = board[i+1][0]
    board[3][0] = temp

    return board

def outercounterclockwise(board):          ## Here we are outercounter clockwise movement
    
    temp = board[0][0]
    board[0] = [*board[0][1:],board[1][4]] 


    i = 0
    while i < 4:
        board[i][4] = board[i+1][4]
        i += 1
    board[4][4] = board[4][3]

    temp1 = board[4][0:3]
    board[4] = [board[3][3],*temp1,board[4][4]] 
    
    i=4
    while i>1:
        board[i][0] = board[i-1][0]
        i-=1
    board[1][0] = temp
    
    return board

def innerclockwise(board):                   ## Here we are doing inner clockwise movement

    temp = board[1][3]
    board[1] = [board[1][0],board[2][1],board[1][1],board[1][2],board[1][4]] 

    temp1 = board[3][3]
    board[3][3] = board[2][3]
    board[2][3] = temp
    

    temp = board[3][1]
    board[3][1] = board[3][2]
    board[3][2] = temp1

    board[2][1] = temp
    return board

def innercounterclockwise(state):          ## Here we are doing inner counter clockwise movement
    temp = state[1][1]
    state[1] = [state[1][0],state[1][2],state[1][3],state[2][3],state[1][4]] 

    temp1 = state[3][1]
    state[3][1] = state[2][1]
    state[2][1] = temp
    
    
    temp = state[3][3]
    state[3][3] = state[3][2]
    state[3][2] = temp1

    state[2][3] = temp
    return state
    
# return a list of possible successor states
def successors(s):                   ## Here we are calling all the above functions to get 24 successor states for each state
    import copy
    ROWS=5
    COLS=5
    a=[*for_row(s),*for_col(s)]
    state = copy.deepcopy(s)
    a.append(outerclockwise(state))
    state = copy.deepcopy(s)
    a.append(outercounterclockwise(state))
    state = copy.deepcopy(s)
    a.append(innerclockwise(state))
    state = copy.deepcopy(s)
    a.append(innercounterclockwise(state))
    return a

def dist_helper(i, j):             ## Here we are changing the manhattan distance 
                                   ## the code is explained in the report but this is not used in the final heuristic
    if(abs(i-j)<=2):
        return abs(i-j)
    else:
        return 1 if(abs(i-j)==4) else 2

def dist(i,j,row,col):
    return dist_helper(i, row) + dist_helper(j, col)   ## here we are using the dist_helper to modify the manhattan distance 
                                                       ## but this is not used in the final heuristic
def h(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            row = (state[i][j]-1)//ROWS               ## here we are getting the row number of the goal state for the given number
            col = (state[i][j]-1)%COLS                ## here we are getting the col number of the goal state for the given number
            #count += dist(i,j, row, col)
            count = count + abs(i - row) + abs(j-col) ## here we are counting the manhattan distance for ach element from given state to                                                              goal state and adding that
    
    return count/5                                    ## here we are dividing the total by 5

# check if we've reached the goal
def is_goal(state):
    count = 1
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j]!=count:
                return False                        ## if not correct position return False
            count += 1
    return True                                     ## if all correct return True

def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    
    state = [[initial_board[j+i] for j in range(5)] for i in range(0,25,5)]
    moves_set=['L1','R1','L2','R2','L3','R3','L4','R4','L5','R5','U1','D1','U2','D2','U3','D3','U4','D4','U5','D5','Oc','Occ','Ic','Icc']
    fringe = PriorityQueue()
    fringe.put((0,(state, [], [], 0)))                           ## here we are implemeting the priority queue

    while not fringe.empty():
        h1, (state, path, move_path, d) = fringe.get(0)
        if is_goal(state):
            return move_path
        i = 0
        for s in successors(state):
            fringe.put((d + 1 + h(s), (s, path + [state,], move_path + [moves_set[i]], d + 1)))
            i += 1
    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))
    
    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]
    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))
    
    # temp_list = [[start_state[j+i] for j in range(5)] for i in range(0,25,5)]

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
