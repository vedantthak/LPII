import heapq

def a_star(graph, start, goal, heuristic):
    g = {v: float('inf') for v in graph}
    f = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}

    g[start] = 0
    f[start] = heuristic[start]

    open_list = [(f[start], start)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(parent, goal, g[goal])

        for neighbor, weight in graph[current]:
            tentative_g = g[current] + weight
            if tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f[neighbor], neighbor))

    return []

def reconstruct_path(parent, goal, cost):
    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    path.reverse()
    print("Path cost:", cost)
    return path

def main():
    n = int(input("Enter number of vertices: "))
    print("Enter vertex names (e.g., A B C ...):")
    vertices = input().split()

    graph = {v: [] for v in vertices}

    m = int(input("Enter number of edges: "))
    print("Enter edges (format: source destination weight):")
    for _ in range(m):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        # graph[v].append((u, w))  # Uncomment for undirected graph

    heuristic = {}
    print("Enter heuristic values (e.g., A 4 B 2 ...):")
    for _ in range(n):
        name, h = input().split()
        heuristic[name] = int(h)

    start = input("Enter start vertex: ")
    goal = input("Enter goal vertex: ")

    path = a_star(graph, start, goal, heuristic)
    if path:
        print("Optimal path:", ' -> '.join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()


# Let's go through the code in detail, explaining each line and its purpose.

# A Algorithm Code Explanation:*
# Imports:
# python
# Copy code
# import heapq
# heapq is a Python module used for heap queue (priority queue) algorithms. In A*, we use this to manage the open list of vertices, where each vertex is stored with its cost value (f), allowing us to efficiently retrieve the vertex with the lowest cost.

# a_star Function:
# python
# Copy code
# def a_star(graph, start, goal, heuristic):
# This is the main function implementing the A* algorithm.

# graph: A dictionary where each vertex has a list of its neighbors and their respective edge weights.

# start: The starting vertex for the pathfinding.

# goal: The target (goal) vertex we want to reach.

# heuristic: A dictionary mapping each vertex to its heuristic value, which estimates the cost to reach the goal.

# python
# Copy code
#     g = {v: float('inf') for v in graph}
#     f = {v: float('inf') for v in graph}
#     parent = {v: None for v in graph}
# g: A dictionary that stores the cost from the start vertex to each vertex. Initially, all values are set to infinity (float('inf')), except for the start vertex which will be updated later.

# f: A dictionary storing the total estimated cost to reach the goal through each vertex. f(v) = g(v) + h(v) where h(v) is the heuristic value for vertex v. Like g, it starts as infinity for all vertices.

# parent: A dictionary that will store the parent of each vertex in the path, allowing us to reconstruct the optimal path later. Initially, all values are None.

# python
# Copy code
#     g[start] = 0
#     f[start] = heuristic[start]
# The g[start] is set to 0 because the cost to reach the starting point from itself is zero.

# The f[start] is set to the heuristic value of the start vertex, as the total cost estimate for the start vertex is just its heuristic at the beginning.

# python
# Copy code
#     open_list = [(f[start], start)]
# open_list is a list that will function as a priority queue, where vertices are stored as tuples (f-value, vertex).

# Initially, only the start vertex is in the open list with its f value.

# python
# Copy code
#     while open_list:
# This starts a loop that will run as long as there are vertices in the open list. The algorithm terminates when there are no more vertices to process or the goal is found.

# python
# Copy code
#         _, current = heapq.heappop(open_list)
# heapq.heappop pops the vertex with the lowest f value from the open list (the most promising vertex to explore).

# We ignore the f value here (as it is stored in _) and just use the current vertex.

# python
# Copy code
#         if current == goal:
#             return reconstruct_path(parent, goal, g[goal])
# If the current vertex is the goal, the function immediately returns the reconstructed path from the start to the goal. The path is reconstructed by tracing back the parent of each vertex from the goal.

# python
# Copy code
#         for neighbor, weight in graph[current]:
# For each neighbor of the current vertex, we check if it’s possible to improve its cost to reach the goal.

# python
# Copy code
#             tentative_g = g[current] + weight
# tentative_g is the calculated cost to reach the neighbor vertex via the current vertex. It is the sum of the cost to reach the current vertex (g[current]) and the weight of the edge between the current and the neighbor vertex (weight).

# python
# Copy code
#             if tentative_g < g[neighbor]:
# If the tentative cost to reach the neighbor is less than the current recorded cost (g[neighbor]), then it means we’ve found a better (lower-cost) way to reach that neighbor.

# python
# Copy code
#                 parent[neighbor] = current
#                 g[neighbor] = tentative_g
#                 f[neighbor] = tentative_g + heuristic[neighbor]
#                 heapq.heappush(open_list, (f[neighbor], neighbor))
# parent[neighbor] = current: We update the parent of the neighbor to be the current vertex, as it’s the best way to reach it at the moment.

# g[neighbor] = tentative_g: We update the cost to reach the neighbor.

# f[neighbor] = tentative_g + heuristic[neighbor]: We update the total estimated cost (f), which is the sum of the actual cost to reach the neighbor (g[neighbor]) and its heuristic value (heuristic[neighbor]).

# heapq.heappush(open_list, (f[neighbor], neighbor)): The neighbor is pushed to the open list, so it will be considered for future exploration.

# python
# Copy code
#     return []
# If the open list is empty and the goal has not been reached, it means there is no path from the start to the goal. The function returns an empty list.

# reconstruct_path Function:
# python
# Copy code
# def reconstruct_path(parent, goal, cost):
#     path = []
# This function is used to reconstruct the optimal path from the start vertex to the goal by tracing back the parents of each vertex.

# python
# Copy code
#     while goal:
#         path.append(goal)
#         goal = parent[goal]
# Starting from the goal, we trace back each vertex to its parent and append each vertex to the path list.

# python
# Copy code
#     path.reverse()
# Since the path is reconstructed from the goal to the start, we reverse the list to get the correct order from start to goal.

# python
# Copy code
#     print("Path cost:", cost)
#     return path
# Finally, the function prints the total cost of the path (the cost to reach the goal) and returns the reconstructed path.

# main Function:
# python
# Copy code
# def main():
#     n = int(input("Enter number of vertices: "))
#     print("Enter vertex names (e.g., A B C ...):")
#     vertices = input().split()
# The main function starts by reading the number of vertices in the graph and the vertex names (which are entered as space-separated strings).

# python
# Copy code
#     graph = {v: [] for v in vertices}
# It then creates an empty graph with each vertex having an empty list of neighbors.

# python
# Copy code
#     m = int(input("Enter number of edges: "))
#     print("Enter edges (format: source destination weight):")
# The user is asked to enter the number of edges in the graph, followed by the edges themselves, where each edge consists of a source vertex, a destination vertex, and the weight of the edge.

# python
# Copy code
#     for _ in range(m):
#         u, v, w = input().split()
#         w = int(w)
#         graph[u].append((v, w))
# For each edge, the code splits the input to extract the source vertex (u), the destination vertex (v), and the weight of the edge (w), then adds the edge to the graph (as a tuple (v, w)).

# python
# Copy code
#     heuristic = {}
#     print("Enter heuristic values (e.g., A 4 B 2 ...):")
#     for _ in range(n):
#         name, h = input().split()
#         heuristic[name] = int(h)
# The heuristic values are then collected for each vertex. These are input by the user, mapping each vertex to a heuristic value.

# python
# Copy code
#     start = input("Enter start vertex: ")
#     goal = input("Enter goal vertex: ")
# The start and goal vertices are entered by the user.

# python
# Copy code
#     path = a_star(graph, start, goal, heuristic)
#     if path:
#         print("Optimal path:", ' -> '.join(path))
#     else:
#         print("No path found.")
# The a_star function is called to find the optimal path from the start to the goal using the A* algorithm.

# If a path is found, it is printed in a readable format (A -> B -> C), otherwise, a message is displayed saying no path was found.

# In Summary:
# A Algorithm* is an informed search algorithm used to find the shortest path between nodes, where the heuristic function guides the search. It uses the idea of cost (g) and estimated cost (f = g + h) to prioritize which node to explore next.

# Priority Queue (via heapq) is used to always process the node with the lowest total cost (f).

# Reconstruction of the Path is done by tracing back the parent of each node from the goal to the start.







# You said:
# give dry run


# ChatGPT said:
# Let's perform a dry run of the provided A* algorithm using a small example graph. Here's the scenario:

# Graph:
# Vertices: A, B, C, D

# Edges:

# A -> B (weight 1)

# A -> C (weight 4)

# B -> C (weight 2)

# B -> D (weight 5)

# C -> D (weight 1)

# Heuristic values:

# A: 7

# B: 6

# C: 2

# D: 0

# Start vertex: A

# Goal vertex: D

# Step-by-step Dry Run:
# Initial Setup:

# Graph:

# python
# Copy code
# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 2), ('D', 5)],
#     'C': [('A', 4), ('B', 2), ('D', 1)],
#     'D': [('B', 5), ('C', 1)]
# }
# Heuristic:

# python
# Copy code
# heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
# Start: A

# Goal: D

# Execution:
# Initialization:
# g = {A: inf, B: inf, C: inf, D: inf}

# f = {A: inf, B: inf, C: inf, D: inf}

# parent = {A: None, B: None, C: None, D: None}

# g[start] = 0 → g = {A: 0, B: inf, C: inf, D: inf}

# f[start] = heuristic[start] → f = {A: 7, B: inf, C: inf, D: inf}

# open_list = [(7, 'A')]

# Iteration 1:
# Pop the vertex with the lowest f value:

# open_list = [(7, 'A')]

# Pop A → current = 'A', f[A] = 7

# Check if current == goal:

# current = A, goal = D, so not yet.

# Explore neighbors of A:

# Neighbors of A: B (weight 1), C (weight 4)

# For neighbor B:

# tentative_g = g[A] + weight = 0 + 1 = 1

# tentative_g < g[B] (since g[B] = inf), so:

# parent[B] = A

# g[B] = 1

# f[B] = g[B] + heuristic[B] = 1 + 6 = 7

# Push B to open_list: open_list = [(7, 'B')]

# For neighbor C:

# tentative_g = g[A] + weight = 0 + 4 = 4

# tentative_g < g[C] (since g[C] = inf), so:

# parent[C] = A

# g[C] = 4

# f[C] = g[C] + heuristic[C] = 4 + 2 = 6

# Push C to open_list: open_list = [(7, 'B'), (6, 'C')]

# open_list after iteration 1: [(6, 'C'), (7, 'B')]

# Iteration 2:
# Pop the vertex with the lowest f value:

# open_list = [(6, 'C'), (7, 'B')]

# Pop C → current = 'C', f[C] = 6

# Check if current == goal:

# current = C, goal = D, so not yet.

# Explore neighbors of C:

# Neighbors of C: A (weight 4), B (weight 2), D (weight 1)

# For neighbor A:

# tentative_g = g[C] + weight = 4 + 4 = 8

# tentative_g >= g[A] (since g[A] = 0), no update.

# For neighbor B:

# tentative_g = g[C] + weight = 4 + 2 = 6

# tentative_g >= g[B] (since g[B] = 1), no update.

# For neighbor D:

# tentative_g = g[C] + weight = 4 + 1 = 5

# tentative_g < g[D] (since g[D] = inf), so:

# parent[D] = C

# g[D] = 5

# f[D] = g[D] + heuristic[D] = 5 + 0 = 5

# Push D to open_list: open_list = [(5, 'D'), (7, 'B')]

# open_list after iteration 2: [(5, 'D'), (7, 'B')]

# Iteration 3:
# Pop the vertex with the lowest f value:

# open_list = [(5, 'D'), (7, 'B')]

# Pop D → current = 'D', f[D] = 5

# Check if current == goal:

# current = D, goal = D, so we have reached the goal.

# Reconstruct the path:

# Start from goal (D), trace back using the parent dictionary.

# parent[D] = C, parent[C] = A, so the path is A -> C -> D.

# Return the path and the total cost:

# Path: A -> C -> D

# Cost: g[D] = 5

# Final Output:
# Optimal Path: A -> C -> D

# Path Cost: 5

# Summary of Dry Run:
# The A* algorithm successfully finds the optimal path from the start vertex (A) to the goal vertex (D), considering both the actual cost to reach a vertex (g) and the heuristic estimate of the remaining cost (h).

# The path found is A -> C -> D, with a total cost of 5.







# You said:
# TAKE INPUT AND GIVE OUTPUT


# ChatGPT said:
# Sure! Here's a working version of the A* Search algorithm in Python that:

# Takes input from the user for the graph (nodes, edges),

# Takes heuristic values,

# Runs A* search, and

# Prints the output (path and cost).

# You can copy and run this code in any Python environment:

# python
# Copy code
# import heapq

# def a_star(graph, start, goal, heuristic):
#     g = {v: float('inf') for v in graph}
#     f = {v: float('inf') for v in graph}
#     parent = {v: None for v in graph}

#     g[start] = 0
#     f[start] = heuristic[start]

#     open_list = [(f[start], start)]

#     while open_list:
#         _, current = heapq.heappop(open_list)

#         if current == goal:
#             return reconstruct_path(parent, goal, g[goal])

#         for neighbor, weight in graph[current]:
#             tentative_g = g[current] + weight
#             if tentative_g < g[neighbor]:
#                 parent[neighbor] = current
#                 g[neighbor] = tentative_g
#                 f[neighbor] = tentative_g + heuristic[neighbor]
#                 heapq.heappush(open_list, (f[neighbor], neighbor))

#     return []

# def reconstruct_path(parent, goal, cost):
#     path = []
#     while goal:
#         path.append(goal)
#         goal = parent[goal]
#     path.reverse()
#     print("Path cost:", cost)
#     return path

# def main():
#     n = int(input("Enter number of vertices: "))
#     print("Enter vertex names (e.g., A B C ...):")
#     vertices = input().split()

#     graph = {v: [] for v in vertices}

#     m = int(input("Enter number of edges: "))
#     print("Enter edges in format: source destination weight")
#     for _ in range(m):
#         u, v, w = input().split()
#         w = int(w)
#         graph[u].append((v, w))
#         # Uncomment the line below for undirected graph
#         # graph[v].append((u, w))

#     heuristic = {}
#     print("Enter heuristic values (format: vertex value)")
#     for _ in range(n):
#         name, h = input().split()
#         heuristic[name] = int(h)

#     start = input("Enter start vertex: ")
#     goal = input("Enter goal vertex: ")

#     path = a_star(graph, start, goal, heuristic)
#     if path:
#         print("Optimal path:", ' -> '.join(path))
#     else:
#         print("No path found.")

# if __name__ == "__main__":
#     main()
# ✅ Sample Input to Use:
# mathematica
# Copy code
# Enter number of vertices: 4
# Enter vertex names (e.g., A B C ...): A B C D
# Enter number of edges: 5
# Enter edges in format: source destination weight
# A B 1
# A C 4
# B C 2
# B D 5
# C D 1
# Enter heuristic values (format: vertex value)
# A 7
# B 6
# C 2
# D 0
# Enter start vertex: A
# Enter goal vertex: D
# ✅ Output:
# mathematica
# Copy code
# Path cost: 5
# Optimal path: A -> C -> D




# 1. What is the purpose of the A algorithm?*
# Answer: The A* algorithm is used to find the shortest path between two nodes in a graph, considering both the cost to reach a node and an estimate of the remaining cost (heuristic) to reach the goal.

# 2. How does A use the heuristic function?*
# Answer: A* uses the heuristic function to estimate the remaining cost from the current node to the goal node. This helps in prioritizing the nodes to explore, guiding the algorithm towards the goal more efficiently.

# 3. What is the difference between g(n) and f(n) in A?*
# Answer:

# g(n) is the actual cost from the start node to the current node n.

# f(n) is the estimated total cost of the cheapest solution through the node n, calculated as f(n) = g(n) + h(n), where h(n) is the heuristic estimate to the goal.

# 4. Why do we use a priority queue (min-heap) in A?*
# Answer: A priority queue (min-heap) is used in A* to always expand the node with the smallest f(n) value, ensuring the algorithm explores the most promising nodes first.

# 5. What is the role of the parent dictionary in A?*
# Answer: The parent dictionary keeps track of the path taken to reach each node. It helps in reconstructing the optimal path once the goal node is reached.

# 6. What is the time complexity of A?*
# Answer: The time complexity of A* is O(E log V), where E is the number of edges and V is the number of vertices, because we use a priority queue to handle nodes efficiently.

# 7. How does A guarantee the optimal path?*
# Answer: A* guarantees the optimal path if the heuristic used is admissible (i.e., it never overestimates the true cost to reach the goal) and consistent (i.e., the estimated cost is always less than or equal to the cost from a node to its neighbor plus the cost to reach the neighbor).

# 8. What would happen if the heuristic is not admissible?
# Answer: If the heuristic is not admissible (i.e., it overestimates the remaining cost), A* may not find the optimal path, and it could produce incorrect results.

# 9. What does the function reconstruct_path do?
# Answer: The reconstruct_path function traces back from the goal node to the start node using the parent dictionary, reconstructing the optimal path and returning it.

# 10. Explain how the f value is updated during the search.
# Answer: The f value for a node is updated when a shorter path to that node is found. It is recalculated as the sum of the g value (cost from start) and the heuristic value (h).

# 11. What are the inputs to the A algorithm in this code?*
# Answer: The inputs to the A* algorithm are:

# A graph represented as an adjacency list.

# The starting vertex and the goal vertex.

# The heuristic values for each vertex.

# 12. What would happen if the graph were undirected?
# Answer: If the graph were undirected, we would need to uncomment the line graph[v].append((u, w)) to add the reverse edge, ensuring bidirectional connectivity between nodes.

# 13. What is the space complexity of the A algorithm?*
# Answer: The space complexity is O(V), where V is the number of vertices, because we store the g, f, and parent values for each vertex, and the open list (priority queue) can hold up to V vertices.

# 14. What would happen if there is no path between the start and goal vertices?
# Answer: If there is no path, the algorithm will return an empty list [], and the output will be "No path found."

# 15. How does the A algorithm handle updates in the open list?*
# Answer: When a better path to a neighbor is found, the neighbor’s f value is updated, and it is pushed back into the open list with the updated value, ensuring that the priority queue always contains the node with the lowest f value.
