#!/usr/bin/python3
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes them back to instances."""
    __file_path = "file.json"
    __objects = {}

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
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
