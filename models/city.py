#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"  # Define the table name

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    # Establish a relationship with the State class
    state = relationship("State", back_populates="cities")
