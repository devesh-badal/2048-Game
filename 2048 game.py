import random

def start_game():

	grid =[]
	for i in range(4):
		grid.append([0] * 4)

	print("Commands are as follows : ")
	print(" 1 : Move Left")
	print(" 2 : Move Right")
	print(" 3 : Move Up")
	print(" 4 : Move Down")
	
	add_new(grid)
	return grid

def add_new(grid):

	r = random.randint(0, 3)
	c = random.randint(0, 3)

	while(grid[r][c] != 0):
		r = random.randint(0, 3)
		c = random.randint(0, 3)

	grid[r][c] = random.choice([2,4])


def get_current_state(grid):

	for i in range(4):
		for j in range(4):
			if(grid[i][j]== 2048):
				return 'WON'

	for i in range(4):
		for j in range(4):
			if(grid[i][j]== 0):
				return 'GAME NOT OVER'

	for i in range(3):
		for j in range(3):
			if(grid[i][j]== grid[i + 1][j] or grid[i][j]== grid[i][j + 1]):
				return 'GAME NOT OVER'

	for j in range(3):
		if(grid[3][j]== grid[3][j + 1]):
			return 'GAME NOT OVER'

	for i in range(3):
		if(grid[i][3]== grid[i + 1][3]):
			return 'GAME NOT OVER'

	return 'LOST'


def compress(grid):

	changed = False
	new_grid = []

	# with all cells empty
	for i in range(4):
		new_grid.append([0] * 4)

	for i in range(4):
		pos = 0

		for j in range(4):
			if(grid[i][j] != 0):

				new_grid[i][pos] = grid[i][j]
				
				if(j != pos):
					changed = True
				pos += 1

	# returning new compressed gridrix
	# and the flag variable.
	return new_grid, changed


def merge(grid):
	
	changed = False
	
	for i in range(4):
		for j in range(3):

			if(grid[i][j] == grid[i][j + 1] and grid[i][j] != 0):

				grid[i][j] = grid[i][j] * 2
				grid[i][j + 1] = 0

				changed = True

	return grid, changed

def reverse(grid):
	new_grid =[]
	for i in range(4):
		new_grid.append([])
		for j in range(4):
			new_grid[i].append(grid[i][3 - j])
	return new_grid


def transpose(grid):
	new_grid = []
	for i in range(4):
		new_grid.append([])
		for j in range(4):
			new_grid[i].append(grid[j][i])
	return new_grid


def move_left(grid):

	new_grid, changed1 = compress(grid)

	new_grid, changed2 = merge(new_grid)
	
	changed = changed1 or changed2

	new_grid, temp = compress(new_grid)

	return new_grid, changed


def move_right(grid):

	new_grid = reverse(grid)

	new_grid, changed = move_left(new_grid)

	new_grid = reverse(new_grid)
	return new_grid, changed


def move_up(grid):

	new_grid = transpose(grid)

	new_grid, changed = move_left(new_grid)

	new_grid = transpose(new_grid)
	return new_grid, changed


def move_down(grid):

	new_grid = transpose(grid)

	new_grid, changed = move_right(new_grid)

	new_grid = transpose(new_grid)
	return new_grid, changed

#----------------------------------------------------------------------------------

grid = start_game()
while(True):

	x = input("Press the command : ")

    # to move left
	if(x == '1'):
		grid, flag = move_left(grid)
		status = get_current_state(grid)
		print(status)
		if(status == 'GAME NOT OVER'):
			add_new(grid)
		else:
			break
			
	# to move right
	elif(x == '2'):
		grid, flag = move_right(grid)
		status = get_current_state(grid)
		print(status)
		if(status == 'GAME NOT OVER'):
			add_new(grid)
		else:
			break

	#  to move up
	elif(x == '3'):

		grid, flag = move_up(grid)
		status = get_current_state(grid)
		print(status)
		if(status == 'GAME NOT OVER'):
			add_new(grid)
		else:
			break

	# to move down
	elif(x == '4'):
		grid, flag = move_down(grid)
		status = get_current_state(grid)
		print(status)
		if(status == 'GAME NOT OVER'):
			add_new(grid)
		else:
			break
			
	else:
		print("Invalid Key Pressed")

	for i in grid:
	    print(i)
	print("")    
	    