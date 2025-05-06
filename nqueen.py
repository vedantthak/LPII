def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur, solutions, n):
    if i == n:
        solutions.append(cur[:])  
        return

    for j in range(n):
        if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
            continue

        cols[j] = 1
        rightDiagonal[i + j] = 1
        leftDiagonal[i - j + n - 1] = 1
        cur.append(j)

        placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur, solutions, n)

        cur.pop()
        cols[j] = 0
        rightDiagonal[i + j] = 0
        leftDiagonal[i - j + n - 1] = 0


def nQueen(n):
    cols = [0] * n
    leftDiagonal = [0] * (2 * n)
    rightDiagonal = [0] * (2 * n)
    cur = []
    solutions = []

    placeQueens(0, cols, leftDiagonal, rightDiagonal, cur, solutions, n)
    return solutions


def printBoards(solutions, n):
    if not solutions:
        print("No solution exists.")
        return

    print(f"Total Solutions: {len(solutions)}\n")
    for index, sol in enumerate(solutions):
        print(f"Solution {index + 1}:")
        board = [['.'] * n for _ in range(n)]
        for row in range(n):
            board[row][sol[row]] = 'Q'
            print(" ".join(board[row]))
        print()


if __name__ == "__main__":
    n = int(input("Enter the number of queens:\t"))
    solutions = nQueen(n)
    printBoards(solutions, n)


# Explanation of Code (Line by Line):
# This program solves the N-Queens problem using backtracking and prints all possible solutions for placing n queens on an n x n chessboard such that no two queens attack each other.

# Function: placeQueens
# python
# Copy
# Edit
# def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur, solutions, n):
# Parameters:

# i: The current row number (i.e., which queen to place next).

# cols: A list of length n to keep track of columns that are already occupied by queens (1 means a queen is placed in that column).

# leftDiagonal: A list to track left diagonals occupied by queens.

# rightDiagonal: A list to track right diagonals occupied by queens.

# cur: A list representing the current configuration of queens. Each element in cur represents the column position of the queen in that row.

# solutions: A list to store all valid board configurations (solutions).

# n: The size of the chessboard (number of rows and columns).

# python
# Copy
# Edit
#     if i == n:
#         solutions.append(cur[:])
#         return
# This checks if i == n, meaning all queens have been placed. If so, it appends the current configuration cur to the solutions list and returns.

# python
# Copy
# Edit
#     for j in range(n):
# This loop iterates over each column (j) in the current row (i).

# python
# Copy
# Edit
#         if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
#             continue
# This checks if placing a queen in column j is valid:

# cols[j]: If column j is already occupied (1).

# rightDiagonal[i + j]: If the right diagonal (with an index i + j) is already occupied.

# leftDiagonal[i - j + n - 1]: If the left diagonal (with an index i - j + n - 1) is already occupied.

# If any of these conditions are True, it means placing a queen at (i, j) would cause a conflict, so we skip this column (continue).

# python
# Copy
# Edit
#         cols[j] = 1
#         rightDiagonal[i + j] = 1
#         leftDiagonal[i - j + n - 1] = 1
# If it's safe to place the queen, mark column j and the diagonals as occupied.

# python
# Copy
# Edit
#         cur.append(j)
# Add column j to the cur list, representing the current row where the queen is placed.

# python
# Copy
# Edit
#         placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur, solutions, n)
# Call placeQueens recursively to place the queen in the next row (i + 1).

# python
# Copy
# Edit
#         cur.pop()
# Backtrack: remove the queen from the current row (undo the choice made earlier) and try another column in the current row.

# python
# Copy
# Edit
#         cols[j] = 0
#         rightDiagonal[i + j] = 0
#         leftDiagonal[i - j + n - 1] = 0
# Backtrack further by marking column j and the diagonals as unoccupied, allowing for the exploration of other possibilities.

# Function: nQueen
# python
# Copy
# Edit
# def nQueen(n):
# This function solves the N-Queens problem by calling placeQueens and collecting all solutions.

# python
# Copy
# Edit
#     cols = [0] * n
#     leftDiagonal = [0] * (2 * n)
#     rightDiagonal = [0] * (2 * n)
#     cur = []
#     solutions = []
# Initialize:

# cols: A list of size n initialized to 0 (all columns are initially unoccupied).

# leftDiagonal and rightDiagonal: Both lists of size 2 * n initialized to 0 to track occupied diagonals.

# cur: An empty list to track the current configuration of queens.

# solutions: An empty list to store valid solutions.

# python
# Copy
# Edit
#     placeQueens(0, cols, leftDiagonal, rightDiagonal, cur, solutions, n)
# Start placing queens from the first row (i = 0), and call placeQueens to explore all possible solutions.

