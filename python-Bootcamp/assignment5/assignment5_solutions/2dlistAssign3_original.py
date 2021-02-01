# WPCC
# 2dlistAssign3.py

import random
import math

def dist(x1, y1, x2, y2): # function dist calculates distance between 2 trees given their coordinates/indices
    dy = y2-y1
    dx = x2-x1
    return math.sqrt(dx**2 + dy**2) # return the differences, squared, and square rooted.

def check(grid):
    for i in range(len(grid)): # iterate through the grid
        for j in range(len(grid[i])):
            
            if grid[i][j] == 'X': # if a tree is found
                for dx in range(-3, 4):
                    for dy in range(-3, 4):
						# check if position is in the proper range
                        if not (dx == 0 and dy == 0) and 0 <= i+dy < len(grid) and 0 <= j+dx < len(grid[i]) and grid[i+dy][j+dx] == 'X':
                            d = dist(j, i, j+dx, i+dy) # compute distance between the 2 trees
                            if d <= 3: # if distance is less than 3 meters return False
                                return False
    return True # if the trees are properly spaced then return True

def printGrid(grid): # helper functions for printing the grid
    for line in grid:
        for char in line:
            print(char, end=' ')
        print('')

def generateGrid(grid): # function to generate the grid
	for i in range(30):
		temp = []
		for j in range(30):	
			temp.append('-')
		grid.append(temp)

	# the following code plants the trees in random spots on the grid
    count = 0
    while count < 10: # plant until 10 trees are planted
        x,y = random.randint(0, 29), random.randint(0, 29) # generate 2 random numbers
        if grid[x][y] != 'X': # make sure that there is not already a tree planted in this spot
            grid[x][y] = 'X'
            count += 1

grid = []
generateGrid(grid)

while check(grid) == False: # generate grids until all the trees are properly spaced
    grid = [] # reset the grid
    generateGrid(grid) # repopulate the grid
print('')
printGrid(grid)



