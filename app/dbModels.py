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
	office_space = Column(String(32))
	living_space = Column(String(32))