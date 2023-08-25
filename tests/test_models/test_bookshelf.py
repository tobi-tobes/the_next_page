#!/usr/bin/python3
"""This module tests the Bookshelf class
"""
from datetime import datetime
import pycodestyle
import unittest

from models.bookshelf import Bookshelf
from models.base_model import BaseModel


class TestBookshelf(unittest.TestCase):
    """Defines tests for the Bookshelf Class
    """
    def setUp(self):
        """Sets up each test. Initializes a new instance of a Bookshelf
        """
        self.bookshelf = Bookshelf()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes
        """
        self.assertTrue(hasattr(self.bookshelf, "name"))
        self.assertEqual(type(self.bookshelf.name), str)
        self.assertTrue(hasattr(self.bookshelf, "books"))
        self.assertEqual(type(self.bookshelf.books), list)

    def test_inheritance(self):
        """Tests if the Bookshelf class inherits from BaseModel
        """
        self.assertTrue(issubclass(Bookshelf, BaseModel))
        self.assertTrue(issubclass(type(self.bookshelf), BaseModel))

    def test_init(self):
        """Tests for proper initialization of a Bookshelf instance
        """
        self.assertTrue(isinstance(self.bookshelf, Bookshelf))
        self.assertIsInstance(self.bookshelf.id, str)
        self.assertIsInstance(self.bookshelf.created_at, datetime)
        self.assertIsInstance(self.bookshelf.updated_at, datetime)

        self.assertEqual(self.bookshelf.name, "")
        self.assertEqual(self.bookshelf.books, [])

    def test_str(self):
        """Tests the informal string representation of the Bookshelf class
        """
        string = "[{}] ({}) {}".format(self.bookshelf.__class__.__name__,
                                       self.bookshelf.id,
                                       self.bookshelf.__dict__)
        self.assertEqual(string, str(self.bookshelf))

    def test_pycodestyle(self):
        """Tests file compliance with PEP8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/bookshelf.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Tests for the presence of docstrings
        """
        self.assertIsNotNone(__import__("models").bookshelf.__doc__)
        self.assertIsNotNone(Bookshelf.__doc__)
        for func in dir(Bookshelf):
            if func[0] != "_" or func in ["__init__", "__str__", "__doc__"]:
                self.assertIsNotNone(func.__doc__)
