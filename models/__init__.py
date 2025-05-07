#!/usr/bin/python3
"""Initialize the storage engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

