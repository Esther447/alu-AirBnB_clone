from base_model import BaseModel
from datetime import datetime

bm = BaseModel()
print(type(bm.created_at))  # <class 'datetime.datetime'>
bm.save()
d = bm.to_dict()
print(type(d["created_at"]))  # <class 'str'>
