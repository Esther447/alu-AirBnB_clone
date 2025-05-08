#!/usr/bin/python3
import json
from models.base_model import BaseModel  # Add this
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file and deserializes them back to instances."""
    __file_path = "file.json"
    __objects = {}
 

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        # add other classes as needed
    }

    def all(self):
        """Returns the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val['__class__']
                    if cls_name in self.classes:
                        self.__objects[key] = self.classes[cls_name](**val)
        except FileNotFoundError:
            pass
