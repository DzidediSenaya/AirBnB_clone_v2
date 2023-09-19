#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


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

    # Define the one-to-many relationship with Review for DBStorage
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    @property
    def reviews(self):
        """Getter attribute for reviews (FileStorage)"""
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
