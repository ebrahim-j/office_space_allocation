import unittest
from app.person import Staff, Fellow

class TestPerson(unittest.TestCase):
	"""Test Person added"""
	def setUp(self):
		self.fellow = Fellow("Maria", "FELLOW", "Y")
		self.staff = Staff("Fai", "STAFF")

	def test_person_is_fellow(self):
		self.assertEqual(self.fellow.role, 'FELLOW',
			msg = 'Invalid role specified')

	def test_person_is_staff(self):
		self.assertEqual(self.staff.role, 'STAFF',
			msg = 'Invalid role specified')

	def test_fellow_valid_accomodation_option(self):
		self.assertEqual(self.fellow.wants_accomodation,
			'Y' or 'N',
			msg = 'Invalid option')

	def test_staff_name_rejects_int(self):
		self.assertRaises(ValueError, 
			self.staff.name, 123)

	def test_fellow_name_rejects_int(self):
		self.assertRaises(ValueError, 
			self.fellow.name, 123)


