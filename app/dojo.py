import random
import itertools
import os

from .person import Person, Fellow, Staff
from .room import OfficeSpace, LivingSpace
from text_styles import text_format


"""This file defines all functionalities for our office 
space allocation app

"""


class Dojo(object):

	def __init__(self):
		self.all_offices = []
		self.all_livingspace = []
		self.all_fellows = []
		self.all_staff = []
		self.officespace_waitinglist = []
		self.livingspace_waitinglist = []
		self.status = False

	def create_room(self, room_type, room_name):
		"""Create a new room, either office or living space at the Dojo. 
		 Check whether a room with a similar name exits,
		 before succesfully creating the room

		 """
		if not isinstance (room_type,str) or not isinstance (room_name,str):
			raise ValueError("Can only be a string variable!")

		if room_type.upper() == "OFFICE":
			if room_name in [office.name for office in self.all_offices]:	
				return (text_format.CRED + "\nWARNING! This office already exists!\n"
				 +text_format.CEND)	
			new_office = OfficeSpace(room_name)
			self.all_offices.append(new_office)
			print (text_format.CBOLD + "\nAn OFFICE called {} has been successfully created\n"
				.format(room_name)
				+ text_format.CEND)	
			return (self.allocate_unallocated_person(room_type))	
				

		elif room_type.upper() == "LIVINGSPACE":
			if room_name in [livingspace.name for livingspace in self.all_livingspace]:
				return (text_format.CRED + "\nWARNING! This livingspace already exists!\n" 
					+text_format.CEND)
			new_livingspace = LivingSpace(room_name)
			self.all_livingspace.append(new_livingspace)
			print (text_format.CBOLD + "\nA LIVING SPACE called {} has been successfully created\n"
				.format(room_name)
				+ text_format.CEND)	
			return (self.allocate_unallocated_person(room_type))

		else:
			return(text_format.CRED + "\nInvalid room type! Create either 'OFFICE' or 'LIVING SPACE'\n"
				+text_format.CEND )

	def allocate_unallocated_person(self,room_type):

		successful_allocations = []

		if room_type.upper() == "OFFICE":
			for each_person in self.officespace_waitinglist:
				print (self.allocate_available_officespace(each_person))
				if self.status == True:
					successful_allocations.append(each_person)

			#update officespace_waitinglist
			self.officespace_waitinglist = list(set(self.officespace_waitinglist) - set(successful_allocations))		
			
		elif room_type.upper() == "LIVINGSPACE":
			for each_person in self.livingspace_waitinglist:
				print (self.allocate_available_livingspace(each_person))
				if self.status ==True:
					successful_allocations.append(each_person)
			#update livingspace_waitinglist
			self.livingspace_waitinglist = list(set(self.livingspace_waitinglist) - set(successful_allocations))
		
		return
					
	def add_person(self, name, email_address, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 

		"""
		if role.upper() == "STAFF":
			if email_address in [this_member.email for this_member 
			in itertools.chain(self.all_staff,self.all_fellows)]:
				return (text_format.CRED + "\nWARNING! STAFF or FELLOW with this email_address already exists!\n"
					+text_format.CEND)
			new_staff = Staff(name)
			new_staff.email = email_address
			self.all_staff.append(new_staff)
			print (text_format.CBOLD + "\nSTAFF {} has been successfully added\n" 
				.format(name)
				+text_format.CEND)			
			print (self.allocate_available_officespace(new_staff))
		elif role.upper() == "FELLOW":
			if email_address in [this_member.email for this_member 
			in itertools.chain(self.all_staff,self.all_fellows)]:
				return (text_format.CRED + "\nWARNING! STAFF or FELLOW with this email_address already exists!\n"
					+text_format.CEND)
			new_fellow = Fellow(name, wants_accomodation)
			new_fellow.email = email_address
			self.all_fellows.append(new_fellow)
			print (text_format.CBOLD + "\nFELLOW {} has been successfully added\n" .format(name)
				+text_format.CEND)
			print (self.allocate_available_officespace(new_fellow))

			#checks whether fellow wants accomodation
			if new_fellow.wants_accomodation== "y":
				return (self.allocate_available_livingspace(new_fellow))
						
		else:
			return (text_format.CRED+"\nInvalid role! Specify either FELLOW or STAFF!\n"
				+text_format.CEND)
			
	def allocate_available_officespace(self,new_person):
		"""This method gets all available offices, confirms if the
		room has space then allocates an office randomly to either fellow or staff

		"""
		available_office = []

		for office_space in self.all_offices:
			if len(office_space.occupants) < office_space.capacity:
				available_office.append(office_space)
		
		#loop to check office space to be allocated exists
		if available_office:
			allocated_office_space = random.choice(available_office)
			allocated_office_space.occupants.append(new_person)
			self.status = True
			return (text_format.CBOLD + "\n{} has been allocated the office {} \n" 
				.format(new_person.name, allocated_office_space.name)
				+text_format.CEND)
		else:
			print (text_format.CRED + "\nWARNING!No available OFFICE space"+text_format.CEND)
			self.officespace_waitinglist.append(new_person)
			return (text_format.CGREEN +"{} has been added to the officespace waiting list\n" 
				.format(new_person.name)
				+ text_format.CEND)

	def allocate_available_livingspace(self, new_person):
		"""This method gets all available living space, confirms if the
		room has space then allocates living space randomly to fellow who requires
		accomodation

		"""
		available_livingspace = []
		for living_space in self.all_livingspace:
			if len(living_space.occupants) < living_space.capacity:
				available_livingspace.append(living_space)
		#loop checks vacant livingspace to be allocated
		if available_livingspace:
			allocated_living_space= random.choice(available_livingspace)
			allocated_living_space.occupants.append(new_person)
			self.status = True
			return (text_format.CBOLD + "\n{} has been allocated the livingspace {} \n" 
				.format(new_person.name, allocated_living_space.name)
				+text_format.CEND)
		else:
			print (text_format.CRED + "\nWARNING!No available LIVING space"+text_format.CEND)
			self.livingspace_waitinglist.append(new_person)
			return (text_format.CGREEN + "{} has been added to the livingspace waiting list\n" 
				.format(new_person.name)
				+ text_format.CEND)

	def print_room(self, room_name):
		"""This method prints names of all occupants in the
		specified room name

		"""
		output = ""

		if not room_name in [room.name for room in itertools.chain(self.all_offices, self.all_livingspace)]:
			output = ("\n\tThe room {} does not exist!\n" .format(room_name))

		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.name == room_name:
				output = ("\n LIST OF ALL OCCUPANTS IN " + room.room_type +  " " + room_name + "\n" + "*" * 50)
				if room.occupants:
					for occupant in room.occupants:
						output += ("\n" + occupant.name + "\t" + occupant.role + "\n")
				else:
					output+= ("\n\n\tThe {} {} has no occupants\n\n".format(room.room_type,room_name))

		return (text_format.CBOLD + output + text_format.CEND)

	def print_allocations(self,filename=None):
		"""This method prints a list of all allocations at the Dojo. The registered
		allocations can then be written to the specified text file

		"""
		output = ""

		if not self.all_offices and not self.all_livingspace:
			return (text_format.CBOLD + "\n\nThere are currently no rooms to allocate.\n\n"
				+text_format.CEND)

		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.occupants:
				output += ("\n\nROOM NAME: {} \tTYPE: {} " .format(room.name, room.room_type))
				output += ("\n" + "-" * 40 + "\n")
				for occupant in room.occupants:
					output += (occupant.name + "-" + occupant.role + ", ")
			else:
				output = ("\n There are empty rooms. Add new Staff or Fellows to allocate\n\n")

		if filename == None:
			return (text_format.CBOLD + output + text_format.CEND)
		else:
			print("Saving output data to file...")
			txt_file = open(filename + ".txt", "w+")
			txt_file.write(output)
			txt_file.close()
			return ("\nData has been successfully saved to {}.txt\n" .format(filename))
			
	def print_unallocated(self,filename=None):
		"""This method prints a list of all staff and fellows,
		that have not been allocated any office or living space.

		"""
		output = ""

		if not self.officespace_waitinglist and not self.livingspace_waitinglist:
			return (text_format.CBOLD + "\nThere are currently no unallocated Fellows or Staff.\n\n" 
				+text_format.CEND)
		else:
			output = (text_format.CBOLD + "\n\n LIST OF ALL UNALLOCATED STAFF AND FELLOWS\n" 
				+ "*" * 50 + "\n" + text_format.CEND)
			for person in self.officespace_waitinglist:
				output += (text_format.CBOLD + person.name + " \t" + person.email + "\t" + person.role 
					+ "\t" + text_format.CEND 
					+ text_format.CRED + "OFFICE SPACE" +text_format.CEND + "\n")
			for person in self.livingspace_waitinglist:
				output += (text_format.CBOLD + person.name + " \t" + person.email + "\t" + person.role 
					+ "\t" + text_format.CEND
					+text_format.CGREEN + "LIVING SPACE" +text_format.CEND + "\n")

		if filename == None:
			return (output)
		else:
			print ("Saving unallocations list to file...")
			txt_file = open(filename + ".txt", "w+")
			txt_file.write(output)
			txt_file.close()
			return ("\nData has been successfully saved to {}.txt\n" .format(filename))

	def reallocate_person(self, emailaddress, new_roomname):
		"""This method reallocates a person using their unique identifier,
		in this case their email address, to a the specified new room

		"""
		#unique_identifier = emailaddress
		new_room = None
		new_room_vacant = False
		person_reallocating = None
		found_emailaddress = False

		#check if a person with the email address exists
		for member in itertools.chain(self.all_staff,self.all_fellows):
			if member.email == emailaddress:
				person_reallocating = member

		if person_reallocating is None:
			return (text_format.CRED + "\nCould not find person with email {}!\n"
				.format(emailaddress)
				+ text_format.CEND)

		#checks if the room exists
		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.name == new_roomname:
				new_room = room	

		if new_room is None:
			return (text_format.CRED + "\nThe room {} does not exist!\n"
				.format(new_roomname)
				+ text_format.CEND)

		#check if the room is vacant
		if new_room.room_type == "OFFICE" and len(new_room.occupants) < 6:
			new_room_vacant = True
					
		if new_room.room_type == "LIVINGSPACE" and len(new_room.occupants) < 4:
			new_room_vacant = True

		if new_room_vacant is False:
			return (text_format.CRED + "\nThe room {} is full! Cannot reallocate {}-{}!\n"
				.format(new_roomname, person_reallocating.role, person_reallocating.name)
				+ text_format.CEND)


		"""for this_room in itertools.chain(self.all_offices, self.all_livingspace):
									for occupant in this_room.occupants:
										if occupant.email == emailaddress:
											person_reallocating = occupant
											print ("email address {} associated with {} {} has been found."
												.format(emailaddress, occupant.role, occupant.name))
											current_room_allocation_type = this_room.room_type
											current_room_allocation_name =this_room.name"""

	def load_people(self, filename):
		"""This method adds people to rooms from a txt file.
		The text input from the text file should have the following format
		NAME EMAIL ROLE ACCOMODATION_OPTION

		"""
		if os.path.isfile(filename + ".txt"):
			if os.stat(filename + ".txt").st_size:
				with open(filename + ".txt") as input_file:
					for line in input_file:
						read_line = line.split()
						if len(read_line) > 4 or len(read_line) < 3:
							print (text_format.CRED + "\nInvalid entry!\n" + text_format.CEND)
						try:
							name = read_line[0]
							email = read_line[1]
							role = read_line[2]
							accomodation_option = read_line[3]
						except IndexError:
							accomodation_option = "N"

						self.add_person(name, email, role, accomodation_option)
						
			else:
				print (text_format.CRED + "\nThe file {}.txt is empty!\n".format(filename) 
					+text_format.CEND )
		else:
			print (text_format.CRED + "\nThe file {}.txt does not exist!\n".format(filename) 
				+text_format.CEND)					

		return


		