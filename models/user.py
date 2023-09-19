#!/usr/bin/python3
"""User Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """The User class, contains user information"""

    __tablename__ = "users"  # Define the table name

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Define the one-to-many relationship with Place
    places = relationship("Place", backref="user", cascade="all, delete-orphan")

    # Define the one-to-many relationship with Review
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
