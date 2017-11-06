import unittest
from board import *

class BoardTestCase(unittest.TestCase):

	def test_A_init(self):
		rows = 3
		cols = 5
		bd = Board(rows, cols) # expect 3 rows 5 cols
		self.assertEqual(bd.width, 5)
		self.assertEqual(bd.height, 3)

	def test_B_all_markings_print(self):
		rows = 5
		cols = 3
		bd = Board(rows, cols) # expect 5 rows 3 cols
		bd.all_markings_print() # numbers for column headers, letters for rows

	def test_C_trans_to_py_xy(self):
		r , c = 1, 4
		bd1 = Board(r, c)
		bd1.simple_print()
		bd_pstn1 = 'A1'
		bd_pstn2 = 'A2'
		bd_pstn3 = 'A3'
		bd_pstn4 = 'A4'
		py_xy1 = bd1.trans_to_python_coords(bd_pstn1)
		py_xy2 = bd1.trans_to_python_coords(bd_pstn2)
		py_xy3 = bd1.trans_to_python_coords(bd_pstn3)
		py_xy4 = bd1.trans_to_python_coords(bd_pstn4)
		self.assertEqual(py_xy1, (0, 0))
		self.assertEqual(py_xy2, (1, 0))
		self.assertEqual(py_xy3, (2, 0))
		self.assertEqual(py_xy4, (3, 0))

	def test_D_trans_to_board_positions(self):
		r , c = 4, 1
		bd2 = Board(r, c)
		bd2.simple_print()
		bd_pos1 = bd2.trans_to_board_coords((0, 0))
		bd_pos2 = bd2.trans_to_board_coords((0, 1))
		bd_pos3 = bd2.trans_to_board_coords((0, 2))
		bd_pos4 = bd2.trans_to_board_coords((0, 3))	
		self.assertEqual(bd_pos1, 'A1')
		self.assertEqual(bd_pos2, 'B1')
		self.assertEqual(bd_pos3, 'C1')
		self.assertEqual(bd_pos4, 'D1')

	def test_E_position_marking(self):
		r, c = 3, 5
		bd3 = Board(r, c)
		bd3.mark_position('A1', 'A1')
		bd3.mark_position('A2', 'A2')
		bd3.mark_position('B1', 'B1')
		bd3.mark_position('X', 'B2')
		bd3.all_markings_print()
		bd3.no_ships_print()

if __name__ == '__main__':
	unittest.main()