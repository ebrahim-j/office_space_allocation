from .person import Person, Fellow, Staff
from .room import OfficeSpace, LivingSpace
import random

"""This file defines all functions for our office space allocation app"""


class Dojo(object):

	def __init__(self):
		self.all_offices = []
		self.all_livingspace = []
		self.all_fellows = []
		self.all_staff = []

	def create_room(self, room_type, room_names):
		"""Create a new room, either office or living space at the Dojo. 
		 Check whether a room with a similar name exits,
		 before succesfully creating the room
		 """
		if room_type.lower() == "office":	
			for room_name in room_names:
				if isinstance(room_name,str):
					name = room_name.lower()
					if name in [office.name for office in self.all_offices]:	#checks if an instance of this room exists
						return ("This office already exists!")
					else:
						new_office = OfficeSpace(name)
						self.all_offices.append(new_office)
						return ("An {} called {} has been successfully created" .format(room_type, name))
				else:
					return ("'room_name' should be a string value!")
		elif room_type.lower() == "living space":
			for room_name in room_names:
				if isinstance(room_name, str):
					name = room_name.lower()
					if name in [livingspace.name for livingspace in self.all_livingspace]:
						return ("This living space already exists!")
					new_livingspace = LivingSpace(name)
					self.all_livingspace.append(new_livingspace)
					return ("A {} called {} has been successfully created" .format(room_type, name))
				else:
					return ("'room_name' should be a string value!")
		else:
			return("Invalid room type. Create either 'OFFICE' or 'LIVING SPACE'")
				
	def add_person(self, name, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 
		"""
		#if wants_accomodation.lower() != "Y" or wants_accomodation.lower() != "N":
		#	print ("Invalid accomodation choice")
		#if checks the role against accomodation option to allocate respective room
		if wants_accomodation.lower() == "y":
			if role.lower() == "fellow":
				new_fellow = Fellow(name, wants_accomodation)
				self.all_fellows.append(new_fellow)
				print ("{} {} has been successfully added" .format(role, name))
				self.allocate_available_officespace(new_fellow)
				self.allocate_available_livingspace(new_fellow)
			elif role.lower() == "staff":
				print ("Staff cannot be assigned Living Space")
		elif wants_accomodation.lower() == "n":
			if role.lower() == "staff":
				new_staff = Staff(name)
				self.all_staff.append(new_staff)
				print (" {} {} has been successfully added" .format(role, name))
				self.allocate_available_officespace(new_staff)
			elif role.lower() == "fellow":
				new_fellow = Fellow(name)
				self.all_fellows.append(new_fellow)
				print ("{} {} has been successfully added" .format(role, name))
				self.allocate_available_officespace(new_fellow)
				self.allocate_available_livingspace(new_fellow)
			
	def allocate_available_officespace(self,new_person):
		"""This method gets all available offices, confirms if the
		room has space then allocates an office randomly to either fellow or staff
		"""
		available_office = []

		for office in self.all_offices:
			if len(office.occupants) < office.capacity:
				available_office.append(office)
		#loop to check office space to be allocated exists
		if len(available_office) >= 1:
			random_office_space = random.choice(available_office)
			random_office_space.occupants.append(new_person)
			print ("{} has been allocated the office {} " .format(new_person.name, random_office_space.name))
		else:
			print ("No available office space")

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
			print ("{} has been allocated the livingspace {}" .format(new_person.name, random_living_space.name))
		else:
			print ("No available living space")


#if __name__ == '__main__':
#	dojo = Dojo()
	#dojo.create_room("office", ["emerald","ruby","perl"])
	#dojo.create_room("living space", ["red", "blue","green"])
	#dojo.add_person("pit","fellow","N")
	#dojo.add_person("matt","staff", "Y")
	#dojo.create_room("space",["A","B"])
	#dojo.create_room(123, ["C","D"])