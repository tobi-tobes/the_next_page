#!/usr/bin/python3
"""This module tests the command interpreter
"""
from io import StringIO
import os
import pycodestyle
import sys
import unittest
from unittest.mock import patch

from console import TheNextPageCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Tests the console
    """
    @classmethod
    def setUpClass(cls):
        """Sets up the class
        """
        storage._FileStorage__file_path = "test.json"

    def setUp(self):
        """Sets up each test
        """
        self.cns = TheNextPageCommand()
        storage._FileStorage__objects = {}
        if os.path.exists("test.json"):
            os.remove("test.json")

    @unittest.skipUnless(sys.__stdin__.isatty(),
                         "Runs only in interactive mode")
    def test_prompt(self):
        """Test the prompt
        """
        self.assertEqual("(tnp) ", self.cns.prompt)

    def test_help(self):
        """Test the help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("help quit")
            output = "Exits the program\n"
            self.assertEqual(output, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("help EOF")
            output = "Exits the program on receiving the EOF signal\n"
            self.assertEqual(output, f.getvalue())

    def test_emptyline(self):
        """Test an empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test the quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test the EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_create(self):
        """Test the create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            self.assertEqual(36, len(f.getvalue().strip()))

    def test_show(self):
        """Test the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            key = "BaseModel." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show BaseModel " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show User " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('User.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Book")
            obj_id = f.getvalue().strip()
            key = "Book." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Book " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Book.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Bookshelf")
            obj_id = f.getvalue().strip()
            key = "Bookshelf." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Bookshelf " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Bookshelf.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Genre")
            obj_id = f.getvalue().strip()
            key = "Genre." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Genre " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Genre.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

    def test_destroy(self):
        """Test the destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create BaseModel")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "BaseModel." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy BaseModel " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "BaseModel." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('BaseModel.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            self.cns.onecmd("create User")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "User." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy User " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "User." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('User.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Book")
            self.cns.onecmd("create Book")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Book." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Book " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Book." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Book.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Bookshelf")
            self.cns.onecmd("create Bookshelf")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Bookshelf." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Bookshelf " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Bookshelf." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Bookshelf.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Genre")
            self.cns.onecmd("create Genre")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Genre." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Genre " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Genre." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Genre.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

    def test_all(self):
        """Test the all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test the all command with no objects
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("all")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Book")
            self.cns.onecmd("all BaseModel")

            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn("User", f.getvalue())
            self.assertNotIn("Book", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.all()')
            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn("User", f.getvalue())
            self.assertNotIn("Book", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Book")
            self.cns.onecmd("all User")

            self.assertNotIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn("Book", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('User.all()')
            self.assertNotIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn("Book", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Book")
            self.cns.onecmd("create Bookshelf")
            self.cns.onecmd("create Genre")

            self.cns.onecmd("Book.all()")
            self.assertIn("Book", f.getvalue())
            self.cns.onecmd("Bookshelf.all()")
            self.assertIn("Bookshelf", f.getvalue())
            self.cns.onecmd("Genre.all()")

            self.assertIn("Genre", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Book")
            self.cns.onecmd("all")

            self.assertIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertIn("Book", f.getvalue())

    def test_update(self):
        """Test the update command
        """
        object_id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            object_id = f.getvalue().strip()
            self.cns.onecmd("update BaseModel " + object_id)
            self.assertIn("** attribute name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name")
            self.assertEqual("** value missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name \"Betty\"")
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name \"Holberton\"")
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Holberton", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.update("' + object_id +
                            '", "first_name", "Zaid")')
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Zaid", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.update("' + object_id +
                            '", {"first_name": "John", "age": 89})')
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("John", f.getvalue())
            self.assertIn("89", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            object_id = f.getvalue().strip()
            self.cns.onecmd('User.update("' + object_id +
                            '", "first_name", "Mary")')
            self.cns.onecmd("show User " + object_id)
            self.assertIn("Mary", f.getvalue())

            self.cns.onecmd('User.update("' + object_id +
                            '", {"first_name": "Bob", "age": 60})')
            self.cns.onecmd("show User " + object_id)
            self.assertIn("Bob", f.getvalue())
            self.assertIn("60", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Book")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Book.update("' + object_id +
                            '", "name", "War_and_Peace")')
            self.cns.onecmd("show Book " + object_id)
            self.assertIn("War and Peace", f.getvalue())

            self.cns.onecmd('Book.update("' + object_id +
                            '", {"name": "The_Odyssey"})')
            self.cns.onecmd("show Book " + object_id)
            self.assertIn("The Odyssey", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Bookshelf")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Bookshelf.update("' + object_id +
                            '", "name", "My_Bookshelf")')
            self.cns.onecmd("show Bookshelf " + object_id)
            self.assertIn("My Bookshelf", f.getvalue())

            self.cns.onecmd('Bookshelf.update("' + object_id +
                            '", {"name": "My_Bookshelf1"})')
            self.cns.onecmd("show Bookshelf " + object_id)
            self.assertIn("My Bookshelf1", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Genre")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Genre.update("' + object_id +
                            '", "name", "Crime")')
            self.cns.onecmd("show Genre " + object_id)
            self.assertIn("Crime", f.getvalue())

            self.cns.onecmd('Genre.update("' + object_id +
                            '", {"name": "Fantasy"})')
            self.cns.onecmd("show Genre " + object_id)
            self.assertIn("Fantasy", f.getvalue())

    def test_count(self):
        """Test the .count() command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("BaseModel.count()")
            self.assertEqual("0\n", f.getvalue())
            self.cns.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("BaseModel.count()")
            self.assertEqual("1\n", f.getvalue())
            self.cns.onecmd("create User")
            self.cns.onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("User.count()")
            self.assertEqual("2\n", f.getvalue())
            self.cns.onecmd("create Book")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Book.count()")
            self.assertEqual("1\n", f.getvalue())
            self.cns.onecmd("create Bookshelf")
            self.cns.onecmd("create Bookshelf")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Bookshelf.count()")
            self.assertEqual("2\n", f.getvalue())
            self.cns.onecmd("create Genre")
            self.cns.onecmd("create Genre")
            self.cns.onecmd("create Genre")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Genre.count()")
            self.assertEqual("3\n", f.getvalue())

    def test_pycodestyle(self):
        """Tests file compliance with PEP8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """Tests compliance with doctring requirements
        """
        self.assertIsNotNone(__import__("console").__doc__)
        self.assertIsNotNone(TheNextPageCommand.__doc__)
        for func in dir(TheNextPageCommand):
            if func[0] != "_" or func in ["__init__", "__str__"]:
                self.assertIsNotNone(func.__doc__)
