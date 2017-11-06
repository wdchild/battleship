import unittest
from ship import *

class ShipTestCase(unittest.TestCase):

	def test_ship_properties(self):
		s1 = Ship.create_ship('carrier', 'A1', 'SE')
		self.assertEqual(s1.type, 'carrier')
		self.assertEqual(s1.length, 5)
		self.assertEqual(s1.bow_position, 'A1')
		self.assertEqual(s1.orientation, 'SE')
		self.assertEqual(s1.slots, [0, 0, 0, 0, 0])

		s2 = Ship.create_ship('submarine', 'B4', 'SW')
		self.assertNotEqual(s2.type, 'carrier') # should be submarine
		self.assertNotEqual(s2.length, 5) # should be 3
		self.assertNotEqual(s2.bow_position, 'C4') # should be B4
		self.assertNotEqual(s2.orientation, 'SZ') # should be SW
		self.assertNotEqual(s2.slots, [0, 0, 0, 0, 0]) # should be [0, 0, 0]

	def test_ship_hits_and_status(self):
		s3 = Ship.create_ship('destroyer', 'C7', 'SN')
		self.assertEqual(s3.status(), 'afloat')
		s3.hit(0)
		self.assertEqual(s3.status(), 'afloat')
		s3.hit(1)
		self.assertEqual(s3.status(), 'sunk')
		self.assertNotEqual(s3.status(), 'afloat')

	''' If you want to the following test so as to test invalid ship types,
		you need to comment out the ValueError raised under
		Ship.length(). I decided to stop program for incorrect ship types,
		but you could also just return a 'None' ship, which is what
		create_ship does if you do not raise the Value Error exception.
		Either approach works. Which is better depends on whether you
		are using try statements for each ship creation on the game board.

	def test_invalid_ship_type(self):
		s4 = Ship.create_ship('raft', 'J1', 'SS')
		self.assertEqual(s4, None) '''

if __name__ == '__main__':
    unittest.main()
