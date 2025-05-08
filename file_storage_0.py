#!/usr/bin/python3
from models.engine.file_storage import FileStorage

fs = FileStorage()
print(type(fs._FileStorage__file_path) == str and "OK" or "FAIL")
