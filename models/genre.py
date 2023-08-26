#!/usr/bin/python3
"""The Genre module
"""
from .base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Genre(BaseModel, Base):
    """The Genre class, inherits from BaseModel

    Attributes:
        name (str): the name of the genre
        parent_genre (str): Fiction or Non-Fiction
    """
    if storage_type == "db":
        __tablename__ = "genres"
        name = Column(String(128), nullable=False)
        parent_genre = Column(String(20), nullable=False)
    else:
        name = ""
        parent_genre = ""
