from person import Person, Fellow, Staff
from room import OfficeSpace, LivingSpace

"""This file defines all functions for our office space allocation app"""

class Dojo(object):

	def __init__(self):
		self.all_offices = []
		self.all_livingspace = []
		self.all_fellows = []
		self.all_staff = []


	def create_room(self, rm_type, rm_names):
		"""Create a new room, either office or living space at the Dojo. 
		 Check whether a room with a similar name exits,
		 before succesfully creating the room
		 """
		if rm_type.lower() == "office":	
			for i in rm_names:
				if isinstance(i,str):
					name = i.lower()
					if name in [office.name for office in self.all_offices]:	#checks if an instance of this room exists
						return ("This office already exists!")
					new_office = OfficeSpace(name)
					self.all_offices.append(new_office)
					return ("An {} called {} has been successfully created" .format(rm_type, name))
				else:
					return ("'room_name' should be a string value!")
		elif rm_type.lower() == "living space":
			for i in rm_names:
				if isinstance(i, str):
					name = i.lower()
					if name in [livingspace.name for livingspace in self.all_livingspace]:
						return ("This living space already exists!")
					new_livingspace = LivingSpace(name)
					self.all_livingspace.append(new_livingspace)
					return ("A {} called {} has been successfully created" .format(rm_type, name))
				else:
					return ("'room_name' should be a string value!")

				
	def add_person(self, name, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 
		"""
		if wants_accomodation.lower() != "Y" or wants_accomodation.lower() != "N":
			return ("Invalid accomodation choice")
		#if checks the role against accomodation option to allocate respective room
		if wants_accomodation.lower() == "y":
			if role.lower() == "fellow":
				new_fellow = Fellow(name, wants_accomodation)
				self.all_fellows.append(new_fellow)
				return ("{} {} has been successfully added" .format(rm_type, rm_name))
				self.allocate_available_officespace(new_fellow)
				self.allocate_available_livingspace(new_fellow)
			elif role.lower() == "staff":
				return "Staff cannot be assigned Living Space"
		elif wants_accomodation.lower() == "n":
			if role.lower() == "staff":
				new_staff = Staff(name)
				self.all_staff.append(new_staff)
				return (" {} {} has been successfully added" .format(role, name))
				self.allocate_available_officespace(new_staff)
			elif role.lower() == "fellow":
				new_fellow = Fellow(name)
				self.all_fellows.append(new_fellow)
				return ("{} {} has been successfully added" .format(rm_type, rm_name))
				self.allocate_available_officespace(new_fellow)
				self.allocate_available_livingspace(new_fellow)
				
			
	def allocate_available_officespace(self,person):
		"""This method gets all available offices, confirms if the
		room has space then allocates an office randomly to either fellow or staff
		"""
		available_office = []

		for of in self.all_offices:
			if len(of.occupants) < OfficeSpace.capacity:
				available_office.append(of)
		#loop to check office space to be allocated exists
		if available_office >= 1
			random_office_space = random.choice(available_office)
			random_office_space.occupants.append(person)
			return ("{} has been allocated the office {} " .format(person.name, random_office_space))
		else:
			return ("No available office space")

	def allocate_available_livingspace(self, person):
		"""This method gets all available living space, confirms if the
		room has space then allocates living space randomly to fellow who requires
		accomodation
		"""
		available_livingspace = []
		for living in self.all_livingspace:
			if len(living.occupants) < LivingSpace.capacity:
				available_livingspace.append(living)
		#loop checks vacant livingspace to be allocated
		if available_livingspace >= 1
			random_living_space= random.choice(available_livingspace)
			random_living_space.occupants.append(person)
			return ("{} has been allocated the livingspace {}" .format(person.name, random_living_space))
		else:
			return ("No available living space")