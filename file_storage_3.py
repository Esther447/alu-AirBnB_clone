#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

bm = BaseModel()
key = "BaseModel.{}".format(bm.id)
print("OK" if key in storage.all() else "FAIL")
