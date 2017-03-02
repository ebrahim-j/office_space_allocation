import unittest
from app.room import OfficeSpace, LivingSpace


class TestCreateRoom(unittest.TestCase):
	"""Test room creation """
	def setUp(self):
		self.office_space = OfficeSpace()
		self.living_space = LivingSpace()
	
	def test_officespace_size(self):
		self.assertEqual(self.office_space.size , 6 ,
			msg ='Maximum capacity is 6 occupants')

	def test_officespace_type(self)
		self.assertEqual(self.office_space.room_type, "OFFICE",
			msg = "Room created should be of type OFFICE")

	def test_officespace_rejects_int(self):
		self.assertRaises(ValueError, self.office_space.name, 111)

	def test_livingspace_size(self):
		self.assertEqual(self.living_space.size, 4, msg = 'Maximum capacity is 4 occupants')

	def test_livingspace_type(self)
		self.assertEqual(self.living_space.room_type, "LIVING SPACE",
			msg = "Room Created should be of type LIVING SPACE")
	
	def test_livingspace_rejects_int(self):
		self.assertRaises(ValueError, self.living_space.name, 111)
