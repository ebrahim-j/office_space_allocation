class Person(object):

	def __init__(self, name, role):
		self.name = name
		self.role = role


class Staff(Person):

	def __init__(self, name, email, wants_accomodation="N"):
		self.role = "STAFF"
		self.wants_accomodation = wants_accomodation
		self.name = name
		self.email = email

class Fellow(Person):

	def __init__(self, name, email, wants_accomodation="N"):
		self.name = name
		self.wants_accomodation = wants_accomodation
		self.role = "FELLOW"
		self.email = email

		