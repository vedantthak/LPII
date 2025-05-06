class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # list of edges (u, v, weight)
        self.nodes = set()

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))
        self.nodes.add(u)
        self.nodes.add(v)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, xroot, yroot):
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        print("\n--- Kruskal's MST ---")
        result = []
        self.graph.sort()  # Sort by weight
        parent = {}
        rank = {}

        for node in self.nodes:
            parent[node] = node
            rank[node] = 0

        for weight, u, v in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        total_cost = sum([w for _, _, w in result])
        for u, v, w in result:
            print(f"{u} -- {v} = {w}")
        print("Total cost:", total_cost)

    def prim_mst(self, start):
        print("\n--- Prim's MST ---")
        import heapq
        visited = set()
        min_heap = [(0, start, None)]
        result = []
        total_cost = 0

        while min_heap:
            weight, u, prev = heapq.heappop(min_heap)
            if u not in visited:
                visited.add(u)
                if prev is not None:
                    result.append((prev, u, weight))
                    total_cost += weight

                for w, x, y in self.graph:
                    if x == u and y not in visited:
                        heapq.heappush(min_heap, (w, y, x))
                    elif y == u and x not in visited:
                        heapq.heappush(min_heap, (w, x, y))

        for u, v, w in result:
            print(f"{u} -- {v} = {w}")
        print("Total cost:", total_cost)

# Selection Sort Function
def selection_sort(arr):
    print("\n--- Selection Sort ---")
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

# Main Menu
def main():
    g = None
    while True:
        print("\n===== MENU =====")
        print("1. Input Graph for MST")
        print("2. Kruskal's MST")
        print("3. Prim's MST")
        print("4. Selection Sort")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            vertices = int(input("Enter number of vertices: "))
            edges = int(input("Enter number of edges: "))
            g = Graph(vertices)
            print("Enter edges (u v weight):")
            for _ in range(edges):
                u, v, w = input().split()
                g.add_edge(u, v, int(w))
            print("Graph input completed.")
        
        elif choice == '2':
            if g:
                g.kruskal_mst()
            else:
                print("Please input the graph first!")

        elif choice == '3':
            if g:
                start = input("Enter starting vertex for Prim's Algorithm: ")
                g.prim_mst(start)
            else:
                print("Please input the graph first!")

        elif choice == '4':
            arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
            selection_sort(arr)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()













# def prim(self):
#     selected = [False] * self.V  # Step 1: Initialize all vertices as not selected.
#     edge_count = 0  # Step 2: Count how many edges have been added to the MST (Minimum Spanning Tree).
#     selected[0] = True  # Step 3: Select the first vertex (0th vertex) to start from.
#     result = []  # Step 4: This will store the edges that form the MST.

#     # Step 5: Loop until we have V-1 edges in the MST (since a tree with V nodes has V-1 edges)
#     while edge_count < self.V - 1:
#         minimum = float('inf')  # Step 6: Initialize the minimum weight for the edge.
#         x = y = 0  # Step 7: Variables to store the vertices of the edge with the minimum weight.

#         # Step 8: Iterate through all vertices to find the edge with the minimum weight.
#         for i in range(self.V):
#             if selected[i]:  # Step 9: If the vertex `i` is already included in the MST
#                 # Step 10: Look at all possible vertices that can form an edge with vertex `i`.
#                 for j in range(self.V):
#                     if not selected[j] and self.adj_matrix[i][j]:  # Step 11: If vertex `j` is not selected, and there is an edge (i, j)
#                         if self.adj_matrix[i][j] < minimum:  # Step 12: Check if this edge has the minimum weight
#                             minimum = self.adj_matrix[i][j]  # Step 13: Update the minimum weight
#                             x, y = i, j  # Step 14: Store the edge (x, y) with the minimum weight.

