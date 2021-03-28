#!/usr/bin/python3
'''contains the class definition of a State and an\
   instance Base = declarative_base()'''
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    '''class definition of a State'''
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    relation = {"cascade": "all, delete-orphan", "backref": "state"}
    cities = relationship("City", **relation)
