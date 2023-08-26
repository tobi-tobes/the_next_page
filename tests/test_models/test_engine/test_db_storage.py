#!/usr/bin/python3
"""This module tests the DBStorage class
"""
from datetime import datetime
import inspect
import json
import os
import unittest

from console import TheNextPageCommand
import models
from models.base_model import BaseModel, Base
from models.book import Book
from models.bookshelf import Bookshelf
from models.engine import db_storage
from models.genre import Genre
from models.user import User

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import MySQLdb
import pycodestyle

DBStorage = db_storage.DBStorage
classes = {"BaseModel": BaseModel, "Book": Book,
           "Bookshelf": Bookshelf, "Genre": Genre,
           "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests
        """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance(self):
        """Tests conformity with PEP8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py',
                                    'tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring
        """
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring
        """
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods
        """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


@unittest.skipIf(models.storage_type != 'db', "Database is not being used")
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class
    """
    @classmethod
    def setUpClass(cls):
        """Sets up the class
        """
        cls.conn = MySQLdb.connect(host=os.getenv("TNP_MYSQL_HOST"),
                                   user=os.getenv("TNP_MYSQL_USER"),
                                   passwd=os.getenv("TNP_MYSQL_PWD"),
                                   db=os.getenv("TNP_MYSQL_DB"))
        cls.cur = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        """Clean up after the tests
        """
        cls.cur.close()
        cls.conn.close()

    def setUp(self):
        """Set up the tests
        """
        self.dbs = DBStorage()

    def test_init(self):
        """Tests for proper initialization
        """
        self.assertIs(type(self.dbs._DBStorage__engine),
                      sqlalchemy.engine.base.Engine)
        self.assertIs(type(self.dbs._DBStorage__session), type(None))

    def test_all(self):
        """Test the all method
        """

        # self.assertIs(type(models.storage.all()), dict)

    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    def test_new(self):
        """Test that new adds an object to the database"""

    def test_save(self):
        """Test that save properly saves objects to file.json"""
