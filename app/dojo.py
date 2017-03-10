import random
import itertools

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

	def create_room(self, room_type, room_name):
		"""Create a new room, either office or living space at the Dojo. 
		 Check whether a room with a similar name exits,
		 before succesfully creating the room

		 """
		if room_type.upper() == "OFFICE":
			if room_name in [office.name for office in self.all_offices]:	
				return (text_format.CRED + "\nWARNING! This office already exists!\n"
				 +text_format.CEND)	
			new_office = OfficeSpace(room_name)
			self.all_offices.append(new_office)
			return (text_format.CBOLD + "\nAn OFFICE called {} has been successfully created\n"
				.format(room_name)
				+ text_format.CEND)
		elif room_type.upper() == "LIVINGSPACE":
			if room_name in [livingspace.name for livingspace in self.all_livingspace]:
				return (text_format.CRED + "\nWARNING! This livingspace already exists!\n" 
					+text_format.CEND)
			new_livingspace = LivingSpace(room_name)
			self.all_livingspace.append(new_livingspace)
			return (text_format.CBOLD + "\nA LIVING SPACE called {} has been successfully created\n"
				.format(room_name)
				+ text_format.CEND)	
		else:
			return(text_format.CRED + "\nInvalid room type! Create either 'OFFICE' or 'LIVING SPACE'\n"
				+text_format.CEND )
				
	def add_person(self, name, email_address, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 

		"""
		if role.upper() == "STAFF":
			if email_address in [this_staff.email for this_staff in self.all_staff]:
				return (text_format.CRED + "\nWARNING! Staff with this email_address already exists!\n"
					+text_format.CEND)
			new_staff = Staff(name)
			new_staff.email = email_address
			self.all_staff.append(new_staff)
			print (text_format.CBOLD + "\nSTAFF {} has been successfully added\n" 
				.format(name)
				+text_format.CEND)			
			return (self.allocate_available_officespace(new_staff))
		elif role.upper() == "FELLOW":
			if email_address in [this_fellow.email for this_fellow in self.all_fellows]:
				return (text_format.CRED + "\nWARNING! Fellow with this email_address already exists!\n" 
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
			return (text_format.CRED + "\n{} has been allocated the livingspace {} \n" 
				.format(new_person.name, allocated_living_space.name)
				+text_format.CEND)
		else:
			print (text_format.CRED + "\nWARNING!No available LIVING space"+text_format.CEND)
			self.livingspace_waitinglist.append(new_person)
			return (text_format.CRED + "{} has been added to the livingspace waiting list\n" 
				.format(new_person.name)
				+ text_format.CEND)

	def print_room(self, room_name):
		"""This method prints names of all occupants in the
		specified room name

		"""
		output = ''

		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.name == room_name:
				output = ("\n LIST OF ALL OCCUPANTS IN " + room.room_type +  " " + room_name + "\n" + "*" * 50)
				if room.occupants:
					for occupant in room.occupants:
						output += ("\n" + occupant.name + "\t" + occupant.role + "\n")
				else:
					output+= ("\n\n\tThe {} {} has no occupants\n\n".format(room.room_type,room_name))
			else:
				output = ("\n\tThe room {} does not exist!\n" .format(room_name))
			return (text_format.CBOLD + output + text_format.CEND)


	def print_allocations(self,filename=None):

		pass

	def print_unallocated(self,filename=None):


		pass	

		