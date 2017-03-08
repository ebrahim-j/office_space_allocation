import random

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

	def create_room(self, room_type, room_name):
		"""Create a new room, either office or living space at the Dojo. 
		 Check whether a room with a similar name exits,
		 before succesfully creating the room

		 """
		if room_type.upper() == "OFFICE":
			if room_name in [office.name for office in self.all_offices]:	
				return (text_format.CRED + "\nWARNING! This office already exists!\n" +text_format.CEND)	
			new_office = OfficeSpace(room_name)
			self.all_offices.append(new_office)
			return (text_format.CBOLD + "\nAn OFFICE called {} has been successfully created\n".format(room_name)
				+ text_format.CEND)
		elif room_type.upper() == "LIVINGSPACE":
			if room_name in [livingspace.name for livingspace in self.all_livingspace]:
				return (text_format.CRED + "\nWARNING! This livingspace already exists!\n" +text_format.CEND)
			new_livingspace = LivingSpace(room_name)
			self.all_livingspace.append(new_livingspace)
			return (text_format.CBOLD + "\nA LIVING SPACE called {} has been successfully created\n".format(room_name)
				+ text_format.CEND)	
		else:
			return(text_format.CRED + "\nInvalid room type! Create either 'OFFICE' or 'LIVING SPACE'\n"+text_format.CEND )
				
	def add_person(self, name, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 

		"""
		if role.upper() == "STAFF":
			new_staff = Staff(name)
			self.all_staff.append(new_staff)
			print (text_format.CBOLD + "\nSTAFF {} has been successfully added\n" .format(name)
				+text_format.CEND)
			return self.allocate_available_officespace(new_staff)
		elif role.upper() == "FELLOW":
			new_fellow = Fellow(name, wants_accomodation)
			self.all_fellows.append(new_fellow)
			print (text_format.CBOLD + "\nFELLOW {} has been successfully added\n" .format(name)
				+text_format.CEND)
			print (self.allocate_available_officespace(new_fellow))

			#checks whether fellow wants accomodation
			if new_fellow.wants_accomodation.upper() == "Y":
				print (self.allocate_available_livingspace(new_fellow))
		else:
			return (text_format.CRED + "\nInvalid role! Specify either FELLOW or STAFF!\n"+text_format.CEND)
			
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
			return (text_format.CBOLD + "\n{} has been allocated the office {} \n" \
				.format(new_person.name, allocated_office_space.name)
				+text_format.CEND)
		else:
			return (text_format.CRED + "\nWARNING!No available OFFICE space\n"+text_format.CEND)

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
			return (text_format.CBOLD + "\n{} has been allocated the livingspace {} \n" \
				.format(new_person.name, allocated_living_space.name)
				+text_format.CEND)
		else:
			return (text_format.CRED + "\nWARNING!No available LIVING space\n"+text_format.CEND)
