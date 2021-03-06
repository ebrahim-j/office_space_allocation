import unittest
import os

from ..app.dojo import Dojo


class TestDojoFunctionalities(unittest.TestCase):
	"""This class contains test methods for functionalities
	defined in dojo.py file"""

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
		expected_output =("\x1b[1m\n LIST OF ALL OCCUPANTS IN OFFICE Green\n" 
			+ "*" * 50 + "\n\n\tThe OFFICE Green has no occupants\n\n\x1b[0m") 
		self.assertEqual(output, expected_output)

	def test_print_room_returns_error_message_if_room_doesnot_exist(self):
		self.the_dojo.create_room("office","blue")
		self.assertEqual(self.the_dojo.print_room("red"),
		 "\x1b[1m\n\tThe room red does not exist!\n\x1b[0m")

	def test_print_room_prints_all_occupants_if_room_is_office(self):
		self.the_dojo.create_room("office","Purple")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_room("Purple")
		expected_output =("\x1b[1m\n LIST OF ALL OCCUPANTS IN OFFICE Purple\n" 
			+ "*" * 50 + "\n" 
			+ "Pete" + "\t" + "STAFF" + "\n\x1b[0m")
		self.assertEqual(output, expected_output)

	def test_print_room_prints_all_occupants_if_room_is_livingspace(self):
		self.the_dojo.create_room("livingspace", "Ruby")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		output = self.the_dojo.print_room("Ruby")
		expected_output = ("\x1b[1m\n LIST OF ALL OCCUPANTS IN LIVING SPACE Ruby\n" 
			+ "*" * 50 + "\n" 
			+ "Marie" + "\t" + "FELLOW" + "\n\x1b[0m")
		self.assertEqual(output, expected_output)

	def test_print_allocations_with_filename_unspecified(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_allocations()
		expected_output = ("\x1b[1m\n\nROOM NAME: Red \tTYPE: OFFICE " + "\n" + "-" * 40
			+ "\nMarie-FELLOW, Pete-STAFF, \033[0m")
		self.assertEqual(output, expected_output)

	def test_print_allocations_with_filename_specified(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.create_room("livingspace", "Ruby")
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_allocations("file1")
		expected_output = "\033[1m \nData has been successfully saved to file1.txt\n \033[0m"
		self.assertEqual(output, expected_output)
		os.remove("file1.txt")

	def test_print_allocations_if_filepath_exists(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.print_allocations("file1")
		self.assertTrue(os.path.isfile("file1.txt"))
		os.remove("file1.txt")

	def test_print_unallocated_with_filename_unspecified(self):
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_unallocated()
		expected_output = ("\x1b[1m\n\n LIST OF ALL UNALLOCATED STAFF AND FELLOWS\n" 
			+ "*" * 50 + "\n"
			+ "Marie\tmarie@marie.com\tFELLOW\t\x1b[31mOFFICE SPACE\x1b[0m\n" 
			+ "Pete\tpete@pete\tSTAFF\t\x1b[31mOFFICE SPACE\x1b[0m\n"
			+ "\x1b[1mMarie\tmarie@marie.com\tFELLOW\t\x1b[32mLIVING SPACE\x1b[0m\n\x1b[0m" )
		self.assertEqual(output, expected_output)
			
	def test_print_unallocated_with_filename_specified(self):
		self.the_dojo.add_person("Marie", "marie@marie.com","Fellow", "y")
		self.the_dojo.add_person("Pete","pete@pete","Staff")
		output = self.the_dojo.print_unallocated("file2")
		expected_output = "\x1b[1m \nData has been successfully saved to file2.txt\n \x1b[0m"
		self.assertEqual(output, expected_output)
		os.remove("file2.txt")

	def test_reallocate_person_returns_error_if_room_doesnot_exist(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		result =self.the_dojo.reallocate_person("pete@pete", "Green")
		self.assertEqual(result, "\x1b[31m\nThe room Green does not exist!\n\x1b[0m")

	def test_reallocate_person_successfully_reallocates_person(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.create_room("office", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Green"]
		count_before_reallocation = len(room_occupancy[0])
		self.the_dojo.reallocate_person("pete@pete", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Green"]
		count_after_reallocation = len(room_occupancy[0])
		self.assertEqual(count_after_reallocation - count_before_reallocation, 1, 
			msg = "Reallocation was unsuccessful!" )

	def test_reallocate_person_moves_person_from_previous_allocation(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.create_room("office", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Red"]
		count_before_reallocation = len(room_occupancy[0])
		self.the_dojo.reallocate_person("pete@pete", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Red"]
		count_after_reallocation = len(room_occupancy[0])
		self.assertEqual(count_before_reallocation - count_after_reallocation, 1, 
			msg = "Reallocation was unsuccessful!" )
		
	def test_reallocate_person_doesnot_reallocate_staff_to_livingspace(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.create_room("livingspace", "Crimson")
		result = self.the_dojo.reallocate_person("pete@pete", "Crimson")
		self.assertEqual(result, "\x1b[1m\nCannot reallocate STAFF to LIVING SPACE!\n\x1b[0m")

	def test_reallocate_person_doesnot_reallocate_if_room_is_full(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.add_person("Matt", "matt@matt", "staff")
		self.the_dojo.add_person("Patt", "patt@patt", "fellow")
		self.the_dojo.add_person("Faith", "faith@faith", "staff")
		self.the_dojo.add_person("Fait", "fait@fait", "fellow", "y")
		self.the_dojo.add_person("Fai", "fai@fai", "staff")
		self.the_dojo.create_room("office", "Green")
		self.the_dojo.add_person("Marie", "maz@maz", "fellow","y")
		result = self.the_dojo.reallocate_person("maz@maz", "Red")
		self.assertEqual(result, "\x1b[31m\nThe room Red is full! Cannot reallocate FELLOW-Marie!\n\x1b[0m")

	def test_reallocate_person_can_reallocate_a_fellow(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Josh", "josh@josh", "fellow", "y")
		self.the_dojo.create_room("office", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Green"]
		count_before_reallocation = len(room_occupancy[0])
		self.the_dojo.reallocate_person("josh@josh", "Green")
		room_occupancy = [room.occupants for room in self.the_dojo.all_offices\
		 if room.name == "Green"]
		count_after_reallocation = len(room_occupancy[0])
		self.assertEqual(count_after_reallocation - count_before_reallocation, 1, 
			msg = "Reallocation was unsuccessful!" )

	def test_reallocate_person_reallocates_fellow_to_livingspace(self):
		self.the_dojo.create_room("office","Red")
		self.the_dojo.create_room("livingspace", "Crimson")
		self.the_dojo.add_person("Matt","matt@matt", "fellow", "y")
		self.the_dojo.create_room("livingspace","Emerald")
		room_occupancy = [room.occupants for room in self.the_dojo.all_livingspace\
		 if room.name == "Emerald"]
		count_before_reallocation = len(room_occupancy[0])
		self.the_dojo.reallocate_person("matt@matt", "Emerald")
		room_occupancy = [room.occupants for room in self.the_dojo.all_livingspace\
		 if room.name == "Emerald"]
		count_after_reallocation = len(room_occupancy[0])
		self.assertEqual(count_after_reallocation - count_before_reallocation, 1, 
			msg = "Reallocation was unsuccessful!" )

	def test_reallocate_person_returns_error_for_non_existent_person(self):
		self.the_dojo.create_room("office","Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.create_room("office","blue")
		result = self.the_dojo.reallocate_person("pat@pat", "blue")
		self.assertEqual(result, "\x1b[31m\nCould not find person with email pat@pat!\n\x1b[0m")


	def test_load_people_successfully(self):
		with open("LoadFile.txt", "w+") as input_file:
			input_file.write("RANDY RANDY@RANDY STAFF\n")
			input_file.write("TYRESE TY@TY FELLOW Y\n")
			input_file.write("HEATHER HEATH@HEATH FELLOW")

		initial_staff_count = len(self.the_dojo.all_staff)
		initial_fellow_count = len(self.the_dojo.all_fellows)
		self.the_dojo.load_people("LoadFile")
		final_staff_count = len(self.the_dojo.all_staff)
		final_fellow_count = len(self.the_dojo.all_fellows)
		self.assertEqual(final_staff_count - initial_staff_count, 1,
			msg = "Error loading Staff")
		self.assertEqual(final_fellow_count - initial_fellow_count, 2,
			msg = "Error Loading Fellows")

	def test_load_people_returns_error_if_file_is_empty(self):
		text_file = open("LoadFile" + ".txt", "w+")
		text_file.close()
		result = self.the_dojo.load_people("LoadFile.txt")
		self.assertEqual(result, "\x1b[31m\nThe file LoadFile.txt.txt does not exist!\n\x1b[0m")

	def test_load_people_filepath_exists(self):
		self.the_dojo.load_people("LoadFile")
		self.assertTrue(os.path.isfile("LoadFile.txt"))
		os.remove("LoadFile.txt")		

	def test_save_state_database_file_exists(self):
		self.the_dojo.save_state("sampleDB")
		self.assertTrue(os.path.isfile("sampleDB.db"))
		os.remove("sampleDB.db")

	def test_save_and_load_room_data_to_DB(self):
		self.the_dojo2 = Dojo()
		self.the_dojo.create_room("office", "Red")
		self.the_dojo2.create_room("livingspace", "Ruby")
		self.the_dojo.save_state("sampleDB")
		
		self.the_dojo2.load_state("sampleDB")
		self.assertEqual(len(self.the_dojo2.all_offices), 1)
		self.assertEqual(len(self.the_dojo2.all_livingspace), 1)

	def test_save_and_load_persons_data_to_DB(self):
		self.the_dojo2 = Dojo()
		self.the_dojo.add_person("Pete","pete@pete","staff")
		self.the_dojo.add_person("Tye", "ty@ty", "fellow", "y")
		self.the_dojo.save_state("sampleDB")

		self.the_dojo2.load_state("sampleDB")
		self.assertEqual(len(self.the_dojo2.all_fellows), 1)
		self.assertEqual(len(self.the_dojo2.all_staff), 1)

	def test_load_state_database_file_exists(self):
		self.the_dojo.create_room("office", "Red")
		self.the_dojo.add_person("Pete", "pete@pete", "staff")
		self.the_dojo.save_state("sampleDB")
		self.the_dojo2 = Dojo()
		self.the_dojo2.load_state("sampleDB")
		self.assertTrue(os.path.isfile("sampleDB.db"))
		os.remove("sampleDB.db")

	def test_load_state_returns_error_when_wrong_DB_is_specified(self):
		self.assertEqual(self.the_dojo.load_state("anotherDB"),
		 "\x1b[31m\nThe database anotherDB.db does not exist!\n\x1b[0m")
	
