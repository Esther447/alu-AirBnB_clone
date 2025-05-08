#!/usr/bin/python3
from models import storage

all_objs = storage.all()
print(type(all_objs) == dict and "OK" or "FAIL")
