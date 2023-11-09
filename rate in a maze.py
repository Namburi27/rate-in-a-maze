#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    for y in range(1, height, 2):
        for x in range(1, width, 2):
            maze[y][x] = 0 
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1 and random.random() < 0.25:
                maze[y][x] = 0 
    return maze
def isSafe( maze, x, y ):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False
def solveMaze( maze,N ):
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
    printSolution(sol)
    return True
def printSolution( sol ):
     
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        print("")
def solveMazeUtil(maze, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True
    if isSafe(maze, x, y) == True:
        sol[x][y] = 1
        
        # Move forward in x direction
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True

        # If moving in x direction doesn't give solution 
        # then Move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True
        
        # If none of the above movements work then 
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False

def print_maze(maze,N):
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    maze[0][0]='S'
    maze[N-1][N-1]='E'
    for row in maze:
        for item in row:
            if item==1:
                item=BLUE+'◌'+RESET
            if item==0:
                item=RED+'■'+RESET
            print(item,end=" ")
        print()

N = int(input())
maze = generate_maze(N,N)
maze[0][0]=1
maze[N-1][N-1]=1
print("Generated Maze:")
print_maze(maze,N)
while True:
    print("1. Print the path")
    print("2. Generate another puzzle")
    print("3. Exit the Game")
    choice = int(input("Enter your choice (1/2/3):"))
    if choice == 1:
        maze=solveMaze(maze,N)
        print_maze(maze,N)
    elif choice == 2:
        maze=generate_maze(N,N)
        print("New Maze Generated:")
        print_maze(maze,N)
    else:
        break

# This code is contributed by Shiv Shankar


# In[ ]:





# In[ ]:




