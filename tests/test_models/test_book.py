#!/usr/bin/python3
"""This module tests the Book class
"""
from datetime import datetime
import pycodestyle
import unittest

from models.book import Book
from models.base_model import BaseModel


class TestBook(unittest.TestCase):
    """Defines tests for the Book Class
    """
    def setUp(self):
        """Sets up each test. Initializes a new instance of a Book
        """
        self.book = Book()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes
        """
        self.assertTrue(hasattr(self.book, "title"))
        self.assertEqual(type(self.book.title), str)
        self.assertTrue(hasattr(self.book, "author"))
        self.assertEqual(type(self.book.author), str)

        self.assertTrue(hasattr(self.book, "pub_date"))
        self.assertEqual(type(self.book.pub_date), type(None))
        self.assertTrue(hasattr(self.book, "age_category"))
        self.assertEqual(type(self.book.age_category), str)

        self.assertTrue(hasattr(self.book, "page_length"))
        self.assertEqual(type(self.book.page_length), int)
        self.assertTrue(hasattr(self.book, "fiction"))
        self.assertEqual(type(self.book.fiction), type(None))

        self.assertTrue(hasattr(self.book, "description"))
        self.assertEqual(type(self.book.description), str)
        self.assertTrue(hasattr(self.book, "cover_image"))
        self.assertEqual(type(self.book.cover_image), str)

    def test_inheritance(self):
        """Tests if the Book class inherits from BaseModel
        """
        self.assertTrue(issubclass(Book, BaseModel))
        self.assertTrue(issubclass(type(self.book), BaseModel))

    def test_init(self):
        """Tests for proper initialization of a Book instance
        """
        self.assertTrue(isinstance(self.book, Book))
        self.assertIsInstance(self.book.id, str)
        self.assertIsInstance(self.book.created_at, datetime)
        self.assertIsInstance(self.book.updated_at, datetime)

        self.assertEqual(self.book.title, "")
        self.assertEqual(self.book.author, "")
        self.assertEqual(self.book.pub_date, None)
        self.assertEqual(self.book.age_category, "")

        self.assertEqual(self.book.page_length, 0)
        self.assertEqual(self.book.fiction, None)
        self.assertEqual(self.book.description, "")
        self.assertEqual(self.book.cover_image, "")

    def test_str(self):
        """Tests the informal string representation of the User class
        """
        string = "[{}] ({}) {}".format(self.book.__class__.__name__,
                                       self.book.id,
                                       self.book.__dict__)
        self.assertEqual(string, str(self.book))

    def test_pycodestyle(self):
        """Tests file compliance with PEP8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/book.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """Tests compliance with doctring requirements
        """
        self.assertIsNotNone(__import__("models").book.__doc__)
        self.assertIsNotNone(Book.__doc__)
        for func in dir(Book):
            if func[0] != "_" or func in ["__init__", "__str__", "__doc__"]:
                self.assertIsNotNone(func.__doc__)
