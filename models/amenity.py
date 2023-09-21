#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    # Define the Many-To-Many relationship with Place
    place_amenities = relationship("Place", secondary="place_amenity")


# Create a table to represent the Many-To-Many relationship
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), nullable=False)
                      )
