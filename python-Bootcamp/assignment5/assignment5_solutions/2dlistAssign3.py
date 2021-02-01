# WPCC

from random import randint

# 30x30 list that holds a 'X' where a tree is, and '_' where there's no tree
backyard = []
for i in range(30):
	l = []
	for j in range(30):
		l.append('_')
	backyard.append(l)

# 10x2 list that holds all coordinates for the 10 trees we're going to plant
trees = []
for i in range(10):
	l = [0, 0]
	trees.append(l)

# Helper function to create the 10x2 list that holds the trees
def createList():
	for i in range(len(trees)):
		trees[i] = [randint(0, 29), randint(0, 29)]
	return trees

# This function will check if any two trees are within 3m of each other.
# It returns True if it's valid and False if it's not valid
def checkDistance(posList):
	# Recursive case: if length of posList is not 1
	if len(posList) != 1:
		# get the first coordinate
		coord1 = posList[0]

		# Check distance between first and the rest of the coordinates
		for coord2 in posList[1:]:
			dist = ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5 # Pythagorean Theorem
			# If invalid distance, returns False
			if dist <= 3:
				return False
		# Recurse with a smaller list. Since we checked the first point, we only need to check the remaining ones now
		flag = checkDistance(posList[1:])
		if flag == False:
			return False

	# Base case: If there's only 1 point in `posList`, then return True
	return True

# Create list until a valid one is generated
while True:
	created = createList()
	if checkDistance(created) == True:
		break

# Make the backyard list out of the coordinates generated
for coord in created:
	backyard[coord[0]][coord[1]] = 'X'

# Print out the backyard
for row in backyard:
	print(*row, sep=' ')

