import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes the object."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Add new instance to storage
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Updates the updated_at attribute and saves the object."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the object."""
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
