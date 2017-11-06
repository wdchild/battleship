from ship import *
from board import *
import random

''' This is the class the essentially manages the game. It draws on the
	Ship and Board classes for functionality. If you were developing this
	further, you would almost certainly create a Player class to handle
	Player logic. But we were asked not to do that.'''

class BattleShip():
	''' If you add to list of ships, need to update codes here accordingly.
		e.g. for raft, 'raft': 'R' '''
	ship_codes = {'carrier': 'A', 'battleship': 'B', 'submarine': 'S', \
				  'cruiser': 'C', 'destroyer': 'D'}

	''' Abstracting hit codes also useful in case the number of ship types
		increases. You can modify here in one place without going all over the code.
		Must not conflict with the ship codes.'''
	hit_codes = {'hit': 'X', 'miss': 'M'}

	''' Class variable, list of ships that are on the BattleShip board.
		This variable is useful for determining the status of the individual ships
		at any point in time.'''
	ships = []

	''' Class variable, indicating possible row labels.
		If you want more than these (e.g. 'AA', 'BB', then a lot of things 
		would have to be altered, but I've never seen a batttleship board 
		with more than rows, so this should be sufficient.'''
	possible_rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# Typically you would want two boards (one for you, one for opponent).
	# But instructions call for only one board.
	def __init__(self, rows=10, cols=10):
		self.board = Board(rows, cols)
		self.right_boundary = self.board.width - 1
		self.lower_boundary = self.board.height - 1

	# References method from Board class; remaning makes it easier to call directly from
	# the battleship class rather than through its board property. Same below.
	def show_board_no_ships(self):
		self.board.no_ships_print()

	# References method from Board class; remaning makes it easy to reference the method.
	def show_board_with_ships(self):
		self.board.all_markings_print()
		
	# References method from Board class; remaning makes it easy to reference the method.
	def trans_to_board_coords(self, xy):
		return self.board.trans_to_board_coords(xy)

	# References method from Board class; remaning makes it easy to reference the method.
	def trans_to_python_coords(self, board_position):
		return self.board.trans_to_python_coords(board_position)

	# References method from Board class; remaning makes it easy to reference the method.
	def mark_position(self, letter, board_position):
		self.board.mark_position(letter, board_position)

	# Checks the positions desired based on bow position and orientation.
	def desired_positions(self, ship):
		bow_pos = self.trans_to_python_coords(ship.bow_position)
		
		# To save on typing (at the cost of minimal memory expense)
		orientation = ship.orientation
		length = ship.length
		positions = [bow_pos]

		# THE FOLLOWING POSITION CALCULATIONS ARE ACCURATE BUT REPETITIVE
		# REFACTOR THIS WHEN YOU GET TIME
		# -> just compute positions
		# -> if any position in positions < 0 or > boundary, raise ValueError
		if orientation == 'SN':
			print('Heading north, {} occupies {} spot(s) south of {}'.format(ship.type, length-1, bow_pos))
			for pos in range(1, length):
				new_pos = (bow_pos[0], bow_pos[1] + pos) # note: xy, not row-col
				# print('new_pos is {}'.format(new_pos))
				if new_pos[0] > self.lower_boundary:
					raise ValueError('Invalid ship position detected.')
					return None # REFACTOR (same below) ... never gets called
				else:
					positions.append(new_pos)

		elif orientation == 'SE':
			print('Heading east, {} occupies {} spot(s) west of {}'.format(ship.type, length-1, bow_pos))
			for pos in range(1, length):
				new_pos = (bow_pos[0] - pos, bow_pos[1])
				# print('new_pos is {}'.format(new_pos))
				if new_pos[0] < 0:
					raise ValueError('Invalid ship position detected.')
					return None
				else:
					positions.append(new_pos)

		elif orientation == 'SS':
			print('Heading south, {} occupies {} spot(s) north of {}'.format(ship.type, length-1, bow_pos))
			for pos in range(1, length):
				new_pos = (bow_pos[0], bow_pos[1] - pos)
				# print('new_pos is {}'.format(new_pos))
				if new_pos[1] < 0:
					raise ValueError('Invalid ship position detected.')
					return None
				else:
					positions.append(new_pos)

		elif orientation == 'SW':
			print('Heading west, {} occupies {} spot(s) east of {}'.format(ship.type, length-1, bow_pos))
			for pos in range(1, length):
				new_pos = (bow_pos[0] + pos, bow_pos[1])
				# print('new_pos is {}'.format(new_pos))
				if new_pos[1] < 0:
					raise ValueError('Invalid ship position detected.')
					return None
				else:
					positions.append(new_pos)

		else:
			raise ValueError('Unknown orientation code! Use SN, SE, SS, or SW')
		print('Desired positions for ship {} with bow at {}: {}'.format(ship.type, ship.bow_position, positions))
		return positions

	''' If this is extended to a real players game, you want ships to be able to sail
		in different directions (up, down, right, and left) on the board. These
		options are notated as north, south, east, west, specifically,
		sailing north (SN), sailing east (SE), sailing south (SS), and
		sailing west (SW).'''
	def place_ship(self, ship):
		code = BattleShip.ship_codes[ship.type]
		print(code)
		print(ship.orientation)
		positions = self.desired_positions(ship)
		# print('Desired positions are {}'.format(positions))
		if self.positions_free(positions):
			for xy in positions:
				# print('Placing xy {}'.format(xy))
				col = xy[0]
				row = xy[1]
				if self.board.grid[row][col] == '.':
					self.board.grid[row][col] = BattleShip.ship_codes[ship.type]
			BattleShip.ships.append(ship)
			ship.positions = positions # for later identification
		else:
			print('Cannot place this ship. Placement ignored.')
			# raise ValueError('Ship positions conflict. Cannot place this ship.')
			# No point killing the game for a stupid placement.'''

	# This method makes sure there are no ships at the desired positions
	# This is used prior to firing missiles.
	def positions_free(self, positions):
		for xy in positions:
			# print('Checking xy {}'.format(xy))
			col = xy[0]
			row = xy[1]
			if self.board.grid[row][col] != '.': # things are either a dot or a ship in the beginning
				return False
		return True

	def play_to_win(self):
		shot_result = self.random_shot()
		result = shot_result[0]
		print('in play_to_win shot_result {} result {}'.format(shot_result, result))
		count = 0
		while(result != 'win' and count < 3):
			result = self.play_to_sink()
			count += 1

	def play_to_sink(self):
		# first take a random shot
		shot_result = self.random_shot()
		result = shot_result[0] # hit, already taken, miss, etc.
		shot_xy = shot_result[1] # coordinates 
		print(shot_result)
		print(result, str(shot_xy))
		
		# while not sunk
		while(result != 'hit'):
			# continue random shots
			shot_result = self.random_shot()
			result = shot_result[0]
			print('in play_to_sink while, shot_result {} result {}'.format(shot_result, result))
		# will break out with a 'hit'

		# do targeted shooting until sunk (whiles are inside the method)
		# target_shots should return a "sink" method
		shot_result = self.target_shots(shot_result)
		print('target_shots returned {}'.format(shot_result))
		result = shot_result[0]

		return result # either 'hit' or 'win'

	def target_shots(self, shot_result):
		result = 'continue'
		print('in target shots shot_result is {}'.format(shot_result))
		xy = shot_result[1]
		print('xy is {}'.format(xy))

		# will continue north until miss or end of board or sunk
		while (result != 'sunk' and result != 'win' \
			   and xy[1] > 0 and result != 'miss'):
			xy = self.move(xy, 'north')
			board_pos = self.trans_to_board_coords(xy)
			shot_result = self.fire_missile(board_pos)
			result = shot_result[0]

		# if sunk going north, will not enter
		while (result != 'sunk' and result != 'win' \
			   and xy[1] < self.lower_boundary and result != 'miss'):
			xy = self.move(xy, 'south')
			board_pos = self.trans_to_board_coords(xy)
			shot_result = self.fire_missile(board_pos)
			result = shot_result[0]

		# if sunk going north or south, will not enter
		while (result != 'sunk' and result != 'win' \
			   and xy[0] < self.right_boundary and result != 'miss'):
			xy = self.move(xy, 'east')
			board_pos = self.trans_to_board_coords(xy)
			shot_result = self.fire_missile(board_pos)
			result = shot_result[0]

		# if sunk going north or south or east, will not enter
		while (result != 'sunk' and result != 'win' \
			   and xy[0] > 0 and result != 'miss'):
			xy = self.move(xy, 'west')
			board_pos = self.trans_to_board_coords(xy)
			shot_result = self.fire_missile(board_pos)
			result = shot_result[0]

		print('from target_shots returning {}'.format(shot_result))
		return shot_result

	def move(self, xy, direction):
		if direction == 'north':
			xy = (xy[0], xy[1] - 1)
		if direction == 'south':
			xy = (xy[0], xy[1] + 1)
		if direction == 'east':
			xy = (xy[0] + 1, xy[1])
		if direction == 'west':
			xy = (xy[0] - 1, xy[1])
		print('Moving {} to {}'.format(direction, xy))
		return xy

	def random_shot(self):
		x = random.randint(0, self.lower_boundary) # get function
		y = random.randint(0, self.right_boundary)
		xy = (x, y)
		bp = self.trans_to_board_coords(xy)
		shot_result = self.fire_missile(bp)
		print('random shot result is {}'.format(shot_result))
		return shot_result

	''' Now for the fun part: firing missiles!
		If it's a hit, then you check if boat is sunk.
		And if it's sunk, then you check for a win.'''

	def fire_missile(self, board_position):
		result = 'continue'
		xy = self.trans_to_python_coords(board_position)
		col = xy[0]
		row = xy[1]
		if col < 0 or col > self.right_boundary: # off the board horizontally
			raise ValueError('Invalid horizontal missile board_position!')
		if row < 0 or row > self.lower_boundary: # off the board vertically
			raise ValueError('Invalid vertical missile board_position!')

		if self.board.grid[row][col] == '.': # open seas
			result = 'miss'
			print('{} is a miss!'.format(board_position))
			self.board.grid[row][col] = BattleShip.hit_codes['miss']
			return (result, xy)

		if self.board.grid[row][col] in BattleShip.hit_codes.values(): # previously shot at
			print('{} is already taken!'.format(board_position))
			result = 'taken'
			# ACTUALLY, YOU SHOULD KEEP TRACK OF SHOT POSITIONS SO YOU DON'T
			# TRY TO SHOOT THEM TWICE (AVOID BACKTRACKING), COULD STORE IN DICTIONARY
			return (result, xy)

		if self.board.grid[row][col] in BattleShip.ship_codes.values(): # ship hit
			result = 'hit'
			print('{} is a hit!'.format(board_position))
			this_ship = self.id_ship_by_pos(xy)
			# print('You hit a {}'.format(this_ship.type))
			# print('Its positions are {}'.format(this_ship.positions))
			i = this_ship.positions.index(xy)
			# print('Corresponding index is {}'.format(i))
			this_ship.hit(i) # damage ship at that slot
			
			# mark the hit on the field
			self.board.grid[row][col] = BattleShip.hit_codes['hit']
			# check if sunk
			status = this_ship.status()
			# print(status)
			if status == 'sunk':
				result = 'sunk'
				print('You sank a {}'.format(this_ship.type))
				# since you sank it, need to see if all ships are sunk
				fleet_status = self.check_fleet_status()
				if fleet_status == 'destroyed':
					result = 'win'
					print('You won!')
					
			return (result, xy)


	def id_ship_by_pos(self, coordinate):
		for ship in BattleShip.ships:
			# print(coordinate)
			# print(ship.positions)
			if coordinate in (ship.positions):
				# print(ship.type, ship.bow_position)
				return ship

	''' If a ship is sunk, then you need to check if the entire fleet
		has been sunk. In that case, you declare a win.'''
	def check_fleet_status(self):
		fleet_status = 'destroyed' # assume everything sunk
		for ship in BattleShip.ships:
			if ship.status() == 'afloat':
				fleet_status = 'still alive'
		return fleet_status


