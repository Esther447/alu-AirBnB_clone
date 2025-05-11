#!/usr/bin/python3
"""
This file defines the console class which will
serve as the entry point of the entire project
"""

from cmd import Cmd
from models import storage
from models.engine.errors import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Global variable of registered models
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(Cmd):
    """
    The Console based driver of the AirBnb Clone
    All interactions with the system is done via
    this class
    """

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Exit the program in non-interactive mode"""
        return True

    def do_quit(self, args):
        """Quit command exits the program"""
        return True

    def do_create(self, args):
        """
        Create an instance of a model given its name:
        Usage: create ModelName
        """
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            temp = classes[args[0]]()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")

    def do_show(self, arg):
        """
        Show an instance of a model based on its name and ID:
        Usage: show ModelName instance_id
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")

    def do_destroy(self, arg):
        """
        Delete an instance of a model by class name and ID:
        Usage: destroy ModelName instance_id
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")

    def do_all(self, args):
        """
        Display all instances of a model or all models:
        Usage: all or all ModelName
        """
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")

    def do_update(self, arg):
        """
        Update an instance based on class name and ID:
        Usage: update ModelName id field value
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")

    def do_models(self, arg):
        """Print all registered Models"""
        print(*classes)

    def handle_class_methods(self, arg):
        """
        Handle class methods like:
        <Model>.all(), <Model>.show("id"), etc.
        """
        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for x in printable:
                if x in arg:
                    print(val)
                    break
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception:
            print("** invalid syntax **")

    def default(self, arg):
        """
        Override default method to handle custom class methods
        like <Model>.all(), <Model>.count(), etc.
        """
        if '.' in arg and arg[-1] == ')':
            if arg.split('.')[0] not in classes:
                print("** class doesn't exist **")
                return
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


def parse(line: str):
    """Splits a line into arguments using shell-like syntax"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
