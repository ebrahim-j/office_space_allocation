import os
import random
import itertools

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .dbModels import Base, PersonModel, RoomModel
from .person import Fellow, Staff
from .room import OfficeSpace, LivingSpace
from text_styles import text_format


"""This file defines all functionalities for our office 
space allocation application

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
			raise ValueError("Use only type string values")

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
			return(text_format.CRED + "\nInvalid room type! Use either 'OFFICE' or 'LIVINGSPACE'\n"
				+text_format.CEND )
		

	def allocate_unallocated_person(self,room_type):
		"""This method allocates people in the waiting list 
		when a new room is created
		"""

		successful_allocations = []

		if room_type.upper() == "OFFICE":
			for each_person in self.officespace_waitinglist:
				print (self.allocate_available_officespace(each_person))
				if self.status == True:
					successful_allocations.append(each_person)

			#update officespace_waitinglist
			updated_list = list(set(self.officespace_waitinglist) - set(successful_allocations))
			self.officespace_waitinglist = updated_list	
			
		elif room_type.upper() == "LIVINGSPACE":
			for each_person in self.livingspace_waitinglist:
				print (self.allocate_available_livingspace(each_person))
				if self.status ==True:
					successful_allocations.append(each_person)

			#update livingspace_waitinglist
			updated_list = list(set(self.livingspace_waitinglist) - set(successful_allocations))
			self.livingspace_waitinglist = updated_list
		
		return
					
	def add_person(self, name, email_address, role, wants_accomodation="N"):
		"""Add a new person to the Dojo and allocate 
		either office space or living space 

		"""
		if role.upper() == "STAFF":
			if email_address in [this_member.email for this_member 
			in itertools.chain(self.all_staff,self.all_fellows)]:
				return (text_format.CRED + "\nWARNING! STAFF or FELLOW with this\
					email_address already exists!\n"
					+text_format.CEND)
			new_staff = Staff(name, email_address)
			self.all_staff.append(new_staff)
			print (text_format.CBOLD + "\nSTAFF {} has been successfully added\n" 
				.format(name)
				+text_format.CEND)			
			print (self.allocate_available_officespace(new_staff))
		elif role.upper() == "FELLOW":
			if email_address in [this_member.email for this_member 
			in itertools.chain(self.all_staff,self.all_fellows)]:
				return (text_format.CRED + "\nWARNING! STAFF or FELLOW with this\
					email_address already exists!\n"
					+text_format.CEND)
			new_fellow = Fellow(name, email_address, wants_accomodation)
			self.all_fellows.append(new_fellow)
			print (text_format.CBOLD + "\nFELLOW {} has been successfully added\n" .format(name)
				+text_format.CEND)
			print (self.allocate_available_officespace(new_fellow))

			#checks whether fellow wants accomodation
			try:
				if new_fellow.wants_accomodation.upper() == "Y":
					return (self.allocate_available_livingspace(new_fellow))
			except AttributeError:
				return
			

		else:
			return (text_format.CRED+"\nInvalid role! Specify either FELLOW or STAFF!\n"
				+text_format.CEND)
			
	def allocate_available_officespace(self,new_person):
		"""This method gets all available offices, confirms if the
		room has space then allocates an office randomly to either fellow or staff
		"""
		available = []

		for office_space in self.all_offices:
			if len(office_space.occupants) < office_space.capacity:
				available.append(office_space)
		
		#loop to check office space to be allocated exists
		if available:
			allocated_room = random.choice(available)
			allocated_room.occupants.append(new_person)
			new_person.office = allocated_room.name
			self.status = True
			return (text_format.CBOLD + "\n{} has been allocated the office {} \n" 
				.format(new_person.name, allocated_room.name)
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
		available = []
		for living_space in self.all_livingspace:
			if len(living_space.occupants) < living_space.capacity:
				available.append(living_space)

		#loop checks vacant livingspace to be allocated
		if available:
			allocated_room= random.choice(available)
			allocated_room.occupants.append(new_person)
			new_person.livingspace = allocated_room.name
			self.status = True
			return (text_format.CBOLD + "\n{} has been allocated the livingspace {} \n" 
				.format(new_person.name, allocated_room.name)
				+text_format.CEND)
		else:
			print (text_format.CRED + "\nWARNING!No available LIVING space"+text_format.CEND)
			self.livingspace_waitinglist.append(new_person)
			print (text_format.CGREEN + "{} has been added to the livingspace waiting list\n" 
				.format(new_person.name)
				+ text_format.CEND)

	def print_room(self, room_name):
		"""This method prints names of all occupants in the
		specified room name
		"""
		output = ""

		if not room_name in [room.name for room in itertools.chain(
			self.all_offices, self.all_livingspace)]:
			output = ("\n\tThe room {} does not exist!\n" .format(room_name))

		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.name == room_name:
				output = ("\n LIST OF ALL OCCUPANTS IN " + room.room_type +\
				  " " + room_name + "\n" + "*" * 50)
				if room.occupants:
					for occupant in room.occupants:
						output += ("\n" + occupant.name + "\t" + occupant.role + "\n")
				else:
					output+= ("\n\n\tThe {} {} has no occupants\n\n"
						.format(room.room_type,room_name))

		return (text_format.CBOLD + output + text_format.CEND)

	def print_allocations(self,filename=None):
		"""This method prints a list of all allocations at the Dojo. The registered
		allocations can then be written to the specified text file

		"""
		output = ""

		if not self.all_offices and not self.all_livingspace:
			return (text_format.CBOLD + "\n\nThere are no rooms at the Dojo.\n\n"
				+text_format.CEND)

		for room in itertools.chain(self.all_offices, self.all_livingspace):
			if room.occupants:
				output += ("\n\nROOM NAME: {} \tTYPE: {} "\
				 .format(room.name, room.room_type))
				output += ("\n" + "-" * 40 + "\n")
				for occupant in room.occupants:
					output += (occupant.name + "-" + occupant.role + ", ")
			else:
				output = ("\n There are no allocations\n\n")

		if filename == None:
			return (text_format.CBOLD + output + text_format.CEND)
		else:
			print("Saving output data to file...")
			txt_file = open(filename + ".txt", "w+")
			txt_file.write(output)
			txt_file.close()
			return ("\033[1m \nData has been successfully saved to {}.txt\n \033[0m"
			 .format(filename))
			
	def print_unallocated(self,filename=None):
		"""This method prints a list of all staff and fellows,
		that have not been allocated any office or living space.

		"""
		output = ""

		if not self.officespace_waitinglist and not self.livingspace_waitinglist:
			return (text_format.CBOLD + "\nThere are currently no unallocated Fellows or Staff.\n\n"
			 +text_format.CEND)
		else:
			output = ("\n\n LIST OF ALL UNALLOCATED STAFF AND FELLOWS\n"\
				+ "*" * 50 + "\n")
			for person in self.officespace_waitinglist:
				output += (person.name + " \t"
						   + person.email + "\t" + person.role 
						   + "\t" + text_format.CRED
						   + "OFFICE SPACE" +text_format.CEND + "\n")
			for person in self.livingspace_waitinglist:
				output += (text_format.CBOLD + person.name + " \t"
						   + person.email + "\t" + person.role
						   + "\t" + text_format.CGREEN
						   + "LIVING SPACE" +text_format.CEND + "\n")

		if filename == None:
			return (text_format.CBOLD + output + text_format.CEND)
		else:
			print ("Saving unallocations list to file...")
			txt_file = open(filename + ".txt", "w+")
			txt_file.write(output)
			txt_file.close()
			return ("\033[1m \nData has been successfully saved to {}.txt\n \033[0m"
			 .format(filename))

	def reallocate_person(self, emailaddress, new_roomname):
		"""This method reallocates a person using their unique identifier,
		in this case their email address, to a the specified new room
		"""

		try:
			person_reallocating = [member for member in itertools.chain(
				self.all_staff,
				self.all_fellows)
			 if member.email == emailaddress][0]
		except IndexError:
			return (text_format.CRED + "\nCould not find person with email {}!\n"
				.format(emailaddress)
				+ text_format.CEND)
		try:
			new_room = [room for room in itertools.chain(
				self.all_offices,
				self.all_livingspace)
			 if room.name == new_roomname][0]
		except IndexError:
			return (text_format.CRED + "\nThe room {} does not exist!\n"
				.format(new_roomname)
				+ text_format.CEND)

		if new_room.room_type == "LIVING SPACE":
			if person_reallocating.role == "STAFF":
				return (text_format.CBOLD +"\nCannot reallocate STAFF to LIVING SPACE!\n" 
					+text_format.CEND)
			if person_reallocating.wants_accomodation != "Y":
				return (text_format.CBOLD +"\nCannot reallocate! This FELLOW does not\
				 require LIVING SPACE!\n" 
					+text_format.CEND)
			if len(new_room.occupants) == 4:
				return(text_format.CRED + "\nThe room {} is full! Can not reallocate {}-{}!\n"
					.format(new_roomname,
					 person_reallocating.role,
					 person_reallocating.name) 
					+ text_format.CEND)

		if new_room.room_type == "OFFICE" and len(new_room.occupants) == 6:
			return (text_format.CRED + "\nThe room {} is full! Cannot reallocate {}-{}!\n"
					.format(new_roomname,
					 person_reallocating.role, person_reallocating.name)
					+ text_format.CEND)


		for room in itertools.chain(self.all_offices, self.all_livingspace):
			for occupant in room.occupants:
					if occupant == person_reallocating:
						current_room = room

		if current_room == new_room:
			return (text_format.CRED + "\nCannot reallocate to the same {}\n"
				.format(current_room.room_type)
				+ text_format.CEND)
		else:
			current_room.occupants.remove(person_reallocating)
			new_room.occupants.append(person_reallocating)
		
			return (text_format.CBOLD + "\n{}-{} was succesfully reallocated to {} {}\n"
				.format(person_reallocating.role,
			 	person_reallocating.name,
			   	new_room.room_type,
			   	new_room.name)
				+ text_format.CEND)

	def load_people(self, filename):
		"""This method adds people to rooms from a txt file.
		The text input from the text file should have the following format
		NAME EMAIL ROLE ACCOMODATION_OPTION

		"""
		output = ''

		if not os.path.isfile(filename + ".txt"):
			return (text_format.CRED + "\nThe file {}.txt does not exist!\n"
				.format(filename) 
				+text_format.CEND)
		if not os.stat(filename + ".txt").st_size:
			return (text_format.CRED + "\nThe file {}.txt is empty!\n"
				.format(filename) 
				+text_format.CEND )

		with open(filename + ".txt") as input_file:
			for line in input_file:
				read_line = line.split()
				if len(read_line) > 4 or len(read_line) < 3:
					print (text_format.CRED + "\nInvalid entry!\n" + text_format.CEND)
				else:
					output += (line + "\n")
				try:
					name = read_line[0]
					email = read_line[1]
					role = read_line[2]
					accomodation_option = read_line[3]
				except IndexError:
					accomodation_option = "N"

				self.add_person(name, email, role, accomodation_option)

		return (text_format.CBOLD + "\tThe following data was loaded successfully\n" 
			+ "_" * 60 + "\n\n" + output + "\n" +text_format.CEND)

	def save_state(self, db_name):
		"""Saves all data from the app to a specified 
		database

		"""

		engine = create_engine('sqlite:///' + db_name + '.db')
		Base.metadata.bind = engine
		Base.metadata.create_all(engine)
		DBSession = sessionmaker(bind=engine)
		session = DBSession()

		for room in itertools.chain(self.all_offices,self.all_livingspace):
			save_room = RoomModel(
				name=room.name,
				room_type=room.room_type,
				capacity=room.capacity,
				)
			existing = session.query(RoomModel).filter(
				RoomModel.name==room.name).count()
			if not existing:
				session.add(save_room)
			session.commit()

		for person in itertools.chain(self.all_staff,self.all_fellows):
			livingspace_waiting = [each_person for each_person\
			 	 in self.livingspace_waitinglist if each_person == person]
			if person.role == "FELLOW" and person.wants_accomodation == "y":
				for living in self.all_livingspace:
					living_allocated = [occupant for occupant in living.occupants\
					 if occupant == person]
					if living_allocated:
						living_status = living.name
				if livingspace_waiting:
					living_status = "UNALLOCATED"		
			else:
				living_status = "N/A"			 	 

			if self.all_offices:	
				for office in self.all_offices:
					office_allocated = [occupant for occupant\
					 in office.occupants if occupant == person]
					if office_allocated:
						office_status = office.name
			else:
				office_status = "UNALLOCATED"	

			save_person = PersonModel(
				name=person.name,
				email=person.email,
				role=person.role,
				office_space=office_status,
				living_space=living_status
				)
			existing = session.query(PersonModel).filter(
				PersonModel.email==person.email).count()
			if not existing:
				session.add(save_person)
		session.commit()

		output = ("\n\nApplication data successfully saved to database!\n\n")
		return (text_format.CBOLD + output + text_format.CEND)

	
	def load_state(self, db_name):
		"""This method loads data from the db
		into the application
		"""
		if not os.path.isfile("{}.db".format(db_name)):
			return (text_format.CRED + "\nThe database {}.db does not exist!\n"
				.format(db_name) 
				+text_format.CEND)
			
		engine = create_engine('sqlite:///' + db_name + '.db')
		Base.metadata.bind = engine			
		DBSession = sessionmaker(bind=engine)
		session = DBSession()
			
		room_list = session.query(RoomModel).all()
		person_list = session.query(PersonModel).all()	
		#load persons
		for person in person_list:
			if person.role == "STAFF":
				load_staff = Staff(person.name, person.email)
				self.all_staff.append(load_staff)
			if person.role == "FELLOW" and person.living_space == "N/A":
				load_fellow = Fellow(person.name, person.email, "N")
				self.all_fellows.append(load_fellow)
			if person.role == "FELLOW" and person.living_space != "N/A":
				load_fellow = Fellow(person.name, person.email, "Y")
				self.all_fellows.append(load_fellow)					
		#loading rooms and occupants	
		for room in room_list:
			if room.room_type == "OFFICE":
				room_to_load = OfficeSpace(room.name)
				self.all_offices.append(room_to_load)
				
				office_occupants = [person for person in person_list\
				 if person.office_space == room.name]
				for occupant in office_occupants:
					if occupant.role == "FELLOW" and occupant.living_space =="N/A":
						fellow_occupant = Fellow(occupant.name, occupant.email, "N")
						room_to_load.occupants.append(fellow_occupant)
					if occupant.role == "FELLOW" and occupant.living_space != "N/A":
						fellow_occupant = Fellow(occupant.name, occupant.email, "y")
						room_to_load.occupants.append(fellow_occupant)
					if occupant.role == "STAFF":
						staff_occupant = Staff(occupant.name, occupant.email)
						room_to_load.occupants.append(staff_occupant)
			if room.room_type == "LIVING SPACE":
				room_to_load = LivingSpace(room.name)
				self.all_livingspace.append(room_to_load)
				
				living_occupants = [person for person in person_list\
				 if person.living_space == room.name]
				for occupant in living_occupants:
					fellow_occupant = Fellow(occupant.name, occupant.email, "Y")
					room_to_load.occupants.append(fellow_occupant)

		#load waiting lists
		unallocated_office = [person for person in person_list\
		 if person.office_space == "UNALLOCATED"]
		
		for person in unallocated_office :
			if person.role == "STAFF":
				staff_to_load = Staff(person.name, person.email)
				self.officespace_waitinglist.append(staff_to_load)	
			if person.role == "FELLOW" and person.living_space == "N/A":
				fellow_to_load = Fellow(person.name, person.email, "N")
				self.officespace_waitinglist.append(fellow_to_load)
			if person.role == "FELLOW" and person.living_space != "N/A":
				fellow_to_load = Fellow(person.name, person.email, "Y")
				self.officespace_waitinglist.append(fellow_to_load)

		unallocated_living = [person for person in person_list\
		 if person.living_space == "UNALLOCATED"]

		for person in unallocated_living:
			unallocated_fellow = Fellow(person.name, person.email, "Y")
			self.livingspace_waitinglist.append(unallocated_fellow)

		output = ("\nData successfully loaded to the Application\n\n")
		return (text_format.CBOLD + output + text_format.CEND)