#         result.append([x, y, self.adj_matrix[x][y]])  # Step 15: Add the edge with the minimum weight to the MST.
#         selected[y] = True  # Step 16: Mark vertex `y` as selected.
#         edge_count += 1  # Step 17: Increase the edge count by 1 since we added an edge to the MST.

#     # Step 18: Calculate the total cost of the MST.
#     total = sum([w for _, _, w in result])

#     # Step 19: Print the edges of the MST.
#     print("Edges in Prim's MST:")
#     for u, v, w in result:
#         print(f"{u} - {v}: {w}")

#     # Step 20: Print the total cost of the MST.
#     print("Total cost:", total)
# Detailed Explanation of Each Line:
# selected = [False] * self.V

# This initializes an array selected of size V (number of vertices) where each element is initially set to False. This array keeps track of which vertices are included in the Minimum Spanning Tree (MST). Initially, no vertex is included in the MST.

# edge_count = 0

# This variable tracks how many edges have been added to the MST. It starts at 0.

# selected[0] = True

# The first vertex (vertex 0) is always selected first to start the MST construction process.

# result = []

# This list stores the edges that are part of the MST. Each edge is represented as a list [u, v, w], where u and v are the connected vertices, and w is the weight of the edge.

# while edge_count < self.V - 1:

# The loop continues until the MST has V-1 edges, as a tree with V nodes must have exactly V-1 edges.

# minimum = float('inf')

# This variable stores the minimum weight of the edge that connects a selected vertex to a non-selected vertex. It is initially set to infinity.

# x = y = 0

# These variables will store the vertices x and y that form the edge with the minimum weight.

# for i in range(self.V):

# This loop iterates through all vertices in the graph.

# if selected[i]:

# If vertex i is already selected (i.e., it's part of the MST), we check all possible edges connected to i.

# for j in range(self.V):

# This inner loop checks all vertices j to see if there is an edge between i and j.

# if not selected[j] and self.adj_matrix[i][j]:

# This checks if vertex j is not selected yet and if there is an edge between vertices i and j (i.e., adj_matrix[i][j] is non-zero). If so, we consider the edge.

# if self.adj_matrix[i][j] < minimum:

# This compares the weight of the current edge (adj_matrix[i][j]) with the previously stored minimum weight.

# minimum = self.adj_matrix[i][j]

# If the current edge weight is less than the previous minimum, we update minimum to the current edge weight.

# x, y = i, j

# We store the vertices i and j that form the edge with the minimum weight.

# result.append([x, y, self.adj_matrix[x][y]])

# Once we find the edge with the minimum weight, we append it to the result list, which holds the edges of the MST.

# selected[y] = True

# Mark vertex y as selected, indicating that it is now part of the MST.

# edge_count += 1

# Increase the edge_count because we've added an edge to the MST.

# total = sum([w for _, _, w in result])

# This calculates the total weight of the MST by summing up the weights of all the edges in the result list.

# print("Edges in Prim's MST:")

# Print a header to indicate that the following lines will display the edges of the MST.

# for u, v, w in result:

# This loop iterates through all the edges in the MST and prints each edge in the format "u - v: w".

# print("Total cost:", total)

# Finally, the total cost of the MST is printed.

# Example:
# Let’s say we have a graph with 4 vertices and the following edges:

# makefile
# Copy
# Edit
# Vertices: 4
# Edges:
# 0-1: 10
# 0-2: 6
# 0-3: 5
# 1-3: 15
# 2-3: 4
# Prim’s Algorithm Process:

# Start with vertex 0. Mark it as selected.

# Find the minimum edge: 0-3 with weight 5. Add it to the MST.

# Now, the selected vertices are 0 and 3. Next, the minimum edge is 2-3 with weight 4. Add it to the MST.

# Now, the selected vertices are 0, 3, and 2. The minimum edge left is 0-2 with weight 6. Add it to the MST.

# The MST is complete, and the total cost is 5 + 4 + 6 = 15.

# The output will look something like:

