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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