# python
# Copy
# Edit
#     return solutions
# Return the list of all solutions found by placeQueens.

# Function: printBoards
# python
# Copy
# Edit
# def printBoards(solutions, n):
# This function prints the solutions in a readable chessboard format.

# python
# Copy
# Edit
#     if not solutions:
#         print("No solution exists.")
#         return
# If no solutions exist (i.e., solutions is empty), print a message indicating no solution and return.

# python
# Copy
# Edit
#     print(f"Total Solutions: {len(solutions)}\n")
# Print the total number of solutions found.

# python
# Copy
# Edit
#     for index, sol in enumerate(solutions):
#         print(f"Solution {index + 1}:")
#         board = [['.'] * n for _ in range(n)]
# For each solution in solutions, create an empty n x n board (represented as a 2D list of . characters).

# python
# Copy
# Edit
#         for row in range(n):
#             board[row][sol[row]] = 'Q'
#             print(" ".join(board[row]))
#         print()
# For each row in the solution, place a queen ('Q') at the appropriate column (sol[row]).

# Print the board row by row.

# Main Program
# python
# Copy
# Edit
# if __name__ == "__main__":
#     n = int(input("Enter the number of queens:\t"))
#     solutions = nQueen(n)
#     printBoards(solutions, n)
# The main program asks for the number of queens (n), calls nQueen(n) to find all solutions, and then prints them using printBoards(solutions, n).

# Example Execution:
# For n = 4, the output would look like:

# less
# Copy
# Edit
# Enter the number of queens: 4

# Total Solutions: 2

# Solution 1:
# . . Q .
# Q . . .
# . . . Q
# . Q . .

# Solution 2:
# . Q . .
# . . . Q
# Q . . .
# . . Q .
# Explanation of the Backtracking Approach:
# The program tries placing queens row by row.

# For each row, it attempts to place a queen in each column and checks for conflicts with previously placed queens (using cols, leftDiagonal, and rightDiagonal).

# If a conflict-free position is found, it places the queen and moves to the next row recursively.

# When a solution is found (i.e., all queens are placed), the current configuration is stored in solutions.

# The program uses backtracking by removing queens and marking columns and diagonals as unoccupied when it backtracks.






# You said:
# give example input and output and viva ques and ans in short 
# ChatGPT said:
# Example Input and Output:
# Input:
# typescript
# Copy
# Edit
# Enter the number of queens: 4
# Output:
# less
# Copy
# Edit
# Total Solutions: 2

# Solution 1:
# . . Q .
# Q . . .
# . . . Q
# . Q . .

# Solution 2:
# . Q . .
# . . . Q
# Q . . .
# . . Q .
# Viva Questions and Answers:
# Question: What is the N-Queens problem?

# Answer: The N-Queens problem is a classic problem in computer science where you are tasked with placing n queens on an n x n chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

# Question: How does the backtracking approach work in solving the N-Queens problem?

# Answer: The backtracking approach tries placing a queen in each row one by one, checking if it is safe to place the queen in a particular column. If placing a queen leads to a conflict (same column or diagonal), it backtracks and tries the next possible column. This process continues until a solution is found or all possibilities are exhausted.

# Question: Why do you use arrays like cols, leftDiagonal, and rightDiagonal?

# Answer: These arrays are used to track whether a column or diagonal is already occupied by a queen. They help quickly check if placing a queen at a specific position would cause a conflict, ensuring that the program runs efficiently.

# Question: What does the placeQueens function do?

# Answer: The placeQueens function is a recursive function that attempts to place queens row by row. It checks if it's safe to place a queen in each column and recursively places queens in subsequent rows. If a solution is found (all queens placed without conflicts), the configuration is stored.

# Question: What is the purpose of the cur list in the code?

# Answer: The cur list keeps track of the current configuration of queens, where each element represents the column of a queen in a specific row. This configuration is stored when a valid solution is found.

# Question: How does the printBoards function work?

# Answer: The printBoards function takes the list of solutions and prints each board configuration. For each solution, it constructs a chessboard and places queens at their respective positions (represented by 'Q').

# Question: How does the program backtrack?

# Answer: The program backtracks by removing a queen from the current row (cur.pop()), resetting the corresponding column and diagonals as unoccupied, and trying the next column in that row.

# Question: What happens if no solution is found?

# Answer: If no solution is found (i.e., if solutions is empty), the program prints "No solution exists."

# Question: What is the time complexity of this algorithm?

# Answer: The time complexity of this backtracking solution is O(n!), where n is the number of queens. This is because, in the worst case, the algorithm tries all possible configurations of queens on the board.

# Question: Can this algorithm be used for very large values of n?

# Answer: For very large values of n, this algorithm becomes inefficient because the number of possible solutions grows factorially (O(n!)). More advanced techniques or optimizations might be necessary for large values of n.