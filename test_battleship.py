import unittest
from battleship import *
from ship import *

class BattleShipTestCase(unittest.TestCase):

	def test_A_empty_grid(self):
		rows = 2
		cols = 4
		bs = BattleShip(rows, cols)
		bs.show_board_no_ships() # expect 2 rows 4 cols

	def test_B_coordinate_conversions(self):
		rows = 5
		cols = 5
		bs = BattleShip(rows, cols)
		bs.show_board_no_ships()
		zero_based_xy = bs.trans_to_python_coords('E1') # should yield (0, 4)
		letter_based_xy = bs.trans_to_board_coords((0, 4)) # should yield 'E5'
		self.assertEqual(zero_based_xy, (0, 4))
		self.assertEqual(letter_based_xy, 'E1')
		zero_based_xy = bs.trans_to_python_coords('A3') # should yield (2, 0)
		letter_based_xy = bs.trans_to_board_coords((2, 0)) # should yield 'E5'
		self.assertEqual(zero_based_xy, (2, 0))
		self.assertEqual(letter_based_xy, 'A3')

	def test_C_marked_position(self):
		rows = 3
		cols = 6
		bs = BattleShip(rows, cols)
		bs.mark_position('X', 'A1')
		bs.mark_position('X', 'A2')
		self.assertEqual(bs.board.grid[0][0], 'X')
		self.assertEqual(bs.board.grid[1][0], '.')
		bs.show_board_no_ships()

	def test_D_desired_positions(self):
		rows = 5
		cols = 3
		bs = BattleShip(rows, cols)

		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		wanted = bs.desired_positions(s1) # calls desired_positions
		self.assertEqual(wanted, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
		
		s2 = Ship.create_ship('submarine', 'A5', 'SE')
		wanted = bs.desired_positions(s2) # calls desired_positions
		self.assertEqual(wanted, [(4, 0), (3, 0), (2, 0)])
		
		s3 = Ship.create_ship('destroyer', 'B1', 'SS')
		wanted = bs.desired_positions(s3) # calls desired_positions
		self.assertEqual(wanted, [(0, 1), (0, 0)])
		
		s4 = Ship.create_ship('submarine', 'A1', 'SW')
		wanted = bs.desired_positions(s4) # calls desired_positions
		self.assertEqual(wanted, [(0, 0), (1, 0), (2, 0)])

	def test_E_fire_missile(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		bs.show_board_with_ships()
		bs.fire_missile('A1')
		bs.show_board_with_ships()
		bs.fire_missile('B1')
		bs.show_board_with_ships()
		bs.fire_missile('C1')
		bs.show_board_with_ships()
		bs.fire_missile('D1')
		bs.show_board_with_ships()
		bs.fire_missile('E1')
		bs.show_board_with_ships() # game won at this point

if __name__ == '__main__':
	unittest.main()
