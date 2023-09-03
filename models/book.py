#!/usr/bin/python3
"""The Book module
"""
from datetime import date

from .base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship

if storage_type == "db":
    book_genre = Table('book_genre', Base.metadata,
                       Column('book_id', String(60),
                              ForeignKey("books.id", onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column("genre_id", String(60),
                              ForeignKey("genres.id", onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


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
        genres (list): a list of genres related to the book
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
        genres = relationship("Genre", secondary=book_genre,
                              viewonly=False)
    else:
        title = ""
        author = ""
        pub_date = None
        age_category = ""

        page_length = 0
        fiction = None
        description = ""
        cover_image = ""
        genre_ids = []

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

        @property
        def genres(self):
            """ Getter for genres associated with book """
            from models import storage
            from .genre import Genre

            genre_list = []
            all_genres = storage.all(Genre).values()
            for genre in all_genres:
                if genre.book_id == self.id:
                    genre_list.append(genre)
            return genre_list
