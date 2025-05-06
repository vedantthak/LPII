def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist.")
        return False
    print("Solution exists: The assigned colors are:")
    print(color)
    return True

def main():
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of colors: "))
    e = int(input("Enter number of edges: "))

    # Initialize adjacency list
    graph = [[] for _ in range(n)]

    print("Enter edges (u v) one per line:")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # since the graph is undirected

    graph_coloring(graph, m)

if __name__ == "__main__":
    main()













# explain each line of code in detail line by line
# ChatGPT said:
# Absolutely! Here's a detailed, line-by-line explanation of the user-input version of the Graph Coloring program in Python.

# 📌 Function: is_safe(node, graph, color, c)
# python
# Copy
# Edit
# def is_safe(node, graph, color, c):
# Purpose: Check if color c can be assigned to vertex node without causing a conflict (i.e., without assigning the same color to an adjacent node).

# Parameters:

# node: the current vertex being colored

# graph: adjacency list of the graph

# color: list tracking assigned colors for all nodes

# c: color we are trying to assign to the current node

# python
# Copy
# Edit
#     for neighbor in graph[node]:
# Loop through all adjacent nodes (neighbors) of the current node.

# python
# Copy
# Edit
#         if color[neighbor] == c:
#             return False
# If any neighbor already has the color c, return False (not safe to assign this color).

# python
# Copy
# Edit
#     return True
# If no neighbors have color c, it's safe to assign it — return True.

# 📌 Function: graph_coloring_util(graph, m, color, node)
# python
# Copy
# Edit
# def graph_coloring_util(graph, m, color, node):
# Recursive backtracking function to try coloring each node.

# python
# Copy
# Edit
#     if node == len(graph):
#         return True
# Base case: If all nodes are colored, return True to indicate success.

# python
# Copy
# Edit
#     for c in range(1, m + 1):
# Try all possible colors 1 to m for the current node.

# python
# Copy
# Edit
#         if is_safe(node, graph, color, c):
# Check if the current color c is safe for this node.

# python
# Copy
# Edit
#             color[node] = c
# Assign color c to the node.

# python
# Copy
# Edit
#             if graph_coloring_util(graph, m, color, node + 1):
#                 return True
# Recursively try to color the rest of the graph.

# If successful, return True.

# python
# Copy
# Edit
#             color[node] = 0  # Backtrack
# If recursion fails, remove the color (reset to 0) and try next color.

# python
# Copy
# Edit
#     return False
# If none of the colors worked, return False to trigger backtracking.

# 📌 Function: graph_coloring(graph, m)
# python
# Copy
# Edit
# def graph_coloring(graph, m):
# Main function to start the coloring process.

# python
# Copy
# Edit
#     n = len(graph)
# Number of vertices in the graph.

# python
# Copy
# Edit
#     color = [0] * n
# Initialize color list with 0 (meaning no color assigned yet).

# python
# Copy
# Edit
#     if not graph_coloring_util(graph, m, color, 0):
# Start coloring from node 0 using the utility function.

# python
# Copy
# Edit
#         print("Solution does not exist.")
#         return False
# If coloring failed, print message and return.

# python
# Copy
# Edit
#     print("Solution exists: The assigned colors are:")
#     print(color)
#     return True
# If successful, print the list of colors for each vertex.

# 📌 Function: main()
# python
# Copy
# Edit
# def main():
# Function to get input from the user.

# python
# Copy
# Edit
#     n = int(input("Enter number of vertices: "))
#     m = int(input("Enter number of colors: "))
#     e = int(input("Enter number of edges: "))
# Read number of vertices, colors, and edges.

# python
# Copy
# Edit
#     graph = [[] for _ in range(n)]
# Initialize an empty adjacency list for each vertex.

# python
# Copy
# Edit
#     print("Enter edges (u v) one per line:")
# Prompt user to input the edges.

# python
# Copy
# Edit
#     for _ in range(e):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)  # since the graph is undirected
# For each edge, read two vertices and update the adjacency list for both directions (undirected).

# python
# Copy
# Edit
#     graph_coloring(graph, m)
# Call the main coloring function with the built graph and color count.

# 📌 Program Entry Point
# python
# Copy
# Edit
# if __name__ == "__main__":
#     main()
# Standard Python idiom: ensures main() runs only when the script is executed directly, not when imported as a module.

