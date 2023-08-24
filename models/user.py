#!/usr/bin/python3
"""The User module
"""
from .base_model import BaseModel


class User(BaseModel):
    """The User class, inherits from BaseModel

    Attributes:
        first_name (str): the user's first name
        last_name (str): the user's last name
        email (str): the user's email address
        password (str): the user's password (temp)
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
