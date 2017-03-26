import unittest
from ..app.person import Staff, Fellow

class TestPerson(unittest.TestCase):
	"""Test instance of Person added"""
	
	def setUp(self):
		self.fellow = Fellow("Maria", "maz@maz" "Y")
		self.staff = Staff("Fai", "fai@fai")

	def test_person_role_is_fellow(self):
		self.assertEqual(
			self.fellow.role, 'FELLOW' ,
			msg = 'Invalid role specified')

	def test_person_role_is_staff(self):
		self.assertEqual(
			self.staff.role, 'STAFF',
			msg = 'Invalid role specified')

	def test_staff_invalid_accomodation_option(self):
		self.assertEqual(
			self.staff.wants_accomodation,'N',
			msg = 'Invalid option')

	


