#!/usr/bin/python3
"""The DBStorage module
"""
import os

from ..base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Defines the attributes and methods of the DBStorage class

    Attributes:
        __engine (sqlalchemy.engine.Engine): The current SQLAlchemy engine
        __session (sqlalchemy.orm.session.Session): The current SQLAlchemy
                                                    session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of DBStorage
        """
        TNP_MYSQL_USER = os.getenv("TNP_MYSQL_USER")
        TNP_MYSQL_PWD = os.getenv("TNP_MYSQL_PWD")
        TNP_MYSQL_HOST = os.getenv("TNP_MYSQL_HOST")
        TNP_MYSQL_DB = os.getenv("TNP_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(TNP_MYSQL_USER, TNP_MYSQL_PWD,
                                              TNP_MYSQL_HOST, TNP_MYSQL_DB),
                                      pool_pre_ping=True)
        if os.getenv("TNP_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session for all objects or all objects
        of a specified class

        Args:
            cls (class): The class to filter for
        """
        from ..book import Book
        from ..bookshelf import Bookshelf
        from ..genre import Genre
        from ..user import User

        if cls is None:
            objs = self.__session.query(Book).all()
            objs.extend(self.__session.query(Bookshelf).all())
            objs.extend(self.__session.query(Genre).all())
            objs.extend(self.__session.query(User).all())
        else:
            objs = self.__session.query(cls).all()
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in objs}

    def new(self, obj):
        """Adds an object to the current database session

        Args:
            obj: The object to add
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes in the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session,
        if it exists

        Args:
            obj: The object to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates the current
        database session
        """
        from ..book import Book
        from ..bookshelf import Bookshelf
        from ..genre import Genre
        from ..user import User

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        from models import storage
        from ..base_model import BaseModel
        from ..book import Book
        from ..bookshelf import Bookshelf
        from ..genre import Genre
        from ..user import User

        classes = {"BaseModel": BaseModel, "Book": Book,
                   "Bookshelf": Bookshelf, "Genre": Genre, "User": User}

        if cls not in classes.values():
            return None

        all_cls = storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def close(self):
        """Closes the current database session
        """
        self.__session.remove()
