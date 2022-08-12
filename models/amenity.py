#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity (child class for BaseModel).

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
