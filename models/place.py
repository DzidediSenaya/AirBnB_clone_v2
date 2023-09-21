#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


# Create an instance of SQLAlchemy Table for the Many-To-Many relationship
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Define the many-to-one relationship with City
    cities = relationship("City", back_populates="places")
    # Define the many-to-one relationship with User
    user = relationship("User", back_populates="places")

    # Define the many-to-many relationship with Amenity (for DBStorage)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    # Getter and setter for amenities (for FileStorage)
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """Getter attribute for amenities"""
            from models import storage
            amenities = []
            for amenity_id in self.amenity_ids:
                key = "Amenity." + amenity_id
                amenity = storage.all("Amenity").get(key)
                if amenity:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute for amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
