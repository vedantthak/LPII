"""
Assignment-A1: DFS & BFS

Problem Statement: Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

"""

from collections import deque

class Graph:
    # Constructor to initalize an empty dictionary
    def __init__(self):
        self.graph = {}

    # Add edges
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected; Comment this line if graph is directed.

    # Perform Depth First Search (DFS)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbour in self.graph.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    # Perform Breadth First Search (BFS)
    def bfs(self, start):
        visited = set()
        visited.add(start)
        queue = deque([start])

        def bfs_helper():
            if not queue:
                return

            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph.get(vertex, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
            bfs_helper()

        bfs_helper()

def main():
    g = Graph()

    while True:
        print("\n\n", "-"*10, "MAIN MENU", "-"*10)
        print("1. Add edge")
        print("2. Depth First Search (DFS)")
        print("3. Breadth First Search (BFS)")
        print("4. Exit")
        choice = int(input("Choose an option (1-4):\t"))
        print("-"*32)

        if choice == 1:
            total = int(input("\nTotal edges to add:\t"))
            for i in range(total):
              print(f"EDGE {i+1} ->")
              u = input(f"Enter first vertex for edge {i+1}: ")
              v = input(f"Enter second vertex for edge {i+1}: ")
              g.add_edge(u, v)
            print("\nVertices and its neighbours are:\t", g.graph)
        elif choice == 2:
            start = input("\nEnter starting vertex for DFS:\t")
            print("Depth First Search (DFS):\t")
            g.dfs(start)
        elif choice == 3:
            start = input("\nEnter starting vertex for BFS:\t")
            print("Breadth First Search (BFS):\t")
            g.bfs(start)
        elif choice == 4:
            print("\n## END OF CODE\n")
            break
        else:
            print("\nPlease choose a valid option.")

main()














# Sure! Here's a line-by-line detailed explanation of the code you've posted, which implements a graph and performs both DFS (Depth First Search) and BFS (Breadth First Search):

# 🔹 from collections import deque
# Imports deque, a double-ended queue from the collections module.

# deque is faster than lists for queue operations like append and popleft, which is useful in BFS.

# 🔹 class Graph:
# Defines a class called Graph to represent the graph data structure and its operations.

# 🔹 def __init__(self):
# python
# Copy
# Edit
#     self.graph = {}
# This is the constructor method.

# Initializes an empty dictionary self.graph to store the adjacency list of the graph.

# Each key is a node, and its value is a list of connected nodes (neighbors).

# 🔹 def add_edge(self, u, v):
# Adds an edge between nodes u and v.

# python
# Copy
# Edit
#     if u not in self.graph:
#         self.graph[u] = []
# If u is not already in the graph, initialize its list of neighbors.

# python
# Copy
# Edit
#     if v not in self.graph:
#         self.graph[v] = []
# Same for v.

# python
# Copy
# Edit
#     self.graph[u].append(v)
#     self.graph[v].append(u)
# Adds v to u’s neighbor list and u to v’s list — i.e., undirected edge.

# ✅ If the graph were directed, you'd remove the second line.

# 🔹 def dfs(self, start, visited=None):
# This defines the DFS traversal function.

# python
# Copy
# Edit
#     if visited is None:
#         visited = set()
# If no visited set is provided, initialize a new empty set.

# This tracks all visited nodes to avoid infinite recursion.

# python
# Copy
# Edit
#     visited.add(start)
#     print(start, end=" ")
# Mark the current node start as visited.

# Print it to show traversal order.

# python
# Copy
# Edit
#     for neighbour in self.graph.get(start, []):
#         if neighbour not in visited:
#             self.dfs(neighbour, visited)
# Iterate over each neighbor of the current node.

# If a neighbor hasn’t been visited, call dfs recursively on it.

# 🔹 def bfs(self, start):
# This defines the BFS traversal function.

# python
# Copy
# Edit
#     visited = set()
#     visited.add(start)
#     queue = deque([start])
# Initialize an empty set for visited nodes.

# Mark the starting node as visited.

# Use a deque to initialize the queue with the starting node.

# 🔹 Nested bfs_helper() function:
# python
# Copy
# Edit
#     def bfs_helper():
# Defines a helper function for recursion. This is a recursive BFS, which is unusual (typically BFS uses loops).

# python
# Copy
# Edit
#         if not queue:
#             return
# Base case: if the queue is empty, stop recursion.

# python
# Copy
# Edit
#         vertex = queue.popleft()
#         print(vertex, end=" ")
# Dequeue the next node, print it.

# python
# Copy
# Edit
#         for neighbour in self.graph.get(vertex, []):
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
# For each unvisited neighbor, mark as visited and enqueue it.

# python
# Copy
# Edit
#         bfs_helper()
# Recurse with updated queue until all reachable nodes are visited.

# 🔹 def main():
# Defines the main() function where you would create a graph and call its methods.

# python
# Copy
# Edit
#     g = Graph()
# Creates an instance of the Graph class.

# Let me know if you'd like me to add interactive input to build a graph and perform BFS/DFS.







# You said:
# give dry run 
# ChatGPT said:
# Sure! Let's do a dry run of the code you shared with a simple example.

# ✅ Suppose we run this in main():
# python
# Copy
# Edit
# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'E')
# g.add_edge('D', 'E')
# Graph looks like this:

# mathematica
# Copy
# Edit
#     A
#    / \
#   B   C
#   |   |
#   D---E
# ▶ DFS Dry Run: g.dfs('A')
# Initial call: dfs('A', visited=None)

# visited = {} → becomes {'A'}

# Prints A

# Neighbors of A: B, C

# Recurse on B:

# visited = {'A', 'B'}

# Prints B

# Neighbors of B: A, D

# A is visited, move to D

# Recurse on D:

# visited = {'A', 'B', 'D'}

# Prints D

# Neighbors of D: B, E

# B is visited, go to E

# Recurse on E:

# visited = {'A', 'B', 'D', 'E'}

# Prints E

# Neighbors of E: C, D → already visited

# Backtrack to B → Done
# Backtrack to A → Next neighbor is C

# Recurse on C:

# visited = {'A', 'B', 'C', 'D', 'E'}

# Prints C

# Neighbors: A, E → visited

# ✅ Final Output:

# mathematica
# Copy
# Edit
# A B D E C
# ▶ BFS Dry Run: g.bfs('A')
# Initialize:

# visited = {'A'}

# queue = deque(['A'])

# First call to bfs_helper:

# Pop A, print A

# Neighbors of A: B, C → mark visited, enqueue

# queue = deque(['B', 'C']), visited = {'A', 'B', 'C'}

# Next call:

# Pop B, print B

# Neighbors: A, D

# A visited, D not → enqueue

# queue = deque(['C', 'D']), visited = {'A', 'B', 'C', 'D'}

# Next call:

# Pop C, print C

# Neighbors: A, E

# A visited, E not → enqueue

# queue = deque(['D', 'E']), visited = {'A', 'B', 'C', 'D', 'E'}

# Next call:

# Pop D, print D

# Neighbors: B, E → both visited

# Next call:

# Pop E, print E

# Neighbors: C, D → both visited

# ✅ Final Output:

# mathematica
# Copy
# Edit
# A B C D E
# Would you like me to help you run this interactively or add input prompts for building a graph?

# Viva Questions and Answers:
# 1. What is the difference between DFS and BFS?
# DFS (Depth First Search) explores as far as possible along a branch before backtracking. It uses a stack (either explicitly or through recursion) to explore nodes.

# BFS (Breadth First Search) explores all the neighbors of a node before moving to the next level. It uses a queue to explore nodes level by level.

# 2. What data structure is used in DFS and BFS?
# DFS: A stack is used (either explicitly or implicitly through recursion).

# BFS: A queue is used to explore nodes level by level.

# 3. How does the recursive approach in DFS work?
# DFS starts at a node, marks it as visited, and recursively visits all unvisited neighbors, backtracking when necessary. This continues until all reachable nodes are visited.

# 4. What is the time complexity of DFS and BFS?
# DFS and BFS both have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.

# 5. Why is the visited set used in DFS and BFS?
# The visited set ensures that nodes are not revisited, preventing infinite loops in cyclic graphs and ensuring each node is processed only once.

# 6. How does the graph structure affect DFS and BFS?
# DFS: Can go deep into the graph along one branch, making it useful for pathfinding and solving puzzles.

# BFS: Explores level by level, which makes it ideal for finding the shortest path in unweighted graphs.

# 7. What is the role of recursion in DFS?
# Recursion allows DFS to explore nodes deeply without the need for an explicit stack. Each recursive call represents a deeper exploration of the graph.

# 8. Why is BFS unusual in the provided code with recursion?
# BFS is typically implemented using a queue and iteration, but in the provided code, BFS uses recursion by defining a bfs_helper function to mimic the iterative process.

# Space Complexity in Short:
# DFS (Depth First Search):

# Recursive: O(V) (due to recursion stack and visited nodes)

# Non-recursive: O(V) (due to the stack and visited nodes)

# BFS (Breadth First Search): O(V) (due to the queue and visited nodes)

# Where V is the number of vertices in the graph.

# Total edges to add:	6
# EDGE 1 ->
# Enter first vertex for edge 1: a
# Enter second vertex for edge 1: b
# EDGE 2 ->
# Enter first vertex for edge 2: a
# Enter second vertex for edge 2: c
# EDGE 3 ->
# Enter first vertex for edge 3: b
# Enter second vertex for edge 3: d
# EDGE 4 ->
# Enter first vertex for edge 4: c
# Enter second vertex for edge 4: e
# EDGE 5 ->
# Enter first vertex for edge 5: d
# Enter second vertex for edge 5: f
# EDGE 6 ->
# Enter first vertex for edge 6: e
# Enter second vertex for edge 6: g