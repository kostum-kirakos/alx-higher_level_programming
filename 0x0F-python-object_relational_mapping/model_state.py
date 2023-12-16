#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
    
METAdata = MetaData()
Base = declarative_base(metadata=METAdata)

class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
