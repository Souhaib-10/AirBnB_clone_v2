#!/usr/bin/python3
''' Script console for command intrepreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def help_quit(self):
        """Help information for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for the EOF command"""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
