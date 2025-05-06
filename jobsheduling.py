"""
Assignment-A3

Problem Statement: Implement Greedy search algorithm for any of the following application:
    I. Selection Sort
    IV. Job Scheduling Problem
"""

# BEGINNING OF SELECTION SORT
numbers = [] # Empty list to store numbers

# Function to take input for numbers
def input_numbers():
        total = int(input("\nHow many numbers you wish to enter?\nTotal numbers:\t"))
        for i in range(total):
                val = float(input(f"Enter number {i+1}:\t"))
                numbers.append(val)
        print("\nNumbers you've entered are:\t", numbers)

# Function for selection sort
def selection_sort():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i] # Swapping
    print("Numbers sorted in ascending order using selection sort:\t", numbers)
# END OF SELECTION SORT

# BEGINNING OF JOB SCHEDULING
def job_scheduling():
    jobs = []
    total = int(input("Total jobs to add:\t"))

    # Take input for jobs
    print("\n", "-"*10, "JOBS", "-"*10, "\n")
    for i in range(total):
        print(f"JOB {i+1} ->")
        job_id = int(input(f"ID for job {i+1}:\t\t"))
        deadline = int(input(f"Deadline for job {i+1}:\t"))
        profit = int(input(f"Profit for job {i+1}:\t"))
        jobs.append((job_id, deadline, profit)) # Index 0 for job_id; Index 1 for deadline; Index 2 for profit
    print(f"\nAdded {total} jobs.")
    print("-"*27, "\n")

    # Initialize
    jobs.sort(key=lambda x: x[2], reverse=True) # Sort jobs by profit; Using index 2 to access profit
    max_deadline = max(job[1] for job in jobs) # Highest deadline; Using index 1 to access deadline
    slots = [0] * (max_deadline + 1)
    total_profit = 0

    # Scheduling jobs using greedy strategy
    for job in jobs:
        for i in range(job[1], 0, -1):
            if slots[i] == 0:
                slots[i] = job[0]
                total_profit += job[2]
                break

    # Print scheduled jobs
    print("Scheduled Jobs:", end=" ")
    for i in range(1, len(slots)):
        if slots[i] != 0:
            print(slots[i], end=" ")

    print(f"\nTotal Profit: {total_profit}")
# END OF JOB SCHEDULING


# Main function for menu
def main():
  while True:
    print("\n\n", "-"*10, "MAIN MENU", "-"*10)
    print("1. Selection Sort")
    print("2. Job Scheduling")
    print("3. Exit")
    choice = int(input("Choose an option (1-3):\t"))
    print("-"*32)

    if (choice == 1):
      input_numbers()
      selection_sort()
    elif (choice == 2):
      job_scheduling()
    elif (choice == 3):
      print("\n## END OF CODE\n")
      break
    else:
      print("\nPlease choose a valid option (1-3)")

main()



















# Explanation of Code Line by Line
# Let's break down each part of the code and explain what it does in detail.

# Selection Sort Part
# python
# Copy
# Edit
# numbers = []  # Empty list to store numbers
# Initializes an empty list numbers where we will store the numbers to be sorted.

# Input Function:
# python
# Copy
# Edit
# def input_numbers():
#         total = int(input("\nHow many numbers you wish to enter?\nTotal numbers:\t"))
#         for i in range(total):
#                 val = float(input(f"Enter number {i+1}:\t"))
#                 numbers.append(val)
#         print("\nNumbers you've entered are:\t", numbers)
# input_numbers() asks the user how many numbers they want to enter.

# total is the number of values the user will input.

# Then, for each of those values, it prompts the user to input a number and adds it to the numbers list using the append() method.

# Selection Sort Function:
# python
# Copy
# Edit
# def selection_sort():
#     for i in range(len(numbers)):  # Iterate through the entire list
#         min_index = i  # Assume the current element is the smallest
#         for j in range(i+1, len(numbers)):  # Compare with all other elements to the right
#             if numbers[j] < numbers[min_index]:  # If a smaller element is found
#                 min_index = j  # Update the index of the smallest element
#         numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # Swap the elements
#     print("Numbers sorted in ascending order using selection sort:\t", numbers)
# The selection_sort() function sorts the list numbers in ascending order using the selection sort algorithm.

# The outer loop iterates through the list, and for each index i, it assumes that the element at index i is the smallest.

# The inner loop finds the smallest element after index i and swaps it with the element at index i.

# Finally, the sorted list is printed.

# Job Scheduling Part (Greedy Algorithm)
# Job Scheduling Function:
# python
# Copy
# Edit
# def job_scheduling():
#     jobs = []  # List to store jobs with job_id, deadline, profit
#     total = int(input("Total jobs to add:\t"))  # User input for number of jobs
# jobs is an empty list that will store tuples representing each job, which includes the job's ID, deadline, and profit.

# total stores the number of jobs that the user wants to input.

