#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: Shyam Makwana (smakwana), Mansi Sarda (msarda), Jiale Guan (guanjia)
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys

from queue import PriorityQueue
import time
start_time = time.time()


N=5

#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
    count = 0
    for ind,i in enumerate(state):         
        if i!=ind+1:                   ## here we are checking number of misplaced cells
            count+=1                   ## counting the misplced cells

    return count//2                    ## We are dividing the count by 2 as in one step we are swaping two elements,
                                       ## hence in one step we might correct the position of two elements if they are neighboring elements
                                       ## hence to keep the heuristic admissible and not overestimate the cost at any step,
                                       ## we are dividing by 2

#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS. 
#
def solve(initial_state):
    fringe = PriorityQueue()                               ## Here we have switched from a queue to a priority queue for fringe.
    d=0
    fringe.put((h(initial_state),(initial_state, [],0)))   ## here we are intially passing h(initially state) and depth is 0
    while not fringe.empty():
        h1,(state, path,d) = fringe.get(0)
        if is_goal(state):
            return path+[state,]                           ## returning the path when goal is reached

        for s in successors(state):
                fringe.put((d+1+h(s),(s, path+[state,],d+1)))   ## here depth is updated for each level that is g(s) + h(current state)
    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    '''
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))
    '''
    test_cases = []
    with open("birds.txt", 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
            print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))

    

print("--- %s seconds ---" % (time.time() - start_time))  
