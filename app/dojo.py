from .person import Person, Fellow, Staff
from .room import OfficeSpace, LivingSpace
import random

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
		if not isinstance (room_type,str) or  not isinstance (room_name, str):
			raise ValueError("Use string values only")
		if room_type.upper() == "OFFICE":
			if room_name in [office.name for office in self.all_offices]:	
				return ("This office already exists!")	
			new_office = OfficeSpace(room_name)
			self.all_offices.append(new_office)
			return ("An {} called {} has been successfully created" .format(room_type, room_name))
		elif room_type.upper() == "LIVINGSPACE":
			if room_name in [livingspace.name for livingspace in self.all_livingspace]:
				return ("This living space already exists!")
			new_livingspace = LivingSpace(room_name)
			self.all_livingspace.append(new_livingspace)
			return ("A {} called {} has been successfully created" .format(room_type, room_name))	
		else:
			return("Invalid room type. Create either 'OFFICE' or 'LIVING SPACE'")
				
	def add_person(self, name, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 

		"""
		if role.upper() == "STAFF":
			new_staff = Staff(name)
			self.all_staff.append(new_staff)
			print ("{} {} has been successfully added" .format(role, name))
			return self.allocate_available_officespace(new_staff)
		elif role.upper() == "FELLOW":
			new_fellow = Fellow(name, wants_accomodation)
			self.all_fellows.append(new_fellow)
			print ("{} {} has been successfully added" .format(role, name))
			print (self.allocate_available_officespace(new_fellow))

			#checks whether fellow wants accomodation
			if new_fellow.wants_accomodation.upper() == "Y":
				return self.allocate_available_livingspace(new_fellow)
		else:
			return ("Invalid role. Specify either FELLOW or STAFF!")
			
	def allocate_available_officespace(self,new_person):
		"""This method gets all available offices, confirms if the
		room has space then allocates an office randomly to either fellow or staff

		"""
		available_office = []

		for office_space in self.all_offices:
			if len(office_space.occupants) < office_space.capacity:
				available_office.append(office_space)
		#loop to check office space to be allocated exists
		if len(available_office) >= 1:
			random_office_space = random.choice(available_office)
			random_office_space.occupants.append(new_person)
			return ("{} has been allocated the office {} " .format(new_person.name, random_office_space.name))
		else:
			return ("No available office space")

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
		if len(available_livingspace) >= 1:
			random_living_space= random.choice(available_livingspace)
			random_living_space.occupants.append(new_person)
			return ("{} has been allocated the livingspace {}" .format(new_person.name, random_living_space.name))
		else:
			return ("No available living space")

