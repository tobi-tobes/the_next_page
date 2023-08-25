#!/usr/bin/python3
"""The Next Page console/command interpreter
"""
import ast
import cmd
import sys
from datetime import date

from models import storage
from models.base_model import BaseModel
from models.book import Book
from models.bookshelf import Bookshelf
from models.genre import Genre
from models.user import User


class TheNextPageCommand(cmd.Cmd):
    """Defines the TheNextPageCommand class

    Attributes:
        prompt (str): The command prompt
        classes (tuple): The list of classes that can be created
    """
    prompt = '(tnp) ' if sys.__stdin__.isatty() else ''
    classes = {'BaseModel': BaseModel, 'Book': Book,
               'Bookshelf': Bookshelf, 'Genre': Genre,
               'User': User}
    types = {'page_length': int, 'fiction': bool,
             'pub_date': date}

    def precmd(self, line):
        """Displays a prompt before each command in non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)', end='')
        return line

    def parseline(self, line):
        """Parses the line before it is executed
        """
        if '(' in line and ')' in line:
            line = line.replace('.', ' ', 1).replace('(', ' ', 1)
            line = line.replace(')', '')
            if '{' in line and ': ' in line and '}' in line:
                #  Update if dictionary is given
                pre_dict, dict_info = line.split(', {', 1)
                pre_dict = pre_dict.split(" ")
                pre_dict[2] = pre_dict[2].replace('"', '')
                line = ' '.join([pre_dict[1], pre_dict[0], pre_dict[2],
                                 '{' + dict_info])
                return super().parseline(line)

            line = line.split()
            if len(line) == 3:
                #  For show and destroy
                line[2] = line[2].replace('"', '')
                line = " ".join([line[1], line[0], line[2]])
            elif len(line) >= 5:
                #  Update if attribute name and value are given
                line[2] = line[2].replace('"', '').replace(',', '')
                line[3] = line[3].replace('"', '').replace(',', '')
                line[4] = line[4].replace('"', '')
                line = " ".join([line[1], line[0], line[2], line[3], line[4]])
            else:
                line = " ".join([line[1], line[0]])

        return super().parseline(line)

    def do_quit(self, arg):
        """Exit the program with the command 'quit'
        """
        return True

    def help_quit(self):
        """Documentation for the quit command
        """
        print("Exits the program")

    def do_EOF(self, arg):
        """Exit the program on receiving the EOF signal
        """
        print()
        return True

    def help_EOF(self):
        """Documentation for the EOF signal
        """
        print("Exits the program on receiving the EOF signal")

    def emptyline(self):
        """Does nothing when an empty line is entered
        """
        return False

    def do_create(self, arg):
        """Create an object of any class with optional parameters

        Usage: create <class name>, OR <class name>.create()
            OR create <Class name> <param1> <param2> <param3> ...
        Param syntax: <key name>=<value>
        Value syntax:
            - String: "<value>"
            - Integer: <number>
            - Date: <YYYY/MM/DD>
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[tokens[0]]()
        # Handle the parameters
        if len(tokens) > 1:
            for i in range(1, len(tokens)):
                if "=" in tokens[i]:
                    key, value = tokens[i].split("=")
                    # Some values may have underscores. For later handling
                    value = value.replace("_", " ").replace('\"', '"')
                    if value[0] == '"' and value[-1] == '"':
                        value = value[1:-1]
                    if key in self.types:
                        # Convert a date string to a date object
                        if self.types[key] is date:
                            year, month, day = value.split("/")
                            value = date(int(year), int(month), int(day))
                        else:
                            value = self.types[key](value)
                    setattr(new_instance, key, value)
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id> OR <class name>.show(<id>)
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")

        else:
            key = tokens[0] + '.' + tokens[1]
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id

        Usage: destroy <class name> <id> OR <class name>.destroy(<id>)
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")

        else:
            key = tokens[0] + '.' + tokens[1]
            if key not in storage.all():
                print('** no instance found **')
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Displays the string representation of all instances or
        all instances of a class

        Usage: all <class name> OR <class name>.all() OR all
        """
        output = []
        if not arg:
            for value in storage.all().values():
                output.append(str(value))
            print(output)

        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg == key.split('.')[0]:
                    output.append(str(value))
            print(output)

    def do_update(self, arg):
        """Updates/adds to an instance's attributes

        Usage: update <class name> <id> <attribute name> "<attribute value>"
            OR <class name>.update(<id>, <attribute name>, "<attribute value>)"
            OR <class name>.update(<id>, <dictionary representation>)
        """
        if not arg:
            print("** class name missing **")
            return
        if '{' in arg and ': ' in arg and '}' in arg:
            tokens = arg.split(' {')
            tokens[0] = tokens[0].split()
            tokens[1] = ast.literal_eval('{' + tokens[1])
            tokens = [tokens[0][0], tokens[0][1], tokens[1]]
        else:
            tokens = arg.split(" ", 4)

        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            if type(tokens[2]) is dict:
                for k, v in tokens[2].items():
                    if type(v) is str:
                        v = v.replace('_', ' ')
                    setattr(storage.all()[key], k, v)
                    storage.save()
                return
            print("** value missing **")

        else:
            # if tokens[3][0] == tokens[3][-1] == '"':
            #     tokens[3] = tokens[3][1:-1]
            if '_' in tokens[3]:
                tokens[3] = tokens[3].replace('_', ' ')
            elif tokens[3].isdigit():
                tokens[3] = int(tokens[3])
            elif tokens[3].replace('.', "", 1).isdigit():
                tokens[3] = float(tokens[3])

            setattr(storage.all()[key], tokens[2], tokens[3])
            storage.save()

    def default(self, line):
        """Parse lines which are not recognized as commands
        """
        tokens = line.split(' ')
        if tokens[0] == 'count':
            count = 0
            for key in storage.all():
                if tokens[1] == key.split('.')[0]:
                    count += 1
            print(count)
        else:
            return super().default(line)


if __name__ == '__main__':
    TheNextPageCommand().cmdloop()
