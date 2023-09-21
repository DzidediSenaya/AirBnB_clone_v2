#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"  # Define the table name

    name = Column(String(128), nullable=False)

    # Establish a relationship with the City class
    cities = relationship("City", backref="state", cascade="delete")
