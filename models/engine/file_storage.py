#!/usr/bin/python3
"""The FileStorage module
"""
import json

classes = {"BaseModel": BaseModel, "Book": Book, "Bookshelf": Bookshelf,
           "Genre": Genre, "User": User}


class FileStorage:
    """Serializes instances to a JSON file and deserializes from a JSON file
    to instances

    Attributes:
        __file_path (str): The path to the JSON file
        __objects (dict): A dictionary to store instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage

        Args:
            cls (class): The class to filter for
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds an object to the '__objects' dictionary

        Args:
            obj: The object to store
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file specified by '__file_path'
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes from the JSON file specified by '__file_path' to
        the '__objects' dictionary, if the file exists
        """
        from ..base_model import BaseModel
        from ..book import Book
        from ..bookshelf import Bookshelf
        from ..genre import Genre
        from ..user import User

        classes = {"BaseModel": BaseModel, "Book": Book, "Bookshelf": Bookshelf
                   , "Genre": Genre, "User": User}

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                if value["__class__"] in classes:
                    cls = classes[value["__class__"]]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from '__objects', if it exists

        Args:
            obj: The object to delete
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        from models import storage

        if cls not in classes.values():
            return None

        all_cls = storage.all(cls)

        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
