#!/usr/bin/python3
''' Testing: console module '''


import unittest
from io import StringIO
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    ''' class thats testing Console module '''
    def setUp(self):
        ''' setUp function '''
        self.copy = sys.stdout
        self.cap = StringIO()
        sys.stdout = self.cap

    def tearDown(self):
        ''' tearDown function '''
        sys.stdout = self.copy

    def create(self):
        ''' Instantiate an object from the HBNBCommand class. '''
        return HBNBCommand()

    def test_quit_exists(self):
        ''' Quit exists testing '''
        cnsl = self.create()
        self.assertTrue(cnsl.onecmd("quit"))

    def test_EOF_exists(self):
        ''' EOF exists testing '''
        cnsl = self.create()
        self.assertTrue(cnsl.onecmd("EOF"))

    def test_all_method(self):
        ''' all method testing '''
        cnsl = self.create()
        cnsl.onecmd("all")
        self.assertTrue(isinstance(self.cap.getvalue(), str))

    def test_show_method(self):
        ''' show method testing '''
        cnsl = self.create()
        cnsl.onecmd("create User")
        user_id = self.cap.getvalue()
        sys.stdout = self.copy
        self.cap.close()
        self.cap = StringIO()
        sys.stdout = self.cap
        cnsl.onecmd("show User " + user_id)
        output = (self.cap.getvalue())
        sys.stdout = self.copy
        self.assertTrue(str is type(output))

    def test_display_class_name(self):
        ''' test: display error message if class is missing '''
        cnsl = self.create()
        cnsl.onecmd("create User")
        sys.stdout = self.copy
        self.cap.close()
        self.cap = StringIO()
        sys.stdout = self.cap
        cnsl.onecmd("show")
        output = (self.cap.getvalue())
        sys.stdout = self.copy
        self.assertEqual("** class name missing **\n", output)

    def test_class_id(self):
        ''' test: display error message if id is missing '''
        cnsl = self.create()
        cnsl.onecmd("create User")
        sys.stdout = self.copy
        self.cap.close()
        self.cap = StringIO()
        sys.stdout = self.cap
        cnsl.onecmd("show User")
        output = (self.cap.getvalue())
        sys.stdout = self.copy
        self.assertEqual("** instance id missing **\n", output)

    def test_display_instance_not_found(self):
        ''' test: display error message if id is missing '''
        cnsl = self.create()
        cnsl.onecmd("create User")
        sys.stdout = self.copy
        self.cap.close()
        self.cap = StringIO()
        sys.stdout = self.cap
        cnsl.onecmd("show User " + "124356876")
        output = (self.cap.getvalue())
        sys.stdout = self.copy
        self.assertEqual("** no instance found **\n", output)

    def test_create_method(self):
        ''' test: create method '''
        cnsl = self.create()
        cnsl.onecmd("create User")
        self.assertTrue(isinstance(self.cap.getvalue(), str))

    def test_class_name(self):
        ''' checks error message if class name doesn't exist '''
        cnsl = self.create()
        cnsl.onecmd("create")
        output = (self.cap.getvalue())
        self.assertEqual("** class name missing **\n", output)

    def test_class_name_missing(self):
        ''' checks error message if class name doesn't exist '''
        cnsl = self.create()
        cnsl.onecmd("create Something")
        output = (self.cap.getvalue())
        self.assertEqual("** class doesn't exist **\n", output)
