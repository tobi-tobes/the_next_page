#!/usr/bin/python3
"""This module tests the Genre class
"""
from datetime import datetime
import pycodestyle
import unittest

from models.genre import Genre
from models.base_model import BaseModel


class TestGenre(unittest.TestCase):
    """Defines tests for the Genre Class
    """
    def setUp(self):
        """Sets up each test. Initializes a new instance of Genre
        """
        self.genre = Genre()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes
        """
        self.assertTrue(hasattr(self.genre, "name"))
        self.assertEqual(type(self.genre.name), str)
        self.assertTrue(hasattr(self.genre, "parent_genre"))
        self.assertEqual(type(self.genre.parent_genre), str)

    def test_inheritance(self):
        """Tests if the Genre class inherits from BaseModel
        """
        self.assertTrue(issubclass(Genre, BaseModel))
        self.assertTrue(issubclass(type(self.genre), BaseModel))

    def test_init(self):
        """Tests for proper initialization of a Genre instance
        """
        self.assertTrue(isinstance(self.genre, Genre))
        self.assertIsInstance(self.genre.id, str)
        self.assertIsInstance(self.genre.created_at, datetime)
        self.assertIsInstance(self.genre.updated_at, datetime)

        self.assertEqual(self.genre.name, "")
        self.assertEqual(self.genre.parent_genre, "")

    def test_str(self):
        """Tests the informal string representation of the Genre class
        """
        string = "[{}] ({}) {}".format(self.genre.__class__.__name__,
                                       self.genre.id,
                                       self.genre.__dict__)
        self.assertEqual(string, str(self.genre))

    def test_pycodestyle(self):
        """Tests pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/genre.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Tests for the presence of docstrings
        """
        self.assertIsNotNone(__import__("models").genre.__doc__)
        self.assertIsNotNone(Genre.__doc__)
        for func in dir(Genre):
            if func[0] != "_" or func in ["__init__", "__str__"]:
                self.assertIsNotNone(func.__doc__)