# yaml
# Copy
# Edit
# Edges in Prim's MST:
# 0 - 3: 5
# 2 - 3: 4
# 0 - 2: 6
# Total cost: 15
# I hope this detailed explanation of Prim’s Algorithm helps! Let me know if you'd like further clarification.







# You said:
# give dry run


# ChatGPT said:
# Let's perform a dry run of Prim's Algorithm with the following graph as an example:

# Graph:
# Number of vertices: 4

# Edges with weights:

# 0 - 1: 10

# 0 - 2: 6

# 0 - 3: 5

# 1 - 3: 15

# 2 - 3: 4

# Initial Setup:
# V = 4 (Number of vertices)

# graph = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

# selected = [False, False, False, False] (Initially no vertices are selected)

# selected[0] = True (Start with vertex 0)

# edge_count = 0 (No edges in MST yet)

# result = [] (Empty result list to store edges in the MST)

# Step-by-Step Dry Run:
# First Iteration (edge_count = 0):
# Set minimum weight to infinity:
# minimum = inf, x = 0, y = 0

# Check neighbors of selected vertices (Starting from vertex 0):

# i = 0 (vertex 0 is selected).

# Check vertex j = 1: edge weight between 0 and 1 is 10 → minimum = 10, x = 0, y = 1.

# Check vertex j = 2: edge weight between 0 and 2 is 6 → minimum = 6, x = 0, y = 2.

# Check vertex j = 3: edge weight between 0 and 3 is 5 → minimum = 5, x = 0, y = 3.

# The minimum weight edge is between vertex 0 and vertex 3 with weight 5.

# Add the edge 0 - 3 with weight 5 to the MST:

# result = [(0, 3, 5)]

# Mark vertex 3 as selected: selected = [True, False, False, True]

# Increment edge count: edge_count = 1

# Second Iteration (edge_count = 1):
# Set minimum weight to infinity:
# minimum = inf, x = 0, y = 0

# Check neighbors of selected vertices (Vertices 0 and 3 are selected):

# i = 0 (vertex 0 is selected).

# Check vertex j = 1: edge weight between 0 and 1 is 10 → minimum = 10, x = 0, y = 1.

# Check vertex j = 2: edge weight between 0 and 2 is 6 → minimum = 6, x = 0, y = 2.

# i = 3 (vertex 3 is selected).

# Check vertex j = 1: edge weight between 3 and 1 is 15 → No update.

# Check vertex j = 2: edge weight between 3 and 2 is 4 → minimum = 4, x = 3, y = 2.

# The minimum weight edge is between vertex 3 and vertex 2 with weight 4.

# Add the edge 3 - 2 with weight 4 to the MST:

# result = [(0, 3, 5), (3, 2, 4)]

# Mark vertex 2 as selected: selected = [True, False, True, True]

# Increment edge count: edge_count = 2

# Third Iteration (edge_count = 2):
# Set minimum weight to infinity:
# minimum = inf, x = 0, y = 0

# Check neighbors of selected vertices (Vertices 0, 2, and 3 are selected):

# i = 0 (vertex 0 is selected).

# Check vertex j = 1: edge weight between 0 and 1 is 10 → minimum = 10, x = 0, y = 1.

# i = 2 (vertex 2 is selected).

# Check vertex j = 1: edge weight between 2 and 1 is not directly connected, so no update.

# i = 3 (vertex 3 is selected).

# Check vertex j = 1: edge weight between 3 and 1 is 15 → No update.

# The minimum weight edge is between vertex 0 and vertex 1 with weight 10.

# Add the edge 0 - 1 with weight 10 to the MST:

# result = [(0, 3, 5), (3, 2, 4), (0, 1, 10)]

# Mark vertex 1 as selected: selected = [True, True, True, True]

# Increment edge count: edge_count = 3

# Final Output:
# Now, the MST has 3 edges (V-1 = 4-1 = 3). The process terminates.

