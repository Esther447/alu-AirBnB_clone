import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(
                {key: obj.to_dict() for key, obj in FileStorage.__objects.items()},
                file,
                default=str
            )

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass  # No file to load, so we do nothing
