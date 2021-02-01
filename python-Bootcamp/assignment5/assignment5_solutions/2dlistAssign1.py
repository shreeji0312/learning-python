# WPCC
# 2dlistAssign1.py

def empty(list2d): # defines a function called empty
	for i in list2d: # iterate through each list in the 2d list.
		for j in i: # iterate through each value in the inner lists
			if j != 0: # if the value is not 0, thus the 2d list is not empty
				return False # return False when 2d list is not empty
	return True # return true if list is empty

def find(list2d, search_number): # define a function called find
	for i in range(len(list2d)): # iterate through the length of the list
		for j in range(len(list2d[i])):
			if list2d[i][j] == search_number: # if the number is found
				return [i, j] # return the position the number is found at
	return [-1, -1] # return [-1, -1] if the value is not found

grid = [[23, 34, 67], [44, 5, 3], [7, 8, 9]]

print(empty(grid))
print(find(grid, 67))
