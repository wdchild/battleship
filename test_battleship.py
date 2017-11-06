import unittest
from battleship import *
from ship import *

class BattleShipTestCase(unittest.TestCase):

	'''def test_A_empty_grid(self):
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
		print(bs.fire_missile('A2'))
		print(bs.fire_missile('A1'))
		bs.show_board_with_ships()
		print(bs.fire_missile('B1'))
		bs.show_board_with_ships()
		print(bs.fire_missile('C1'))
		bs.show_board_with_ships()
		print(bs.fire_missile('D1'))
		bs.show_board_with_ships()
		print(bs.fire_missile('E1'))
		bs.show_board_with_ships() # game won at this point

	def test_F_random_shots(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		bs.show_board_with_ships()
		print(bs.random_shot())
		print(bs.fire_missile('A1'))'''

	'''def test_G_play_to_sink(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		result = 'continue'
		while result != 'hit':
			shot_result = bs.random_shot()
			result = shot_result[0]
			shot_xy = shot_result[1]
		print('Hit with shot at {}'.format(shot_xy))

	def test_H_move(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)
		pos_n = bs.move((1, 1), 'north')
		pos_s = bs.move((1, 1), 'south')
		pos_e = bs.move((1, 1), 'east')
		pos_w = bs.move((1, 1), 'west')
		print(pos_n, pos_s, pos_e, pos_w)'''

	''' def test_I_target_shot(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)	
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		shot_result = bs.fire_missile('C1')
		bs.target_shots(shot_result)'''

	'''def test_J_play_to_sink(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)	
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		bs.play_to_sink()'''

	def test_H_play_to_win(self):
		rows, cols = 5, 5
		bs = BattleShip(rows, cols)	
		s1 = Ship.create_ship('carrier', 'A1', 'SN')
		bs.place_ship(s1)
		bs.play_to_win()



if __name__ == '__main__':
	unittest.main()

