#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
import shlex

classes = {
    "BaseModel": BaseModel
}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        args = shlex.split(arg)
        objs = storage.all()
        if not args:
            print([str(obj) for obj in objs.values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objs.items() if key.startswith(args[0] + ".")])

    def do_update(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                try:
                    cast_type = type(getattr(obj, attr_name))
                    attr_value = cast_type(attr_value)
                except (AttributeError, ValueError):
                    pass  # Keep as string if not castable
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