# Input for Jobs:
# python
# Copy
# Edit
#     print("\n", "-"*10, "JOBS", "-"*10, "\n")
#     for i in range(total):
#         print(f"JOB {i+1} ->")
#         job_id = int(input(f"ID for job {i+1}:\t\t"))
#         deadline = int(input(f"Deadline for job {i+1}:\t"))
#         profit = int(input(f"Profit for job {i+1}:\t"))
#         jobs.append((job_id, deadline, profit))  # Store job details as a tuple (ID, deadline, profit)
#     print(f"\nAdded {total} jobs.")
#     print("-"*27, "\n")
# This block asks the user to input job details (ID, deadline, and profit) for each job.

# Each job is stored as a tuple (job_id, deadline, profit) in the jobs list.

# Greedy Job Scheduling Algorithm:
# python
# Copy
# Edit
#     jobs.sort(key=lambda x: x[2], reverse=True)  # Sort jobs by profit in descending order
#     max_deadline = max(job[1] for job in jobs)  # Find the highest deadline
#     slots = [0] * (max_deadline + 1)  # Create slots (array) to keep track of scheduled jobs
#     total_profit = 0  # Initialize total profit to zero
# The jobs list is sorted by profit in descending order using a lambda function that sorts by the third element (profit) of the tuple.

# max_deadline finds the highest deadline across all jobs.

# slots is a list initialized with zeros. The length of slots is equal to the highest deadline, and each slot will represent a time slot where a job can be scheduled.

# total_profit starts at zero and will accumulate the total profit from the scheduled jobs.

# Job Scheduling Loop:
# python
# Copy
# Edit
#     for job in jobs:  # Iterate through each job
#         for i in range(job[1], 0, -1):  # Try to schedule the job at its deadline or earlier
#             if slots[i] == 0:  # Check if slot is empty
#                 slots[i] = job[0]  # Schedule the job at this slot (using job ID)
#                 total_profit += job[2]  # Add job profit to total profit
#                 break  # Exit the loop once the job is scheduled
# This nested loop schedules jobs. For each job, it tries to schedule the job at its deadline or earlier by iterating backwards from its deadline.

# If a slot is available (slots[i] == 0), the job is scheduled there, and the profit is added to total_profit.

# Output the Scheduled Jobs and Total Profit:
# python
# Copy
# Edit
#     print("Scheduled Jobs:", end=" ")
#     for i in range(1, len(slots)):
#         if slots[i] != 0:
#             print(slots[i], end=" ")  # Print the IDs of scheduled jobs

#     print(f"\nTotal Profit: {total_profit}")
# After the loop completes, it prints the job IDs that were scheduled (those jobs that are assigned to non-zero slots).

# The total profit is printed.

# Main Menu
# python
# Copy
# Edit
# def main():
#     while True:  # Infinite loop to keep showing the menu
#         print("\n\n", "-"*10, "MAIN MENU", "-"*10)
#         print("1. Selection Sort")
#         print("2. Job Scheduling")
#         print("3. Exit")
#         choice = int(input("Choose an option (1-3):\t"))  # Ask user for their choice
#         print("-"*32)
# This main() function continuously displays the menu until the user chooses to exit.

# The user is asked to select an option: either selection sort, job scheduling, or exit.

# Choice Handling:
# python
# Copy
# Edit
#         if (choice == 1):
#             input_numbers()  # Take input for numbers
#             selection_sort()  # Perform selection sort and print the result
#         elif (choice == 2):
#             job_scheduling()  # Perform job scheduling and print the result
#         elif (choice == 3):
#             print("\n## END OF CODE\n")  # Exit message
#             break  # Exit the loop
#         else:
#             print("\nPlease choose a valid option (1-3)")  # Handle invalid inputs
# If the user selects 1, the program will ask for numbers, then perform and display the result of selection sort.

# If the user selects 2, the program will ask for job details and schedule the jobs, then display the result.

# If the user selects 3, the program prints "END OF CODE" and exits the loop.

# Dry Run Example
# Input 1: Selection Sort
# yaml
# Copy
# Edit
# Choose an option (1-3): 1
# How many numbers you wish to enter?
# Total numbers: 5
# Enter number 1: 34.5
# Enter number 2: 10.3
# Enter number 3: 78.9
# Enter number 4: 23.4
# Enter number 5: 56.7

# Numbers you've entered are: [34.5, 10.3, 78.9, 23.4, 56.7]
# Numbers sorted in ascending order using selection sort: [10.3, 23.4, 34.5, 56.7, 78.9]
# Input 2: Job Scheduling
# rust
# Copy
# Edit
# Choose an option (1-3): 2
# Total jobs to add: 3

# ---------- JOBS ----------
# JOB 1 ->
# ID for job 1:     1
# Deadline for job 1:  2
# Profit for job 1:   50
# JOB 2 ->
# ID for job 2:     2
# Deadline for job 2:  1
# Profit for job 2:   60
# JOB 3 ->
# ID for job 3:     3
# Deadline for job 3:  3
# Profit for job 3:   70

# Added 3 jobs.
# ---------------------------

# Scheduled Jobs: 2 1 3 
# Total Profit: 180
# Input 3: Exit
# shell
# Copy
# Edit
# Choose an option (1-3): 3
# ## END OF CODE
# This is how the code functions. Let me know if you'd like further details!







