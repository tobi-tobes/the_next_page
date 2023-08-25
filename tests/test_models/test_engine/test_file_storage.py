#!/usr/bin/python3
"""This module tests the FileStorage class"""
import json
import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.book import Book
from models.bookshelf import Bookshelf
from models.genre import Genre
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class
    """
    def setUp(self):
        """Sets up the test environment
        """
        self.fs = FileStorage()
        self.fs._FileStorage__file_path = "test.json"
        self.fs._FileStorage__objects = {}
        
        if os.path.exists(self.fs._FileStorage__file_path):
            os.remove(self.fs._FileStorage__file_path)

    def test_all(self):
        """Tests the all method
        """
        all_objs = self.fs.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(all_objs, self.fs._FileStorage__objects)
        self.assertEqual(len(all_objs), 0)

        b1, b2 = BaseModel(), BaseModel()
        self.fs.new(b1)
        self.fs.new(b2)

        self.assertIn("BaseModel.{}".format(b1.id), all_objs)
        self.assertIn("BaseModel.{}".format(b2.id), all_objs)
        self.assertEqual(len(all_objs), 2)
        book, bookshelf, genre, user = Book(), Bookshelf(), Genre(), User()

        self.fs.new(book)
        self.fs.new(bookshelf)
        self.fs.new(genre)
        self.fs.new(user)

        self.assertEqual(len(all_objs), 6)
        self.assertIn("Book.{}".format(book.id), self.fs.all(Book))
        self.assertIn("Bookshelf.{}".format(bookshelf.id),
                      self.fs.all(Bookshelf))
        self.assertIn("Genre.{}".format(genre.id), self.fs.all(Genre))

        self.assertIn("User.{}".format(user.id), self.fs.all(User))
        self.assertNotIn("User.{}".format(user.id), self.fs.all(Book))
        self.assertNotIn("User.{}".format(user.id), self.fs.all(Bookshelf))
        self.assertNotIn("User.{}".format(user.id), self.fs.all(Genre))
        self.assertNotIn("Book.{}".format(book.id), self.fs.all(User))

    def test_new(self):
        """Tests the new method
        """
        all_objs = self.fs.all()
        obj1 = BaseModel()
        self.fs.new(obj1)
        self.assertIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIs(all_objs["BaseModel.{}".format(obj1.id)], obj1)

        obj2 = BaseModel()
        self.fs.new(obj2)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)
        self.assertIs(all_objs["BaseModel.{}".format(obj2.id)], obj2)

    def test_save(self):
        """Tests the save method
        """
        obj1, obj2 = BaseModel(), BaseModel()
        self.fs.new(obj1)
        self.fs.new(obj2)
        self.fs.save()

        self.assertTrue(os.path.isfile(self.fs._FileStorage__file_path))
        self.assertGreater(os.path.getsize(self.fs._FileStorage__file_path), 0)

        with open(self.fs._FileStorage__file_path, "r") as f:
            contents = json.load(f)
        self.assertIn("BaseModel.{}".format(obj1.id), contents)
        self.assertIn("BaseModel.{}".format(obj2.id), contents)

        self.assertEqual(contents["BaseModel.{}".format(obj1.id)],
                         obj1.to_dict())
        self.assertEqual(contents["BaseModel.{}".format(obj2.id)],
                         obj2.to_dict())

    def test_reload(self):
        """Tests the reload method
        """
        all_objs = self.fs.all()
        obj1, obj2 = BaseModel(), BaseModel()
        self.fs.new(obj1)
        self.fs.new(obj2)
        self.fs.save()
        all_objs.clear()

        self.fs.reload()
        all_objs = self.fs.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)

        self.assertEqual(all_objs["BaseModel.{}".format(obj1.id)].to_dict(),
                         obj1.to_dict())
        self.assertEqual(all_objs["BaseModel.{}".format(obj2.id)].to_dict(),
                         obj2.to_dict())

    def test_delete(self):
        """Tests the delete method
        """
        all_objs = self.fs.all()
        obj1, obj2 = BaseModel(), BaseModel()
        self.fs.new(obj1)
        self.fs.new(obj2)

        self.assertIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)
        self.fs.delete(obj1)
        self.assertNotIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)
