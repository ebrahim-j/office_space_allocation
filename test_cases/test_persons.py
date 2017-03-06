import unittest
from ..app.person import Staff, Fellow

class TestPerson(unittest.TestCase):
	"""Test Person added"""
	def setUp(self):
		self.fellow = Fellow("Maria", "Y")
		self.staff = Staff("Fai")

	def test_person_role_is_fellow(self):
		self.assertEqual(self.fellow.role, 'FELLOW',
			msg = 'Invalid role specified')

	def test_person_role_is_staff(self):
		self.assertEqual(self.staff.role, 'STAFF',
			msg = 'Invalid role specified')

	def test_fellow_valid_accomodation_option(self):
		self.assertEqual(self.fellow.wants_accomodation,
			'Y' or 'N',
			msg = 'Invalid option')

	def test_fellow_name_returns_error_message_if_arg_not_string(self):
		new_fellow = Fellow(123,"Y")
		with self.assertRaises(ValueError):
			new_fellow.name

	def test_staff_name_returns_error_message_if_arg_not_string(self):
		new_staff = Staff(123)
		with self.assertRaises(ValueError):
			new_staff.name

	def test_fellow_accomodation_returns_error_message_if_arg_not_string(self):
		new_fellow = Fellow("maz", 1)
		with self.assertRaises(ValueError):
			new_fellow.role


