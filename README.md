# A-star-search


***Part1 : Birds, heuristics, and A***
=======================================================================================================================================================================
The problem posed here is to rearrange the set of five birds into an order of 1 to N in as few steps as possible using A* search algorithm. It can be posed as a search problem in which there is a set of states S corresponding to all possible permutations of the birds. 

Implementation
=======================================================================================================================================================================
This problem can be solved using A* search algorithm where we need to search for a goal state where each bird is in the order 1 to N. Here in each of our successor state exactly one bird can exchange places with exactly one of its neighboring birds. The goal is to find the goal state in as few steps as possible and within 10 seconds of timespan.

**A\* search :** We need to define an admissible heuristic function h(s) and the g(s) which is the cost for the best path found till each state and apply Best First Search. 

**State space :**  In each step, exactly one bird exchange places with exactly one of its neighboring birds.

For example:
[1, 3, 4, 2, 5] - if this is the initial state
Then the successor states are:
- [3, 1, 4, 2, 5]
- [1, 4, 3, 2, 5]
- [1, 3, 2, 4, 5]
- [1, 3, 4, 5, 2]

**Successor function :** We already had a pre difined successor function in the given code given below.
- [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

**Goal state :** Goal state is the state where all the birds are arranged in the order of 1 to N.

**Heuristic function :** Here the heuristic function or h(s) is basically the number of misplaced birds.

**g(s) :** It is the cost of best path found so far to s.

**Best First Search :** It takes the most promising state or state with lowest cost from fringe first using a priority queue. Here the cost function f(s) estimates the 
cost from initial state, through sucessor state, to a goal state.
- Cost or f(s) = g(s) + h(s)

**Why the heuristic is admissible :** An heuristic h(s) is admissible if for any state s, 0 <= h(s) <= h*(s)
where h*(s) is the optimal cost from s to a goal. In other words, an admissible heuristic never overestimates the cost to the goal.
We have taken the count of misplaced elements and then dividing by 2.
***We are dividing the count by 2 as in one step we are swaping two elements,***
   - hence, in one step we might correct the position of two elements if they are neighboring elements
   - hence, to keep the heuristic admissible and not overestimate the cost at any step, we are dividing by 2
   
**A brief description of how the search algorithm works**

1. Define fringe using a Priority Queue. In this way, we can pop the most promising state from the fringe first so that we can reach the goal with minimum cost that is with less number of steps from the intial state to goal state through all the successor state.
2. Insert the initial state to the Fringe.
3. while Fringe is not empty:
    - pop the most promising state from the Fringe using the property of Priority Queue.
    - if the state is the goal state then return the path
    - get the successor state from the present state
    - insert every successor state and its cost into the Fringe
4. If the fringe is empty then return nothing in the path

For Examample:
From state [1, 3, 4, 2, 5] found goal state by taking path: [[1, 3, 4, 2, 5], [1, 3, 2, 4, 5], [1, 2, 3, 4, 5]]

The successor state for depth 1:
- [3, 1, 4, 2, 5]
- [1, 4, 3, 2, 5]
- [1, 3, 2, 4, 5]
- [1, 3, 4, 5, 2]

The successor state for depth 2:
- [3, 1, 2, 4, 5]
- [1, 2, 3, 4, 5]
- [1, 3, 4, 2, 5]
- [1, 3, 2, 5, 4]

![part1](https://media.github.iu.edu/user/20798/files/66549d11-99bd-45b8-940f-10f4c8656ecd)

The above picture shows the path followed and the cost for that path. The state with minimum cost is popped at each level and the goal is reached in 3 steps.

**Problems you faced :** This Problem gave me a basic understanding about how to implement A* search algorithm. Initially we faced problem to define the cost function for each state. We missed the point where we also need to add depth to the cost for each succcessor state. We referred the 8 puzzle problem discussed in class for better understanding.

# ***Part 2: The 2022 Puzzle***

We are given a board of 5x5 size, and we have to arrange the number of the tile in sequence, i.e., 1,2,3,4,5,...,24,25 in the 5x5 size board. We are given the initial state and must reach the goal state using eight different moves.

# **Implementation**

This problem can be solved using the A* search algorithm, where we need to search for a goal state where each tile is in the order of 1 to 25. Here in each of our successor states, we can make eight different moves: shifting the row in a left direction, right direction, up a column, down column, rotating the outer border clockwise and counterclockwise, and the inner border clockwise and counterclockwise. So, there are a total of 8 different moves, and using these moves, we have to reach the goal state.

**A\* search:** We need to define an admissible heuristic function h(s) and the g(s), which is the cost for the fewest moves found till each state, and apply Best First Search.

**State space:** We can make eight different moves in each step. Thus, 24 states are possible from 1 state.

**Successor function:** All the 24 states from the current state where tiles can be placed.

**Initial state:** The random arrangement of the 5x5 board.

**Goal state:** Goal state is the state where all the tiles are arranged in the order from 1 to 25.

**g(s):** It is the cost of the best path found so far to s.

**Best First Search:** It takes the most promising state or state with the lowest cost from a fringe using a priority queue. Here the cost function f(s) estimates the

Cost from the initial state, through the successor state, to a goal state.

- Cost or f(s) = g(s) + h(s)

**Why the heuristic is admissible :** An heuristic h(s) is admissible if for any state s, 0 <= h(s) <= h*(s), Where h*(s) is the optimal cost from s to a goal, in other words, an admissible heuristic never overestimates the plan's cost.

## **Heuristic function:**</br>

- **Here, the heuristic function or h(s) is the manhattan distance of the 5x5 board.**</br>

- **Explanation:** First, we tried different heuristic functions, which I have explained below in the problems faced. After that, we modified the heuristic function differently, which is explained below with an example.</br>

- Let's take a random board:</br>
![board](https://media.github.iu.edu/user/21472/files/f0d625b0-c0c1-4fe0-b6a8-225956cb720a)

- All the rows and columns are correct except the first and last columns. So, let's say the 25 correct position is at (4,4), and the current position is (0,0). So, the manhattan distance is 8. So, we tried this heuristic function, but it was going into a loop.</br>

- So, we modified the manhattan distance. The distance is not 8; it's two only because if we shift the first-row left side and the last column upside, the 25 will be at the correct position. So, the distance is two only and not 8. We tried this approach (commented on in the code), but it gave a suboptimal answer.

- Finally, we came up with the old manhattan distance but divided the total distance by five because when making any eight moves, we change any tile position by 5. So, to bring it to the correct position, we need to divide by 5. After doing this, we get the optimal answer.

**A brief description of how the search algorithm works**

1. Define Fringe using a Priority Queue. In this way, we can pop the most promising state from the Fringe first to reach the goal with minimum cost, that is, with fewer moves from the initial state to the goal state through all the successor states.

2. Insert the initial state into the Fringe.

3. while Fringe is not empty:

- pop the most promising state from the Fringe using the property of Priority Queue.

- if the state is the goal state, then return the total moves as a list.

- get the successor state from the present state.

- insert every successor state and its cost into the Fringe.

4. If the Fringe is empty, then return an empty list.

**Problems we faced:** We tried several heuristic functions such as misplaced tiles, manhattan distance, and many variations of it. First, we tried misplaced tiles and manhattan distance, but it was going in an infinite loop. So, after that, we tried a combination of it, i.e., misplaced + manhattan, abs(misplaced - manhattan), minimum(misplaced, manhattan), and maximum(misplaced, manhattan), but all the heuristic functions were giving wrong answers. So, we tried to compute manhattan distance differently, i.e., calculate the distance between the misplaced tiles and the actual tile position and the same for the column and add it. Using this, we got our moves, but it was suboptimal. We tried different heuristics, but we were getting suboptimal answers.

### 1. In this problem, what is the branching factor of the search tree?

Ans: There are eight different moves, as mentioned above. So, using that eight moves, we are getting 24 other states from the current state. So, the branching factor(b) for this problem is 24.

### 2. If the solution can be reached in 7 moves, how many states would we need to explore before we found it if we used BFS instead of A* search? A rough answer is fine.

Ans: If we use BFS instead of A*, then we will explore all the states of a given state, and the time complexity will be b<sup>d</sup> (b = branching factor, d = depth of the tree). So, we will explore 24<sup>7</sup> states if we use BFS, and the solution can be reached in 7 moves.
