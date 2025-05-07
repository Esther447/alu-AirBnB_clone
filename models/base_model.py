import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        # Assign unique id to each instance
        self.id = str(uuid.uuid4())
        # Assign the current datetime to created_at and updated_at
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        # Return a string representation of the object
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        # Update the updated_at attribute with the current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create a dictionary of the object
        dict_rep = self.__dict__.copy()
        # Add the class name as __class__
        dict_rep["__class__"] = self.__class__.__name__
        # Convert datetime objects to ISO format strings
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
