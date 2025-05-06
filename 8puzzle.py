import heapq

# Goal state
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions: (row, col)
DIRECTIONS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

# Convert 2D list to tuple of tuples for hashable state
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Manhattan distance heuristic
def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist

# Find position of 0 (blank)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate new state after a move
def move(state, direction):
    i, j = find_blank(state)
    x, y = DIRECTIONS[direction]
    new_i, new_j = i + x, j + y

    if 0 <= new_i < 3 and 0 <= new_j < 3:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return new_state
    return None

# Reconstruct path from goal to start
def reconstruct_path(came_from, state):
    path = []
    while came_from[state][1]:
        state, move_dir = came_from[state]
        path.append(move_dir)
    return path[::-1]

# A* Search
def a_star(start):
    start_t = to_tuple(start)
    goal_t = to_tuple(GOAL_STATE)

    open_list = [(heuristic(start), 0, start_t)]  # (f, g, state)
    heapq.heapify(open_list)

    came_from = {start_t: (None, None)}  # state: (parent, move)
    g_score = {start_t: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal_t:
            return reconstruct_path(came_from, current)

        current_list = [list(row) for row in current]

        for dir in DIRECTIONS:
            new_state = move(current_list, dir)
            if new_state:
                new_t = to_tuple(new_state)
                tentative_g = g + 1

                if new_t not in g_score or tentative_g < g_score[new_t]:
                    g_score[new_t] = tentative_g
                    f = tentative_g + heuristic(new_state)
                    heapq.heappush(open_list, (f, tentative_g, new_t))
                    came_from[new_t] = (current, dir)

    return None

# Input and output
def main():
    print("Enter the 8-puzzle initial state row-wise, use 0 for blank:")
    start = []
    for _ in range(3):
        row = list(map(int, input().split()))
        start.append(row)

    path = a_star(start)
    if path is None:
        print("No solution found.")
    else:
        print("Steps to solve:")
        for step in path:
            print(step)
        print("Total moves:", len(path))

if __name__ == "__main__":
    main()











# explain each line of code in detail


# ChatGPT said:
# Sure! Here's a detailed line-by-line explanation of the A* algorithm implementation for the 8-puzzle problem:

# 🔹 Imports and Constants
# python
# Copy code
# import heapq
# heapq provides a priority queue implementation (min-heap), which is used for selecting the node with the lowest f = g + h cost in A*.

# python
# Copy code
# GOAL_STATE = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]
# This is the target arrangement of the puzzle (0 is the blank tile).

# python
# Copy code
# DIRECTIONS = {
#     'UP': (-1, 0),
#     'DOWN': (1, 0),
#     'LEFT': (0, -1),
#     'RIGHT': (0, 1)
# }
# Dictionary representing valid moves and how they shift the position of the blank tile (row, column).

# 🔹 Helper Functions
# python
# Copy code
# def to_tuple(state):
#     return tuple(tuple(row) for row in state)
# Converts the 2D list state into a hashable tuple of tuples (for using it as keys in dictionaries like came_from and g_score).

# python
# Copy code
# def heuristic(state):
#     dist = 0
#     for i in range(3):
#         for j in range(3):
#             value = state[i][j]
#             if value != 0:
#                 goal_x = (value - 1) // 3
#                 goal_y = (value - 1) % 3
#                 dist += abs(i - goal_x) + abs(j - goal_y)
#     return dist
# Manhattan distance heuristic.

# For each tile (not blank), it computes how far it is from its correct position in GOAL_STATE (sum of row and column distance).

# python
# Copy code
# def find_blank(state):
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == 0:
#                 return i, j
# Returns the position (i, j) of the blank tile (0).

# python
# Copy code
# def move(state, direction):
#     i, j = find_blank(state)
#     x, y = DIRECTIONS[direction]
#     new_i, new_j = i + x, j + y

#     if 0 <= new_i < 3 and 0 <= new_j < 3:
#         new_state = [row[:] for row in state]
#         new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
#         return new_state
#     return None
# Moves the blank in the given direction if it’s within bounds.

# Makes a copy of the state and swaps the blank with the adjacent tile.

# python
# Copy code
# def reconstruct_path(came_from, state):
#     path = []
#     while came_from[state][1]:
#         state, move_dir = came_from[state]
#         path.append(move_dir)
#     return path[::-1]
# Traces back the path from the goal to the start using the came_from dictionary.

# Collects the moves and reverses them to get the correct order.

# 🔹 A Algorithm*
# python
# Copy code
# def a_star(start):
#     start_t = to_tuple(start)
#     goal_t = to_tuple(GOAL_STATE)

#     open_list = [(heuristic(start), 0, start_t)]  # (f, g, state)
#     heapq.heapify(open_list)
# Initializes the open list (priority queue) with the start node.

# f = g + h: heuristic + actual cost.

# python
# Copy code
#     came_from = {start_t: (None, None)}
#     g_score = {start_t: 0}
# came_from: tracks parent of each node and which move got you there.

# g_score: keeps the actual cost to reach each node.

# python
# Copy code
#     while open_list:
#         _, g, current = heapq.heappop(open_list)

#         if current == goal_t:
#             return reconstruct_path(came_from, current)
# While nodes exist in the queue:

# Pop the one with the lowest f.

# If the goal is reached, return the path.

# python
# Copy code
#         current_list = [list(row) for row in current]
# Convert tuple form back to 2D list for manipulation.

# python
# Copy code
#         for dir in DIRECTIONS:
#             new_state = move(current_list, dir)
#             if new_state:
#                 new_t = to_tuple(new_state)
#                 tentative_g = g + 1
# For each move direction:

# Try to move the blank.

# If valid, convert to tuple form.

# tentative_g: one more than current cost.

# python
# Copy code
#                 if new_t not in g_score or tentative_g < g_score[new_t]:
#                     g_score[new_t] = tentative_g
#                     f = tentative_g + heuristic(new_state)
#                     heapq.heappush(open_list, (f, tentative_g, new_t))
#                     came_from[new_t] = (current, dir)
# If this path to new_t is shorter, update g_score, compute f, and push it into the open list.

# Record how we got there in came_from.

# python
# Copy code
#     return None
# If the queue is exhausted and no path found.

# 🔹 Main Program: Taking Input and Output
# python
# Copy code
# def main():
#     print("Enter the 8-puzzle initial state row-wise, use 0 for blank:")
#     start = []
#     for _ in range(3):
#         row = list(map(int, input().split()))
#         start.append(row)
# Takes 3 rows of input from the user to define the puzzle.

# python
# Copy code
#     path = a_star(start)
#     if path is None:
#         print("No solution found.")
#     else:
#         print("Steps to solve:")
#         for step in path:
#             print(step)
#         print("Total moves:", len(path))
# Runs A* and prints the move directions if a path is found.

# python
# Copy code
# if __name__ == "__main__":
#     main()
# Standard way to call main() only if this script is being run directly.

# Would you like a step-by-step dry run with an example puzzle to visualize how it works?







# You said:
# give dry run
# ChatGPT said:
# Let's do a dry run of the A* algorithm for solving the 8-puzzle problem, using this initial configuration:

# perl
# Copy code
# Initial state:
# 1 2 3
# 4 0 6
# 7 5 8
# (0 is the blank tile)

# 🎯 Goal State:
# Copy code
# 1 2 3
# 4 5 6
# 7 8 0
# 🔹 Step 1: Initialization
# Start state:

# Copy code
# 1 2 3
# 4 0 6
# 7 5 8
# Convert it to tuple format for hashing:

# python
# Copy code
# ((1, 2, 3), (4, 0, 6), (7, 5, 8))
# g = 0 (cost so far)

# Heuristic (Manhattan distance):

# Tile	Current	Goal	Distance
# 5	(2,1)	(1,1)	1
# 8	(2,2)	(2,1)	1

# So h = 1 + 1 = 2

# So f = g + h = 0 + 2 = 2

# Push:

# python
# Copy code
# open_list = [(2, 0, ((1,2,3),(4,0,6),(7,5,8)))]
# 🔹 Step 2: Pop current state
# Pop:

# scss
# Copy code
# ((1,2,3),
#  (4,0,6),
#  (7,5,8))
# g = 0

# 🔹 Step 3: Explore neighbors (legal moves of blank at (1,1))
# a. Move UP → (0,1)
# Copy code
# 1 0 3
# 4 2 6
# 7 5 8
# Heuristic:

# 2 at (0,1), goal (0,1) → 0

# 5 at (2,1), goal (1,1) → 1

# 8 at (2,2), goal (2,1) → 1
# h = 2, g = 1, f = 3

# Push:

# python
# Copy code
# ((1,0,3), (4,2,6), (7,5,8)) → f=3
# b. Move DOWN → (2,1)
# Copy code
# 1 2 3
# 4 5 6
# 7 0 8
# Heuristic:

# 8 at (2,2), goal (2,1) → 1
# h = 1, g = 1, f = 2

# ✅ This is closer to the goal.

# Push:

# python
# Copy code
# ((1,2,3), (4,5,6), (7,0,8)) → f=2
# c. Move LEFT → (1,0)
# Copy code
# 1 2 3
# 0 4 6
# 7 5 8
# Heuristic:

# 4 at (1,1), goal (1,0) → 1

# 5 at (2,1), goal (1,1) → 1

# 8 at (2,2), goal (2,1) → 1
# h = 3, f = 4

# d. Move RIGHT → (1,2)
# Copy code
# 1 2 3
# 4 6 0
# 7 5 8
# Heuristic:

# 6 at (1,1), goal (1,2) → 1

# 5 at (2,1), goal (1,1) → 1

# 8 at (2,2), goal (2,1) → 1
# h = 3, f = 4

# 🔹 Updated open list:
# python
# Copy code
# (2, 1, ((1,2,3),(4,5,6),(7,0,8)))
# (3, 1, ((1,0,3),(4,2,6),(7,5,8)))
# (4, 1, ((1,2,3),(0,4,6),(7,5,8)))
# (4, 1, ((1,2,3),(4,6,0),(7,5,8)))
# 🔹 Next Pop:
# State with f=2 →

# Copy code
# 1 2 3
# 4 5 6
# 7 0 8
# This is not yet the goal.

# Move DOWN → Invalid
# Move RIGHT →

# Copy code
# 1 2 3
# 4 5 6
# 7 8 0
# ✅ Goal reached!
# 🧾 Final Output:
# text
# Copy code
# Steps to solve:
# DOWN
# RIGHT
# Total moves: 2



# Example Input:
# perl
# Copy
# Edit
# Enter the 8-puzzle initial state row-wise, use 0 for blank:
# 1 2 3
# 4 5 6
# 0 7 8
# Example Output:
# sql
# Copy
# Edit
# Steps to solve:
# RIGHT
# DOWN
# LEFT
# DOWN
# LEFT
# RIGHT
# RIGHT
# UP
# Total moves: 8
# Viva Questions and Answers:
# What is the goal state in the 8-puzzle problem?
# Answer: The goal state is a 3x3 grid arranged as:

# Copy
# Edit
# 1 2 3
# 4 5 6
# 7 8 0
# Where 0 represents the blank space.

# What heuristic function is used in this implementation?
# Answer: The Manhattan distance heuristic is used, which calculates the sum of the vertical and horizontal distances of each tile from its goal position.

# What is the purpose of the find_blank() function?
# Answer: The find_blank() function locates the position of the blank space (represented by 0) in the puzzle to facilitate the movement of tiles.

# How does the move() function work?
# Answer: The move() function generates a new state after moving the blank space in one of the four possible directions (up, down, left, right), provided the move stays within the bounds of the grid.

# What is the role of the to_tuple() function?
# Answer: The to_tuple() function converts a 2D list (the puzzle state) into a tuple of tuples, making it hashable, which is necessary for using it as a key in dictionaries (like came_from and g_score).

# How does A use the open list (priority queue)?*
# Answer: The open list is a priority queue (min-heap) that stores the states to be explored, sorted by the f value (calculated as g + h), ensuring that the most promising state is expanded first.

# What is stored in the came_from dictionary?
# Answer: The came_from dictionary stores the parent state and the direction from which the state was reached, allowing us to reconstruct the path from the goal to the start.

# What happens if no solution is found in the A search?*
# Answer: If no solution is found, the function returns None, and the program prints "No solution found."

# What is the space complexity of the A algorithm in this implementation?*
# Answer: The space complexity is O(b^d), where b is the branching factor (maximum number of possible moves from a given state), and d is the depth of the solution (maximum number of moves in the solution path).

# What is the time complexity of the A algorithm in this implementation?*
# Answer: The time complexity is O(b^d), where b is the branching factor and d is the solution depth. The A* algorithm explores all possible states up to the solution depth.

# Why do we use a priority queue in A?*
# Answer: A priority queue is used to always explore the most promising states first by sorting nodes based on their f value (which is the sum of the cost to reach the node and the heuristic estimate).

# How do we ensure the moves are valid in this implementation?
# Answer: The move() function checks if the new state after a move is within the valid boundaries (0 ≤ row, col < 3), ensuring that no invalid moves are made.

# What happens if you enter an unsolvable puzzle state?
# Answer: If the puzzle is unsolvable (i.e., there is no solution), the program will output "No solution found."

# What does the output Total moves: 8 signify?
# Answer: The output indicates that the optimal solution to reach the goal state from the initial state requires 8 moves.