class Person(object):

	def __init__(self, name, role, wants_accomodation="N"):
		self.name = name
		self.role = role
		self.wants_accomodation = wants_accomodation


class Staff(Person):

	def __init__(self, name):
		self.role = "STAFF"
		self.name = name
		self.wants_accomodation = wants_accomodation
		self.email = ''
		

class Fellow(Person):

	def __init__(self, name, wants_accomodation="N"):
		self.name = name
		self.wants_accomodation = wants_accomodation
		self.role = "FELLOW"
		self.email = ''
