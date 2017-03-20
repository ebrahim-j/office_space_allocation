class Person(object):
	"""This class describes each instance of person"""
	def __init__(self,name, email):
		self.name = name
		self.email = email


class Staff(Person):
	"""This class describes each instance of Staff"""

	def __init__(self, name, email):
		super(Staff, self).__init__(name,email)
		self.role = "STAFF"
		self.wants_accomodation = "N"
		

class Fellow(Person):
	"""This class defines each instance Fellow"""

	def __init__(self, name, email, wants_accomodation="N"):
		super(Fellow, self).__init__(name,email)
		self.role = "FELLOW"
		self.wants_accomodation = wants_accomodation
		