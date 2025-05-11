#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage  # This ensures access to the storage engine

class BaseModel:
    def __init__(self, **kwargs):
        """Initializes a new instance or re-creates from a dictionary"""
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    val = datetime.fromisoformat(val)
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates `updated_at` and saves the instance to storage"""
        self.updated_at = datetime.now()
        storage.save()
