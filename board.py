from battleship import *

''' This class deals with a single important feature: providing
	the board on which the game is played. The reason it's best to
	separate this class is that it contains a fair amount of logic
	of its own. Specifically, you need to be able to translate back
	and forth between a Python list_of_lists (matrix) referenced from (0, 0)
	to a "natural game board" referenced from position A1.'''

class Board():
	# Class variable, possible rows. There is a built-in limit of 26 rows.
	# If you want more than these (e.g. 'AA', 'BB', then a lot of things 
	# would have to be altered, but I've never seen a board game beyond 10
	# rows.)
	possible_rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# REFACTOR: SHOULDN'T NEED TO COPY, BUT IMPORT WAS NOT WORKING, TEMPORARY FIX
	hit_codes = {'hit': 'X', 'miss': 'M'}

	# The default board size is 10 x 10, but any size is possible 
	# so long as the ships will fit.
	def __init__(self, rows=10, cols=10):
		self.width = cols
		self.height = rows
		self.grid = [p[:] for p in [['.'] * cols] * rows] # dot means empty
		# adapted from StackOverflow :), apparently fast, trippy syntax

	# When printing or accessing values, make sure the rows and columns are 
	# correct!!! When getting positions, the order is self.grid[row][col]
	# The whole x/y, width/height/ rows/cols thing is a nightmare, and 
	# easy to get mixed up, so pay attention to the order throughout.
	def simple_print(self):
		print('>>> printing {} row(s) and {} column(s)'.format(self.height, self.width))
		for row in range(self.height):
			one_row = ''
			for col in range(self.width):
				one_row += ('\t' + self.grid[row][col])
			print(one_row)
		print()

	# This method prints col and row headings, as well as any and all markings.
	# This is the method you would use to view your own board, as you can
	# see your own ships plus the opponent's hits and misses.
	def all_markings_print(self):
		print('>>> labeled {} row(s) and {} column(s)'.format(self.height, self.width))
		# Get column headings (horizontal spread)
		horizon_points =  [str(x + 1) for x in range(self.width)] # numbers 1 .. x as string
		horizon = '\t'.join(list(horizon_points)) # numbers go horizontally
		horizon = '\n\t' + horizon + '\n'
		print(horizon)

		# Get row headings (vertical spread)
		vert_headings = Board.possible_rows[0:self.height] # letters go down vertically on board

		for row in range(self.height):
			one_row = vert_headings[row]
			for col in range(self.width):
				one_row += ('\t' + self.grid[row][col])
			one_row += '\n'
			print(one_row)
		print()	

	# This method prints col and row headings and hit / miss markings,
	# but it leaves out ships. This is all you can see of the opponent's board
	# as you do not know where their ships are but know what positions
	# you fired at (hits and misses).
	def no_ships_print(self):
		print('>>> labeled {} row(s) and {} column(s)'.format(self.height, self.width))
		# Get column headings (horizontal spread)
		horizon_points =  [str(x + 1) for x in range(self.width)] # numbers 1 .. x as string
		horizon = '\t'.join(list(horizon_points)) # numbers go horizontally
		horizon = '\n\t' + horizon + '\n'
		print(horizon)

		# Get row headings (vertical spread)
		vert_headings = Board.possible_rows[0:self.height] # letters go down vertically on board

		for row in range(self.height):
			one_row = vert_headings[row] # letter on left edge (A, B, C...)
			for col in range(self.width):
				val = self.grid[row][col]
				if val in Board.hit_codes.values():
					one_row += ('\t' + self.grid[row][col])
				else:
					one_row += ('\t' + '.')
			one_row += '\n'
			print(one_row)
		print()

	# Takes a position expressed as a tuple (e.g. (0, 0)) 
	# and converts it to board coordinates (e.g. 'A1')
	def trans_to_board_coords(self, coordinate):
		x = coordinate[0] # row
		y = coordinate[1] # col
		if x < 0 or x >= self.width:
			raise ValueError('Horizontal coordinate invalid. Try again.')
		if y < 0 or y >= self.height:
			raise ValueError('Vertical coordinate invalid. Try again.')
		row = Board.possible_rows[y]
		col = str(x + 1)
		board_coord = row + col
		print('{} translates to {}'.format(coordinate, board_coord))
		return board_coord

	# Takes a board position (e.g. 'A1') and 
	# converts to python xy coords (e.g. (0, 0))
	def trans_to_python_coords(self, board_position):
		row = board_position[0]
		col = board_position[1:]
		x = int(col) - 1
		y = Board.possible_rows.index(row)
		py_coords = (x, y)
		print('{} translates to {}'.format(board_position, py_coords))
		return py_coords

	# This method takes a marking letter (e.g. 'X') 
	# and board position (e.g. 'A1') and marks the board with it.			
	def mark_position(self, letter, board_position):
		xy = self.trans_to_python_coords(board_position) # should return a tuple or -1 (error)
		if xy != -1:
			col = xy[0] 
			row = xy[1]
			print('Will place an {} at coordinate {} (= {} ), previously marked {}'. \
				format(letter, xy, board_position, self.grid[row][col]))
			self.grid[row][col] = letter

if __name__ == '__main__':
	# Default board is 10 x 10
	default_board = Board()
	default_board.no_ships_print()

	# One row four columns
	r , c = 1, 4
	bd1 = Board(r, c)
	bd1.simple_print()

	# Four rows, one column
	r , c = 4, 1
	bd2 = Board(r, c)
	bd2.simple_print()

	# The following should all fit on the first board (bd1)
	bd_pstn1 = 'A1'
	bd_pstn2 = 'A2'
	bd_pstn3 = 'A3'
	bd_pstn4 = 'A4'
	py_xy1 = bd1.trans_to_python_coords(bd_pstn1)
	py_xy2 = bd1.trans_to_python_coords(bd_pstn2)
	py_xy3 = bd1.trans_to_python_coords(bd_pstn3)
	py_xy4 = bd1.trans_to_python_coords(bd_pstn4)
	print()

	# The following should all fit on the second board (bd2)
	bd_pstn1 = 'A1'
	bd_pstn2 = 'B1'
	bd_pstn3 = 'C1'
	bd_pstn4 = 'D1'
	py_xy1 = bd2.trans_to_python_coords(bd_pstn1)
	py_xy2 = bd2.trans_to_python_coords(bd_pstn2)
	py_xy3 = bd2.trans_to_python_coords(bd_pstn3)
	py_xy4 = bd2.trans_to_python_coords(bd_pstn4)
	print()

	# Reverse translations for board 1
	bd_pos1 = bd1.trans_to_board_coords((0, 0))
	bd_pos1 = bd1.trans_to_board_coords((1, 0))
	bd_pos1 = bd1.trans_to_board_coords((2, 0))
	bd_pos1 = bd1.trans_to_board_coords((3, 0))	
	print()

	# Reverse translations for board 2
	bd_pos1 = bd2.trans_to_board_coords((0, 0))
	bd_pos1 = bd2.trans_to_board_coords((0, 1))
	bd_pos1 = bd2.trans_to_board_coords((0, 2))
	bd_pos1 = bd2.trans_to_board_coords((0, 3))	
	print()

	# Test print with labels
	bd1.all_markings_print()
	bd2.all_markings_print()

	# Test print no ships
	bd1.no_ships_print()
	bd2.no_ships_print()




