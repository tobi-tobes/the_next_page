#!/usr/bin/python3
"""The Bookshelf module
"""
from .base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

if storage_type == "db":
    bookshelf_books = Table("bookshelf_books", Base.metadata,
                            Column("bookshelf_id", String(60),
                                   ForeignKey("bookshelves.id"),
                                   primary_key=True),
                            Column("book_id", String(60),
                                   ForeignKey("books.id"), primary_key=True))


class Bookshelf(BaseModel, Base):
    """The Bookshelf class, inherits from BaseModel and Base (SQLAlchemy)

    Attributes:
        name (str): the name of the bookshelf
        book_ids (list): a list of book ids associated with a bookshelf
                         (FS only)
        books (list): a list of the books in the bookshelf (ORM only)
    """
    if storage_type == "db":
        __tablename__ = "bookshelves"
        name = Column(String(128), nullable=False)
        books = relationship("Book", secondary="bookshelf_books",
                             back_populates="bookshelves", viewonly=False)
    else:
        name = ""
        book_ids = []

        @property
        def books(self):
            """Getter for the list of books in the bookshelf
            """
            from models import storage
            from .book import Book

            books = []
            for value in storage.all(Book).values():
                if value.id in self.book_ids:
                    books.append(value)
            return books

        @books.setter
        def books(self, obj):
            """Adds an id to the list of book ids
            """
            from .book import Book

            if type(obj) == Book:
                self.book_ids.append(obj.id)