# You said:
# give dry run by code


# ChatGPT said:
# Dry Run Output:
# 1. Selection Sort
# Input Numbers: [34.5, 10.3, 78.9, 23.4, 56.7]

# After applying Selection Sort, the numbers are sorted in ascending order:
# Sorted Numbers: [10.3, 23.4, 34.5, 56.7, 78.9]

# 2. Job Scheduling
# Jobs:

# Job 1: (Job ID: 1, Deadline: 2, Profit: 50)

# Job 2: (Job ID: 2, Deadline: 1, Profit: 60)

# Job 3: (Job ID: 3, Deadline: 3, Profit: 70)

# Job Sorting by Profit (Descending Order):
# Jobs after sorting:

# Job 2 (Profit: 60)

# Job 3 (Profit: 70)

# Job 1 (Profit: 50)

# Scheduling Process:

# Slot 3: Job 3 (Profit 70, Deadline 3) is scheduled.

# Slot 1: Job 2 (Profit 60, Deadline 1) is scheduled.

# Slot 2: Job 1 (Profit 50, Deadline 2) is scheduled.

# Scheduled Jobs: 2, 1, 3

# Total Profit: 180

# This confirms the correct working of both Selection Sort and the Job Scheduling algorithm with the given input. 






# Example Input and Output
# Input for Selection Sort:
# yaml
# Copy
# Edit
# How many numbers you wish to enter?
# Total numbers: 5
# Enter number 1: 12.5
# Enter number 2: 3.8
# Enter number 3: 9.1
# Enter number 4: 5.7
# Enter number 5: 7.4
# Output for Selection Sort:
# vbnet
# Copy
# Edit
# Numbers you've entered are: [12.5, 3.8, 9.1, 5.7, 7.4]
# Numbers sorted in ascending order using selection sort: [3.8, 5.7, 7.4, 9.1, 12.5]
# Input for Job Scheduling:
# rust
# Copy
# Edit
# Total jobs to add: 3

# ---------- JOBS ----------
# JOB 1 ->
# ID for job 1: 1
# Deadline for job 1: 2
# Profit for job 1: 50

# JOB 2 ->
# ID for job 2: 2
# Deadline for job 2: 1
# Profit for job 2: 40

# JOB 3 ->
# ID for job 3: 3
# Deadline for job 3: 2
# Profit for job 3: 70
# Output for Job Scheduling:
# yaml
# Copy
# Edit
# Added 3 jobs.
# --------------------------- 

# Scheduled Jobs: 3 1 
# Total Profit: 120
# Viva Questions and Answers
# What is Selection Sort, and how does it work in the provided code?

# Selection Sort is a simple sorting algorithm. It works by selecting the smallest element from the unsorted part of the array and placing it at the beginning of the sorted part. The code iterates over the list and swaps the minimum element found with the current element.

# What is the purpose of the job_scheduling function?

# The job_scheduling function schedules jobs based on profit and deadlines using a greedy approach. It sorts jobs by profit in descending order and assigns them to the latest possible slot before the job's deadline to maximize profit.

# What happens when you enter jobs with overlapping deadlines?

# The program ensures that jobs are scheduled in such a way that no two jobs overlap by placing each job in the latest available slot before its deadline. It maximizes the profit by prioritizing high-profit jobs.

# What does the slots array represent in job scheduling?

# The slots array represents the available time slots for scheduling jobs. Each slot corresponds to a time unit, and a job is placed in the latest available slot that is before or on its deadline.

# How does the greedy strategy apply to job scheduling?

# The greedy strategy in job scheduling selects jobs with the highest profit and attempts to schedule them in the latest available time slot before the job's deadline. This ensures maximum profit while preventing overlapping job schedules.

# What is the time complexity of the selection sort algorithm?

# The time complexity of selection sort is 
# 𝑂
# (
# 𝑛
# 2
# )
# O(n 
# 2
#  ), where 
# 𝑛
# n is the number of elements to be sorted. This is because for each element, the algorithm scans the remaining unsorted portion to find the minimum element.

# What is the time complexity of the job scheduling algorithm?

# The time complexity of the job scheduling algorithm is 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn), where 
# 𝑛
# n is the number of jobs. This is because the algorithm sorts the jobs by profit, which takes 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn) time, and then schedules each job in a linear scan.

# Can the job scheduling algorithm be modified for more complex constraints?

# Yes, the job scheduling algorithm can be extended to accommodate additional constraints, such as job duration, job priorities, or time window constraints. Modifying the greedy strategy or using dynamic programming can handle such complexities.

# What happens if there are more jobs than available slots in job scheduling?

# If there are more jobs than available slots, the algorithm will assign jobs to the latest available slots up to the maximum number of slots. Jobs that cannot be scheduled due to slot limitations will not be assigned.

# How can the program be improved to handle more complex job scheduling scenarios?

# To handle more complex scenarios, the program can be modified to include job duration, dependencies, or multiple job types. Advanced algorithms like dynamic programming or backtracking can be used to explore more optimal solutions in such cases.








