#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()

# Assign additional attributes
my_model.name = "My First Model"
my_model.my_number = 89

# Print the instance to see the string representation
print(my_model)

# Save the instance (update the updated_at timestamp)
my_model.save()
print(my_model)

# Convert the instance to a dictionary
my_model_json = my_model.to_dict()
print(my_model_json)

# Print the keys and types of the dictionary
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
