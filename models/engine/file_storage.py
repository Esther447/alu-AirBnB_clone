#!/usr/bin/python3
import json
import os

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, only if it exists."""
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val["__class__"]
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**val)
