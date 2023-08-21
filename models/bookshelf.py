#!/usr/bin/python3
"""The Bookshelf module
"""
from .base_model import BaseModel


class Bookshelf(BaseModel):
    """The Bookshelf class, inherits from BaseModel
    
    Attributes:
        name (str): the name of the bookshelf
        books (list): a list of the books on the bookshelf (temp)
    """
    name = ""
    books = []
