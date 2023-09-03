#!/usr/bin/python3
"""The User module
"""
from hashlib import md5

from .base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Defines the attributes of a user, inherits from BaseModel and
    Base (SQLAlchemy)

    Attributes:
        first_name (str): the user's first name
        last_name (str): the user's last name
        email (str): the user's email address
        password (str): the user's password (temp)
        bookshelves (list): a list of the user's bookshelves (ORM only)
    """
    if storage_type == "db":
        __tablename__ = "users"
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)

        password = Column(String(128), nullable=False)
        # bookshelves = relationship("Bookshelf", cascade="all, delete",
        #                            backref="user")
    else:
        first_name = ""
        last_name = ""
        email = ""
        password = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance
        """
        if kwargs and "password" in kwargs:
            passwd = md5(kwargs["password"].encode('utf-8')).hexdigest()
            kwargs["password"] = passwd
        super().__init__(*args, **kwargs)
