#!/usr/bin/python3
"""The Book module
"""
from datetime import date

from .base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship


class Book(BaseModel, Base):
    """Defines the Book class, inherits from BaseModel and Base (SQLAlchemy)

    Attributes:
        title (str): the title of the book
        author (str): the author of the book
        pub_date (date): the date the book was published
        age_category (str): the age category the book is intended for

        page_length (int): the number of pages in the book
        fiction (bool): whether the book is fiction or not
        description (str): a description of the book
        cover_image (str): the url of the book's cover image
        bookshelves (list): a list of the bookshelves the book is in (ORM only)
    """
    if storage_type == "db":
        __tablename__ = "books"
        title = Column(String(128), nullable=False)
        author = Column(String(128), nullable=False)
        pub_date = Column(Date, nullable=False)
        age_category = Column(String(128), nullable=False)

        page_length = Column(Integer, nullable=False)
        fiction = Column(Boolean, nullable=False)
        description = Column(String(1024), nullable=False)
        cover_image = Column(String(1024), nullable=False)
        bookshelves = relationship("Bookshelf", secondary="bookshelf_books",
                                   back_populates="books")
    else:
        title = ""
        author = ""
        pub_date = None
        age_category = ""

        page_length = 0
        fiction = None
        description = ""
        cover_image = ""

        @property
        def bookshelves(self):
            """Getter for the list of bookshelves the book is in
            """
            from models import storage
            from .bookshelf import Bookshelf

            bookshelves = []
            for value in storage.all(Bookshelf).values():
                if self.id in value.book_ids:
                    bookshelves.append(value)
            return bookshelves