# MST Edges: (0, 3, 5), (3, 2, 4), (0, 1, 10)

# Total cost: 5 + 4 + 10 = 19

# Output:

# yaml
# Copy
# Edit
# Edges in Prim's MST:
# 0 - 3: 5
# 3 - 2: 4
# 0 - 1: 10
# Total cost: 19
# Summary of the Dry Run:
# Start with vertex 0 and select the minimum edge connected to it.

# After adding the first edge, select the next unselected vertex and find the minimum edge connecting it to the selected vertices.

# Repeat until we have V-1 edges in the MST.

# The algorithm always selects the edge with the minimum weight that connects a selected vertex to an unselected vertex.
































# Let’s go through your Kruskal's Algorithm implementation in Python line-by-line and explain each part in detail.

# ✅ CLASS AND CONSTRUCTOR
# python
# Copy
# Edit
# class Graph:
# This defines a new class named Graph. It will contain functions and data to represent a graph and perform Kruskal's algorithm.

# python
# Copy
# Edit
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = []
# __init__ is the constructor called when a new Graph object is created.

# self.V = vertices: Stores the number of vertices in the graph.

# self.graph = []: Initializes an empty list to store edges. Each edge will be stored as [u, v, w] (start vertex, end vertex, weight).

# ✅ ADDING EDGES
# python
# Copy
# Edit
#     def add_edge(self, u, v, w):
#         self.graph.append([u, v, w])
# Adds an edge to the graph.

# u: start vertex, v: end vertex, w: weight.

# Appends the edge as a list [u, v, w] to self.graph.

# ✅ UNION-FIND (CYCLE DETECTION)
# python
# Copy
# Edit
#     def find(self, parent, i):
#         if parent[i] == i:
#             return i
#         return self.find(parent, parent[i])
# This is a recursive function used in the Disjoint Set (Union-Find) data structure.

# Purpose: Find the root/representative of the set that contains i.

# If i is its own parent, return i; otherwise, recursively find its parent.

# python
# Copy
# Edit
#     def union(self, parent, rank, x, y):
#         xroot = self.find(parent, x)
#         yroot = self.find(parent, y)
# Find the root representatives of the sets that contain x and y.

# python
# Copy
# Edit
#         if rank[xroot] < rank[yroot]:
#             parent[xroot] = yroot
# If xroot has lower rank (depth of tree), attach it under yroot.

# python
# Copy
# Edit
#         elif rank[xroot] > rank[yroot]:
#             parent[yroot] = xroot
# If yroot has lower rank, attach it under xroot.

# python
# Copy
# Edit
#         else:
#             parent[yroot] = xroot
#             rank[xroot] += 1
# If both have equal rank, make one root and increment its rank.

# ✅ This method keeps the disjoint sets balanced, reducing the time complexity of future find() calls.

# ✅ KRUSKAL'S ALGORITHM
# python
# Copy
# Edit
#     def kruskal(self):
# Begins the Kruskal’s algorithm function.

# python
# Copy
# Edit
#         result = []
#         i, e = 0, 0
# result: list to store the edges of the final Minimum Spanning Tree (MST).

# i: index for iterating over sorted edges.

# e: count of edges added to MST.

# python
# Copy
# Edit
#         self.graph.sort(key=lambda item: item[2])
# Sorts all the edges in non-decreasing order of their weights using lambda item: item[2] as key.

# After sorting, we will try to add edges from smallest to largest weight.

# python
# Copy
# Edit
#         parent = []
#         rank = []
# parent: keeps track of parent of each vertex for union-find.

# rank: stores the depth of each tree to optimize union operation.

# python
# Copy
# Edit
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
# Initializes parent of each node as itself and rank as 0.

# ✅ MAIN LOOP (Build MST)
# python
# Copy
# Edit
#         while e < self.V - 1 and i < len(self.graph):
# Continue until we have V-1 edges in MST or we run out of edges.

