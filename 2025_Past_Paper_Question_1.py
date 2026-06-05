# %% [markdown]
# # 2025 Past Paper: Question 1
# This paper focused on Fundamentals: Dictionaries, Search Algorithms (BFS), and Logic.

# %% [markdown]
# ### Part A: Basic Python (Dictionaries & Loops)
# The goal is to ask the user for a genre and print recommended movies.

# %%
# 1. Create a dictionary where the 'Key' is the genre, and the 'Value' is a list of movies.
movies = {
    "action" : ["Spider Man", "Harry Potter"],
    "comedy" :  ["FRIENDS", "The Office"],
    "drama" : ["Game of Thrones", "The Wire"]
}

# 2. Hardcoding the genre for this test (In the exam, they used: genre = input("Enter a genre: "))
genre = "action"

def filterAndShowRecommendedMovies(genre):
    # 3. Check if the genre exists in our dictionary
    if genre not in movies:
        print("Invalid genre")
    else:
        # 4. Loop through the list of movies for that specific genre
        for movie in movies[genre]:
            print(movie)

# Run the function
print("--- Recommended Movies ---")
filterAndShowRecommendedMovies(genre)


# %% [markdown]
# ### Part B: Breadth-First Search (BFS)
# Finding the shortest path in a grid from 'Start' to 'Goal'.
# NOTE: I fixed a bug from the original student's code so this will run perfectly!

# %%
from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)       # Number of rows (4)
    cols = len(grid[0])    # Number of columns (5)
    
    # A queue keeps track of where we are and the path we took to get there
    queue = deque([(start, [start])])
    
    # A set keeps track of places we've already been so we don't go in circles
    visited = set([start])
    
    # Directions we can move: Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        # Pop the oldest item from the queue
        (row, col), path = queue.popleft()

        # If we reached the goal, return the path we took!
        if (row, col) == goal:
            return path

        # Try moving in all 4 directions
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Check if the new move is inside the grid AND it is a '0' (an open path, not a wall)
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
                m = (new_row, new_col)
                if m not in visited:
                    visited.add(m)
                    # FIX: We append the new position AND the updated path to the queue
                    queue.append((m, path + [m]))

    return None # No path found

# The grid: 0 is an open path, 1 is a wall
grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0]
]
start = (0,3)
goal = (3,4)

shortest_path = bfs(grid, start, goal)

print("\n--- BFS Shortest Path ---")
if shortest_path:
    print("Path found:", shortest_path)
else:
    print("No path found.") 


# %% [markdown]
# ### Part C: Propositional Logic (Truth Table)
# Generating a Truth Table for a boolean math formula.

# %%
import pandas as pd

# The math formula: (A OR D) AND (If B then C)
def formula(A, B, C, D):
    # A or D
    form1 = A or D
    # (B -> C) translates to (not B or C) in code
    form2 = not B or C
    # Final combined formula
    return form1 and form2

# The two possible boolean values
values = [True, False]
data = []

# Loop through every possible combination of A, B, C, and D
for A in values:
    for B in values:
        for C in values:
            for D in values:
                result = formula(A, B, C, D)
                # Save the combination to our data list
                data.append({'A': A, 'B': B, 'C': C, 'D': D, 'Result': result})

# Use Pandas to display it as a beautiful table
df = pd.DataFrame(data)
df = df.set_index(['A', 'B', 'C', 'D'])
print("\n--- Truth Table ---")
print(df)
