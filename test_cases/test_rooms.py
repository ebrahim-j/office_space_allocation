import unittest
from ..app.room import OfficeSpace, LivingSpace


class TestCreateRoom(unittest.TestCase):
	"""Test room creation """
	def setUp(self):
		self.office_space = OfficeSpace("Red")
		self.living_space = LivingSpace("Emerald")
	
	def test_officespace_size(self):
		self.assertEqual(self.office_space.capacity, 6,
			msg ='Maximum capacity is 6 occupants')

	def test_officespace_type(self):
		self.assertEqual(self.office_space.room_type, "OFFICE",
			msg = "Room created should be of type OFFICE")

	def test_livingspace_size(self):
		self.assertEqual(self.living_space.capacity, 4, 
			msg = 'Maximum capacity is 4 occupants')

	def test_livingspace_type(self):
		self.assertEqual(self.living_space.room_type, "LIVING SPACE",
			msg = "Room Created should be of type LIVING SPACE")
	
	def test_allowed_maximum_number_of_occupants_per_office(self):
		self.assertEqual(len(self.office_space.occupants), 6,
			msg = 'You cannot assign more than 6 people to an office')

	def test_allowed_maximum_number_of_occupants_per_livingspace(self):
		self.assertEqual(len(self.living_space.occupants), 4,
			msg = 'You cannot assign more than 4 people to a living space')