# python
# Copy
# Edit
#             u, v, w = self.graph[i]
#             i += 1
# Pick the next edge from the sorted list.

# python
# Copy
# Edit
#             x = self.find(parent, u)
#             y = self.find(parent, v)
# Find the set representatives (roots) of u and v.

# python
# Copy
# Edit
#             if x != y:
# If adding this edge won’t form a cycle (i.e., u and v are in different sets)...

# python
# Copy
# Edit
#                 e += 1
#                 result.append([u, v, w])
#                 self.union(parent, rank, x, y)
# Add this edge to the MST.

# Union the sets to indicate that u and v are now connected.

# ✅ PRINT THE MST AND TOTAL COST
# python
# Copy
# Edit
#         total = sum([w for _, _, w in result])
# Calculates the total cost of the MST by summing up the weights of the edges in the result.

# python
# Copy
# Edit
#         print("Edges in Kruskal's MST:")
#         for u, v, w in result:
#             print(f"{u} - {v}: {w}")
#         print("Total cost:", total)
# Prints each edge in the MST.

# Displays the total cost.

# ✅ Summary:
# Time complexity:
# Sorting edges = O(E log E)
# Union-Find operations = near constant (O(α(V)))
# Overall: O(E log E)

# Space complexity:
# O(V + E) for parent, rank, and edge list.

# Would you like the same step-by-step explanation for the Prim’s algorithm as well?







# You said:
# give dry run
# ChatGPT said:
# Let’s perform a dry run of the Kruskal’s algorithm using your code with a small example:

# 🧪 Input Graph:
# Let’s say we have a graph with 4 vertices (0 to 3) and the following edges:

# Edge	Weight
# 0-1	10
# 0-2	6
# 0-3	5
# 1-3	15
# 2-3	4

# We’ll add these edges to the graph using:

# python
# Copy
# Edit
# g = Graph(4)
# g.add_edge(0, 1, 10)
# g.add_edge(0, 2, 6)
# g.add_edge(0, 3, 5)
# g.add_edge(1, 3, 15)
# g.add_edge(2, 3, 4)
# 🔁 Dry Run of kruskal():
# Step 1: Sort Edges by Weight
# After sorting, edges become:

# csharp
# Copy
# Edit
# [2, 3, 4]
# [0, 3, 5]
# [0, 2, 6]
# [0, 1, 10]
# [1, 3, 15]
# Step 2: Initialize parent = [0, 1, 2, 3], rank = [0, 0, 0, 0]
# 🔧 Iteration Details:
# ✅ i = 0 (Edge: 2–3, weight = 4)
# Find(2) → 2, Find(3) → 3 → different sets

# Add to result

# Union(2, 3) → parent[3] = 2, rank[2] = 1

# MST edges: [2–3]

# ✅ i = 1 (Edge: 0–3, weight = 5)
# Find(0) → 0, Find(3) → 2 (since parent[3] = 2)

# Add to result

# Union(0, 2) → parent[0] = 2, rank[2] = 1

# MST edges: [2–3], [0–3]

# ✅ i = 2 (Edge: 0–2, weight = 6)
# Find(0) → 2, Find(2) → 2 → same set

# Skip (would form a cycle)

# ✅ i = 3 (Edge: 0–1, weight = 10)
# Find(0) → 2, Find(1) → 1 → different sets

# Add to result

# Union(2, 1) → parent[1] = 2

# MST edges: [2–3], [0–3], [0–1]

# → Now we have 3 edges (V−1), so MST is complete.

# ✅ Final Output:
# plaintext
# Copy
# Edit
# Edges in Kruskal's MST:
# 2 - 3: 4
# 0 - 3: 5
# 0 - 1: 10
# Total cost: 19









# Example Input:
# Input Graph for MST:

# mathematica
# Copy
# Edit
# Enter number of vertices: 4
# Enter number of edges: 5
# Enter edges (u v weight):
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4
# Kruskal's MST:

