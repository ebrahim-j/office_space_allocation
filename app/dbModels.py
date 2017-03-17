import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class RoomModel(Base):
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	room_type = Column(String(32))
	capacity = Column(Integer)

class PersonModel(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)
	role = Column(String(32))
	office = Column(String(255))
	livingspace	= Column(String(255))

class UnallocationsModel(Base):
	__tablename__ = 'unallocations'
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)
	role = Column(String(32))
	space = Column(String(10))


#unallocations table (person id, name, office, livingspace)
#allocations table (person id, name, role, accomodation option)

#or create one table then have a column to show
#ALLOCATED OR UNALLOCATED

#engine to store data
#engine = create_engine('sqlite:///' + self.db + '.db')

#create all tables in the engine
#Base.metadata.create_all(engine)
