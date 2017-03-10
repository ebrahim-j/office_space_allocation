import unittest
import os

from ..app.dojo import Dojo


class TestDojoFunctionalities(unittest.TestCase):

	def setUp(self):
		self.the_dojo = Dojo()

	def test_officespace_creation(self):
		initial_count_offices = len(self.the_dojo.all_offices)
		self.the_dojo.create_room("office", "Red")
		new_count_offices = len(self.the_dojo.all_offices) 
		self.assertEqual(new_count_offices - initial_count_offices, 1, 
			msg = 'No new office created')

	def test_livingspace_creation(self):
		initial_count_livingspace = len(self.the_dojo.all_livingspace)
		self.the_dojo.create_room("livingspace", "Emerald")
		new_count_livingspace = len(self.the_dojo.all_livingspace)
		self.assertEqual(new_count_livingspace - initial_count_livingspace, 1, 
			msg = 'No new living space created')

	def test_adding_fellow(self):
		initial_count_fellows = len(self.the_dojo.all_fellows)
		self.the_dojo.add_person("Barney", "barney@barney.com","FELLOW", "N")
		new_count_fellows= len(self.the_dojo.all_fellows)
		self.assertEqual(new_count_fellows - initial_count_fellows, 1, 
			msg = 'Failed to add new Fellow')		

	def test_adding_staff(self):
		initial_count_staff = len(self.the_dojo.all_staff)
		self.the_dojo.add_person("Louis", "louis@louis", "Staff")
		new_count_staff= len(self.the_dojo.all_staff)
		self.assertEqual(new_count_staff - initial_count_staff, 1, 
			msg = 'Failed to add new Staff')

	def test_create_room_returns_error_message_if_roomtype_not_string(self):
		with self.assertRaises(ValueError):
			self.the_dojo.create_room(123,"blue")

	def test_create_room_returns_error_message_if_roomname_not_string(self):
		with self.assertRaises(ValueError):
			self.the_dojo.create_room("OFFICE",123)
	
	def test_print_room_returns_error_message_if_room_is_empty(self):
		self.the_dojo.create_room("office","Green")
		output = self.the_dojo.print_room("Green")
		self.assertEqual(output, "The OFFICE Green has no occupants")

	def test_print_room_returns_error_message_if_room_doesnot_exist(self):
		self.the_dojo.create_room("office","blue")
		self.assertEqual(self.the_dojo.print_room("red"), "The room red does not exist!")

	def test_print_room_prints_all_occupants_if_room_is_office(self):
		self.the_dojo.create_room("office","Purple")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_room("Purple")
		expected_output =("\n LIST OF ALL OCCUPANTS IN OFFICE Purple\n" + "*" * 40 
			+ "\n" + "Pete" + "\t" + "STAFF" + "\n")
		self.assertEqual(output, expected_output)

	def test_print_room_prints_all_occupants_if_room_is_livingspace(self):
		self.the_dojo.create_room("livingspace", "Ruby")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		output = self.the_dojo.print_room("Ruby")
		expected_output = ("\n LIST OF ALL OCCUPANTS IN LIVING SPACE Ruby\n" + "*" * 40 + "\n" 
			+ "Marie" + "\t" + "FELLOW" + "\n")
		self.assertEqual(output, expected_output)

	def test_print_allocations_with_filename_unspecified(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_allocations()
		expected_output = ("\n\n\tRed\t" + "OFFICE\n" + "-" * 50 
			+ "\n\tMarie - FELLOW, Pete - STAFF,\n")
		self.assertEqual(output, expected_output)

	def test_print_allocations_with_filename_specified(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.create_room("livingspace", "Ruby")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_allocations("file1")
		expected_output = "\nData has been successfully saved to file1.txt\n"
		self.assertEqual(output, expected_output)

	def test_print_allocations_if_filepath_exists(self):
		self.the_dojo.print_allocations("file1")
		self.assertTrue(os.path.isfile("file1.txt"))
		os.remove("file1.txt")

	def test_print_unallocated_with_filenamed_unspecified(self):
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_unallocated()
		expected_output = ("\n\n\tUNALLOCATED PEOPLE\n" + "*" * 50 
			+ "\n\tMarie\tmarie@marie.com\tFellow\ty \n" 
			+ "\n\tPete\tpete@pete.com\tStaff ")
		self.assertEqual(output, expected_output)
			
	def test_print_unallocated_with_filename_specified(self):
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_unallocated("file1")
		expected_output = "\nData has been successfully saved to file2.txt\n"
		self.assertEqual(output, expected_output)

	def test_if_print_unallocated_filepath_exists(self):
		self.the_dojo.print_unallocated("file2")
		self.assertTrue(os.path.isfile("file2.txt"))
		os.remove("file2.txt")