# pgsql
# Copy
# Edit
# --- Kruskal's MST ---
# 2 -- 3 = 4
# 0 -- 3 = 5
# 0 -- 1 = 10
# Total cost: 19
# Prim's MST:

# pgsql
# Copy
# Edit
# Enter starting vertex for Prim's Algorithm: 0
# --- Prim's MST ---
# 0 -- 3 = 5
# 2 -- 3 = 4
# 0 -- 1 = 10
# Total cost: 19
# Selection Sort:

# mathematica
# Copy
# Edit
# Enter numbers to sort (space-separated): 4 3 5 1 2
# --- Selection Sort ---
# Sorted array: [1, 2, 3, 4, 5]
# Viva Questions and Answers:
# What is Kruskal’s algorithm used for?
# Answer: Kruskal’s algorithm is used to find the Minimum Spanning Tree (MST) of a graph by selecting edges in increasing order of weight and ensuring no cycles are formed.

# How does Kruskal’s algorithm avoid cycles?
# Answer: Kruskal’s algorithm uses a Union-Find (Disjoint-Set) data structure to check if two vertices are in the same set before adding an edge between them, thus preventing cycles.

# What is Prim’s algorithm used for?
# Answer: Prim’s algorithm is also used to find the Minimum Spanning Tree (MST) of a graph. It starts from an arbitrary vertex and grows the MST by adding the minimum weight edge connecting a vertex inside the MST to a vertex outside.

# What is the difference between Kruskal’s and Prim’s algorithms?
# Answer: Kruskal’s algorithm sorts all the edges and selects them one by one, while Prim’s algorithm expands the MST by choosing the smallest edge connecting a vertex already in the MST to a vertex outside.

# Explain the find function in Kruskal’s algorithm.
# Answer: The find function is used to find the root of a vertex in the Union-Find data structure. It helps in determining if two vertices belong to the same set or not.

# What is the time complexity of Kruskal’s algorithm?
# Answer: The time complexity of Kruskal’s algorithm is O(E log E), where E is the number of edges, due to sorting the edges and performing union-find operations.

# What is the time complexity of Prim’s algorithm?
# Answer: The time complexity of Prim’s algorithm is O(E log V), where V is the number of vertices and E is the number of edges, because it uses a priority queue (min-heap) to select edges.

# What is the role of the heap in Prim’s algorithm?
# Answer: The heap in Prim’s algorithm is used to efficiently select the edge with the minimum weight connecting a vertex in the MST to one outside the MST.

# What does the union function do in Kruskal’s algorithm?
# Answer: The union function connects two subsets in the Union-Find structure by making one root the parent of the other, ensuring the two sets are merged.

# How is the selection_sort algorithm implemented?
# Answer: The selection_sort algorithm works by finding the minimum element from the unsorted portion of the list and swapping it with the first unsorted element. This process repeats until the list is sorted.

# What is the time complexity of Selection Sort?
# Answer: The time complexity of Selection Sort is O(n^2), where n is the number of elements in the array, as it uses two nested loops to find the minimum element for each iteration.

# What is the space complexity of Kruskal’s and Prim’s algorithms?
# Answer: Both Kruskal’s and Prim’s algorithms have a space complexity of O(V + E), where V is the number of vertices and E is the number of edges, because they require storing the graph and auxiliary structures like the Union-Find or priority queue.

# How does Prim’s algorithm handle disconnected graphs?
# Answer: Prim’s algorithm requires the graph to be connected, as it starts from a vertex and gradually adds edges to form the MST. If the graph is disconnected, Prim’s algorithm will only produce a spanning tree for the connected component containing the starting vertex.

# What happens if you input a graph with negative edge weights in Kruskal’s or Prim’s algorithm?
# Answer: Both Kruskal’s and Prim’s algorithms can handle negative edge weights as long as the graph is undirected and there are no negative weight cycles. They still find the minimum spanning tree based on the smallest weight edges.