if __name__ == '__main__':
	# test basic board
	bs = BattleShip(5, 5)
	bs.show_board_no_ships()
	print()

	# test references to coordinate translation methods
	'''
	bs.trans_to_python_coords('D1') # should be (0, 3)
	bs.trans_to_python_coords('B5') # should be (4, 1)
	bs.trans_to_python_coords('A1') # works
	print()
	bs.trans_to_board_coords((0, 0)) # should be A1
	bs.trans_to_board_coords((0, 3)) # should be D1
	bs.trans_to_board_coords((3, 0)) # should be A4
	print()''' 

	# create ship and place it
	s1 = Ship.create_ship('carrier', 'E1', 'SS')
	bs.desired_positions(s1) # sailing east with bow at A5
	bs.place_ship(s1)
	bs.show_board_with_ships()

	# bs.fire_missile('A11') # invalid missle coordinate for testing
	# bs.fire_missile('Z1') # invalid missle cordinate for testing
	bs.fire_missile('A1')
	bs.fire_missile('A2')
	bs.fire_missile('B1')
	bs.fire_missile('C1')
	bs.fire_missile('D1')
	bs.fire_missile('E1')
	bs.show_board_with_ships()
	bs.show_board_no_ships()
	
	'''
	s1 = Ship.create_ship('carrier', 'A1', 'SN')
	bs.place_ship(s1) # sailing north
	bs.show_board_with_ships()
	s2 = Ship.create_ship('submarine', 'C4', 'SE')
	bs.place_ship(s2)
	bs.show_board_with_ships()

	s3 = Ship.create_ship('cruiser', 'G5', 'SS')
	bs.place_ship(s3)
	bs.show_board_with_ships()

	s4 = Ship.create_ship('destroyer', 'I9', 'SW')
	bs.place_ship(s4)
	bs.show_board_with_ships()

	# rather than shutting down the game, I simply ignore
	# ships whose positions will conflict with another ship
	# so rather than raising an error, I simply print the error,
	# but the game can continue (temporary design decision)
	# the invalid ship is not placed
	s5 = Ship.create_ship('battleship', 'F4', 'SE')
	bs.place_ship(s5)
	bs.show_board_with_ships()


	# bf.fire_missile('C5')
	# bf.show_board_with_ships()
	'''

