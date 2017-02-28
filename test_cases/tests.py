import unittest

class TestCreateRoom(unittest.TestCase):
	"""Test room creation """

	def setUp(self):
		self.office_space = OfficeSpace()
		self.living_space = LivingSpace()


	def test_office_creation(self):

		self.office_space = OfficeSpace("Office 1")
		self.assertIsInstance(self.office_space, OfficeSpace,
			msg = "'office_space' should be an instance of 'OfficeSpace' class")

		office_capacity = self.office_space.size
		self.assertEqual(office_capacity , 6 ,
			msg ='Maximum capacity is 6 occupants')

	def test_livingspace_creation(self):

		self.living_space = LivingSpace("Rodgen")
		self.assertIsInstance(self.living_space, LivingSpace,
			msg = "'living_space' should be an instance of 'LivingSpace' class")
		)
		living_capacity = self.living_space.size
		self.assertEqual(living_capacity, 4,
			msg = 'Maximum capacity is 4 occupants')




