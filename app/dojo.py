from person import Person, Fellow, Staff
from room import OfficeSpace, LivingSpace


class Dojo(object):

	def __init__(self):
		self.all_offices = []
		self.all_livingspace = []
		self.all_fellows = []
		self.all_staff = []

	def create_room(self, rm_type, rm_name):
		"""Create a new room at the Dojo"""
		if rm_type.lower() == 'office':
			if not rm_name in self.all_offices:
				new_office = OfficeSpace(rm_name)
				self.all_offices.append(new_office)
				print ("An {} called {} has been successfully created" .format(rm_type, rm_name))
			else:
				print ("An office with this name already exists!")
		elif rm_type.lower() == 'living space':
			if not rm_name in self.all_livingspace:
				new_livingspace = LivingSpace(rm_name)
				self.all_livingspace.append(new_livingspace)
				print ("A {} called {} has been successfully created" .format(rm_type, rm_name))
			else:
				print ("A living space with this name already exists!")
		else:
			print ("Invalid room type!")

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
	


