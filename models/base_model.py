#!/usr/bin/python3
"""The BaseModel module
"""
from datetime import datetime, date
from uuid import uuid4

import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Defines the common attributes/methods for other inheriting classes
    """
    if models.storage_type == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = updated_at = Column(DateTime, nullable=False,
                                         default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Runs when a new instance is created
        """
        if kwargs:
            if "id" not in kwargs:
                self.id = str(uuid4())
            if "created_at" not in kwargs:
                self.created_at = self.updated_at = datetime.utcnow()

            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                if key == "pub_date":
                    value = date.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns the informal string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's
        __dict__ attribute
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        if "pub_date" in new_dict:
            new_dict["pub_date"] = self.pub_date.isoformat()
        new_dict.pop("_sa_instance_state", None)

        return new_dict

    def delete(self):
        """Deletes the current instance from storage
        """
        models.storage.delete(self)
