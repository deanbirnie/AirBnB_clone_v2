#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='states', cascade='all, delete',
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of the state object"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances
            with state_id
            equals to the current State.id"""
        from models import storage
        city_instances = storage.all(City)
        related_cities = [city for city in city_instances.values()
                          if city.state_id == self.id]
        return related_cities
