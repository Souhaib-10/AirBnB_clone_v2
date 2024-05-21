#!/usr/bin/python3
"""__init__ method for models package, like filestorage module"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
