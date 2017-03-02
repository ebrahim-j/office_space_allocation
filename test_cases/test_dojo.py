import unittest
from app.dojo import Dojo

	def setUp(self):
		the_dojo = Dojo()

	def test_officespace_creation(self):
		initial_count_offices = len(self.the_dojo.all_offices)
		self.the_dojo.create_room("office", "Red")
		new_count_offices = len(self.the_dojo.all_offices) 
		self.assertEqual(new_count_offices - initial_count_offices, 1, 
			msg = 'No new office created')

	def test_livingspace_creation(self):
		initial_count_ls = len(self.the_dojo.all_livingspace)
		self.the_dojo.create_room("livingspace", "Emerald")
		new_count_ls = len(self.the_dojo.all_livingspace)
		self.assertEqual(new_count_ls - initial_count_ls , 1, 
			msg = 'No new living space created')

	def test_adding_fellow(self):
		initial_count_fellows = len(self.the_dojo.total_fellows)
		new_fellow = self.the_dojo.add_person("Barney", "FELLOW", "N")
		self.assertTrue(new_fellow)
		new_count_fellows= len(self.the_dojo.total_fellows)
		self.assertEqual(new_count_fellows - initial_count_fellows, 1, 
			msg = 'Failed to add new Fellow')		

	def test_adding_staff(self):
		initial_count_staff = len(self.the_dojo.total_staff)
		new_staff = self.staff.add_person("Louis", "STAFF")
		self.assertTrue(new_staff)
		new_count_staff= len(self.the_dojo.total_staff)
		self.assertEqual(new_count_staff - initial_count_staff, 1, 
			msg = 'Failed to add new Staff')