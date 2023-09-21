#!/usr/bin/python3
"""Review module for the HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """Review class to store review information"""

    __tablename__ = "reviews"  # Define the table name

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Establish relationships with Place and User classes
    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
