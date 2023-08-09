#!/usr/bin/python3
'''
    console.py that contains the entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program on End-of-File input (Ctrl+D or Ctrl+Z)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
