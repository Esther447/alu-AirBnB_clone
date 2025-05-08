#!/usr/bin/python3
import os
from models import storage
from models.base_model import BaseModel

file_path = "file.json"
if os.path.exists(file_path):
    os.remove(file_path)

bm = BaseModel()
storage.save()
print("OK" if os.path.exists(file_path) else "FAIL")
