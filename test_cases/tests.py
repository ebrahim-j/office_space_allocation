import unittest

class TestCreateRoom(unittest.TestCase):
	"""Test room creation """

	def setUp(self):
		self.office_space = OfficeSpace()
		self.living_space = LivingSpace()


	def test_officespace_creation(self):
		initial_count_offices = len(self.office_space.total)
		self.office_space.create_new("Office 1")
		new_count_offices = len(self.office_space.total) 
		self.assertEqual(new_count_offices - initial_count_offices, 1, 
			msg = 'No new office created')
	

	def test_officespace_size_type(self):
		self.assertEqual(self.office_space.size , 6 ,
			msg ='Maximum capacity is 6 occupants')

		self.assertEqual(self.office_space.room_type, "OFFICE",
			msg = "Room created should be of type OFFICE")


	def test_officespace_accepts_str(self):
		self.assertRaises(ValueError, self.office_space.create_new, 111)



	def test_livingspace_creation(self):

		initial_count_ls = len(self.living_space.total)
		self.living_space.create_new("Rodgen")
		new_count_ls = len(self.office_space.total)
		self.assertEqual(new_count_ls - initial_count_ls , 1, 
			msg = 'No new Living space created')


	def test_livingspace_size_type(self):

		self.assertEqual(self.living_space.size, 4, msg = 'Maximum capacity is 4 occupants')

		self.assertEqual(self.living_space.room_type, "LIVING SPACE",
			msg = "Room Created should be of type LIVING SPACE")

	
	def test_livingspace_accepts_str(self):
		self.assertRaises(ValueError, self.living_space.create_new, 111)


class TestPerson(unittest.TestCase):
	"""Test Person added"""

	def setUp(self):
		self.new_fellow = Fellow()
		self.new_staff = Staff()

	def test_adding_fellow(self):
		self.new_fellow.add()