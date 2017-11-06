''' The ship class enables you to create different types of ships.
	Ships, of course, have a type (e.g. sub, carrier) or size.
	For convenience, they also have a bow position, orientation, and
	(horizontal 'H' or vertical 'V'). Ship 'slots' are used to keep
	track of which positiosn on the ship have been hit. Ship positions
	are the actual game-board positions. These are only provided once
	the ship is successfully provided on the game board.'''

class Ship():
	# Class variable: ship_types (dictionary)
	# This dictionary contains the valid shp types and their lengths.
	# If you want to add ships and their lengths, do it here. e.g. 'raft': 1
	# Rest of code should still work with such updates.
	ship_types = {'carrier': 5, 'battleship': 4, 'submarine': 3, \
				  'cruiser': 3, 'destroyer': 2}

	# Class variable: orientations (list)
	''' NOTE: Ship orientation codes are		'SN' (sailing North)
												'SE' (sailing East)
												'SS' (sailing South)
												'SW' (sailing West) '''
	orientations = ['SN', 'SE', 'SS', 'SW'] # used for placement on board

	''' This method determines the length based on the ship type
		passed to the init method (or create_ship method). If the ship
		type is invalid, length determination will fail.'''
	@classmethod
	def length(cls, ship_type):
		if ship_type in Ship.ship_types.keys():
			l = Ship.ship_types[ship_type]
		else:
			# if you want to test invalid ship type, comment out the 'raise'
			raise ValueError('Unknown ship type')
			l = -1
		return l

	# The class version for creating a ship screens for invalid ship types.
	@classmethod
	def create_ship(cls, t, bp, o):
		if Ship.length(t) == -1: # invalid ship type or length
			return None # comment out Ship.length() raise to return None.
			# Bad ship types currently simply caught as a ValueError, both approaches make
			# sense depending on what behavior the engineers want.
		return cls(t, bp, o)

	# Standard init method, screens for Value Error on length returned from ship type.
	def __init__(self, t, bp, o):
		self.type = t
		self.bow_position = bp # Validity checked on game board, not here.
		self.length = Ship.length(t) # Raises error if type invalid.
		if o in Ship.orientations: # Raises error if orientation invalid.
			self.orientation = o # Sailing North/South/East/West (SN, SE, SS, SW)
		else:
			raise ValueError('Orientation code is invalid. Use SN, SE, SS, or SW.')
		self.slots = [0] * self.length # '0' means not hit, '1' means hit
		self.positions = [] # these will be set when ship is placed on the board
		self.describe()

	def describe(self):
		print('{} at {} with length {} and orientation {}'. \
			format(self.type, self.bow_position, self.length, self.orientation))

	''' The status of a ship will basicaly indicate floating
		or alive. Knowledge of which positions are hit can be made explicit by
		examining the 'slots' list, but you can also quickly determine whether
		the boat is afloat or sunk based on whether the number of hits (1)
		equals the length of the boat.'''
	def status(self):
		# print(self.slots)
		num_hits = sum(self.slots)
		status = 'afloat' if num_hits < self.length else 'sunk'
		# print(status)
		return status

	''' This method simply marks that a ship should be hit at a certain position.
		Invalid positions ignored: the battlefield should recognize that
		they are not on the ship, so unlikely to be sent.'''
	def hit(self, position):
		if position < self.length:
			self.slots[position] = 1
		print(self.status())

if __name__ == '__main__':
	s1 = Ship('carrier', 'A1', 'SE')
	s2 = Ship.create_ship('carrier', 'A1', 'SW')
	s3 = Ship('submarine', 'J9', 'SN')
	s1.status()
	s2.status()
	s3.status()
	s3.hit(0)
	s3.hit(1)
	s3.hit(2)
	s3.hit(3) # invalid number will be ignored

