#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

bm = BaseModel()
bm.save()
storage.reload()

key = "BaseModel.{}".format(bm.id)
print(key in storage.all() and "OK" or "FAIL")
