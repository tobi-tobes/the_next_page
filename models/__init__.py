#!/usr/bin/python3
"""Instantiates a storage object, choosing between database or file storage
"""
import os


storage_type = os.getenv("TNP_STORAGE_TYPE")
if storage_type == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
