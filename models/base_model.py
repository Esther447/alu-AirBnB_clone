#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models"""
    
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance from kwargs dictionary or as new instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at timestamp to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
