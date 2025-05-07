#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project
"""

import cmd
import sys
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Command processor for HBNB"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

        def do_all(self, arg):
            print("This is fine")

        objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg == "BaseModel":
            print([
                str(obj)
                for obj in objs.values()
                if type(obj).__name__ == "BaseModel"
            ])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = all_objs[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
