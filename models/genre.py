#!/usr/bin/python3
"""The Genre module
"""
from .base_model import BaseModel


class Genre(BaseModel):
    """The Genre class, inherits from BaseModel
    
    Attributes:
        name (str): the name of the genre
        parent_genre (str): Fiction or Non-Fiction
    """
    name = ""
    parent_genre = ""
