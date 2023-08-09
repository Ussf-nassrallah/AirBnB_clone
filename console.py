#!/usr/bin/python3
'''
    console.py that contains the entry point of the command interpreter
'''
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    own_classes = {'BaseModel'}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on End-of-File input (Ctrl+D or Ctrl+Z)"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel & saves it"""
        if not line:
            print('** class name missing **')
            return
        if line not in self.own_classes:
            print('** class doesn\'t exist **')
            return

        new_inst = BaseModel()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on class name & id
        """
        arguments = line.split()
        if not arguments:
            print('** class name missing **')
            return
        if arguments[0] not in self.own_classes:
            print('** class doesn\'t exist **')
            return
        if len(arguments) < 2:
            print('** instance id missing **')
            return

        key = arguments[0] + '.' + arguments[1]
        all_objcts = storage.all()
        if key in all_objcts:
            print(all_objcts[key])
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name & id"""
        arguments = line.split()
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.own_classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objcts = storage.all()
            key = arguments[0] + '.' + arguments[1]
            if key in objcts.keys():
                del(objcts[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation
        of all instances based or not on the class name
        """
        arguments = line.split()
        if not line or arguments[0] in self.own_classes:
            list_string = []
            objcts = storage.all()
            for value in objcts.values():
                list_string.append(value.__str__())
            print(list_string)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name, id,
        and attribute name with a new attribute value.
        """
        arguments = line.split()
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.own_classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        else:
            all_objcts = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if key in all_objcts.keys():
                for value in all_objcts.values():
                    try:
                        attr_type = type(getattr(value, arguments[2]))
                        arguments[3] = attr_type(arguments[3])
                    except AttributeError:
                        pass
                setattr(value, arguments[2], arguments[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
