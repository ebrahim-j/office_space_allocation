"""This file defines all functions for our office space allocation app"""
from person import Person, Fellow, Staff
from room import OfficeSpace, LivingSpace


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
		if rm_type.lower() == "office"	
			for i in rm_names:
				if isinstance(i,str):
					name = i.lower()
					if name in [office.name for office in self.all_offices]:
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
				
	def add_person(self, name, role, wants_accomodation='N'):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 
		"""
		if role.lower() == "staff":
			new_staff = Staff(name)
			self.all_staff.append(new_staff)
			print (" {} {} has been successfully added" .format(role, name))
			self.allocate_room(new_staff)
		elif role.lower() == "fellow":
			new_fellow = Fellow(name, wants_accomodation)
			self.all_fellows.append(new_fellow)
			print ("{} {} has been successfully added" .format(rm_type, rm_name))
			self.allocate_room(new_fellow)
		else:
			return ("You can only be staff or fellow at the Dojo")

	def allocate_room(person):
		pass
	


