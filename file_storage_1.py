#!/usr/bin/python3
from models.engine.file_storage import FileStorage

fs = FileStorag()
print("OK" if type(fs._FileStorage__objects) is dict else "FAIL")
