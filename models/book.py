#!/usr/bin/python3
"""The Book module
"""
from datetime import datetime

from .base_model import BaseModel


class Book(BaseModel):
    """Defines the Book class, inherits from BaseModel

    Attributes:
        title (str): the title of the book
        author (str): the author of the book
        pub_date (date): the date the book was published
        age_category (str): the age category the book is intended for

        page_length (int): the number of pages in the book
        fiction (bool): whether the book is fiction or not
        description (str): a description of the book
        cover_image (str): the url of the book's cover image
    """
    title = ""
    author = ""
    pub_date = None
    age_category = ""

    page_length = 0
    fiction = None
    description = ""
    cover_image = ""