# Would you like me to show how to visualize the colored graph using a library like matplotlib or networkx?


















# give dry run

# ChatGPT said:
# Absolutely! Let's walk through a dry run of the graph coloring code with a simple example to see how it works step by step.

# 🧠 Sample Input:
# Let's assume the user enters:

# yaml
# Copy
# Edit
# Enter number of vertices: 4
# Enter number of colors: 3
# Enter number of edges: 5
# Enter edges (u v) one per line:
# 0 1
# 0 2
# 0 3
# 1 2
# 2 3
# This creates the following undirected graph:

# lua
# Copy
# Edit
#      0
#    / | \
#   1--2--3
# And we are allowed to use 3 colors.

# 🧮 Internal Representation:
# The adjacency list will look like:

# python
# Copy
# Edit
# graph = [
#     [1, 2, 3],  # Node 0 is connected to 1, 2, 3
#     [0, 2],     # Node 1 is connected to 0 and 2
#     [0, 1, 3],  # Node 2 is connected to 0, 1, 3
#     [0, 2]      # Node 3 is connected to 0 and 2
# ]
# Color array (initially):

# python
# Copy
# Edit
# color = [0, 0, 0, 0]
# 🪜 Dry Run (Backtracking):
# Start at node = 0

# Try color 1 → it's safe → assign: color = [1, 0, 0, 0]

# Move to node = 1

# color 1 → not safe (node 1 connected to 0 which is color 1)

# Try color 2 → safe → assign: color = [1, 2, 0, 0]

# Move to node = 2

# color 1 → not safe (connected to 0)

# color 2 → not safe (connected to 1)

# color 3 → safe → assign: color = [1, 2, 3, 0]

# Move to node = 3

# color 1 → not safe (connected to 0)

# color 2 → safe → assign: color = [1, 2, 3, 2]

# ✅ All nodes colored successfully with no conflicts.

# 🖨️ Output:
# sql
# Copy
# Edit
# Solution exists: The assigned colors are:
# [1, 2, 3, 2]
# This means:

# Vertex 0 → color 1

# Vertex 1 → color 2

# Vertex 2 → color 3

# Vertex 3 → color 2

# No adjacent nodes share the same color — ✅ valid coloring.






# Example Input and Output
# Input:
# yaml
# Copy
# Edit
# Enter number of vertices: 4
# Enter number of colors: 3
# Enter number of edges: 4
# Enter edges (u v) one per line:
# 0 1
# 0 2
# 1 2
# 2 3
# Output:
# sql
# Copy
# Edit
# Solution exists: The assigned colors are:
# [1, 2, 3, 2]
# Viva Questions and Answers
# What is the purpose of the is_safe function?

# The is_safe function checks whether it is safe to color a node with a particular color by ensuring that none of its neighbors have the same color.

# What is the role of backtracking in this code?

# Backtracking is used to explore all possible color assignments. If a valid coloring is not possible with a given color, the algorithm undoes the assignment and tries the next possibility.

# What happens if a solution does not exist?

# If no valid coloring can be found, the program prints "Solution does not exist."

# What is the input format for this program?

# The program accepts the number of vertices, the number of colors, and the edges of the graph. Each edge is represented by two integers, denoting an edge between two vertices.

# How does the program determine whether a solution exists?

# The program uses backtracking to try all possible colorings of the graph. If a valid coloring is found, the program prints the assigned colors; otherwise, it concludes that no solution exists.

# Can this program work for any graph?

# The program can work for any graph, but it will only work if the number of colors provided (m) is sufficient to color the graph without two adjacent nodes sharing the same color. If m is too small, the solution might not exist.

# What does the graph_coloring_util function do?

# The graph_coloring_util function is a recursive function that tries to assign colors to each vertex, checking if it is safe to do so. If it encounters a conflict, it backtracks and tries a different color.

# What is the role of the color array?

# The color array holds the current color assigned to each vertex. A 0 indicates that a vertex has not been colored yet.

# What is the worst-case time complexity of this algorithm?

# The worst-case time complexity is O(m^n), where m is the number of colors and n is the number of vertices. This is because for each vertex, the algorithm may try all m colors, leading to an exponential growth of possibilities.

# How would you improve the efficiency of this algorithm?

# To improve efficiency, heuristics like choosing the next node with the most constraints or using more advanced algorithms (such as greedy algorithms) could reduce the number of recursive calls.