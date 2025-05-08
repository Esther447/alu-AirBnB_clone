#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

bm = BaseModel()
key = "BaseModel.{}".format(bm.id)
print(key in storage.all() and "OK" or "FAIL")
