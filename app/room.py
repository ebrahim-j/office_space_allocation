class Room (object):
	
	def __init__(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type
		

#implement all methods that are similar to these two classes

class OfficeSpace(Room):

	def __init__(self, name):
		self.name = name
		self.room_type = "OFFICE"
		self.capacity = 6
		self.occupants = []
		

class LivingSpace(Room):

	def __init__(self, name):
		self.name = name
		self.room_type = "LIVING SPACE"
		self.capacity = 4
		self.occupants = []
		