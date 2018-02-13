"""
    Program class

    This class keep track of programs that are programmed.
    And feeds it to the controller when a program is executed.
"""

# import threading
import pickle
import csv
import logging

from program_line import ProgramLine

class Program():
    """ store program lines in nice way plus more """

    def __init__(self):
        """ Load program (not doing anything yet),
        and fill default command list """

        self.current_line = -1
        self._program = []
        self.register = [0, 0, 0, 0, 0, 0]

    def clear_program(self):
        self._program = []
        self.register = [0, 0, 0, 0, 0, 0]

    def load_program(self, program_name):
        """ Load program from file into memory """

        folder = "../samples/"

        try:
            self._program = pickle.load(open(folder+program_name, "rb"))
            print(self._program)
        except IOError:
            print("could not find program")
            # TODO: stuff
            new_cmd = ProgramLine()
            new_cmd.comment = '##BEGINNING OF PROGRAM##'
            
            
            self.add_command(new_cmd, -1)

    def save_program(self, program_name):
        """ save program to disc """
        try:
            pickle.dump(self._program, open(program_name, "wb"))
        except:
            pickle.dump(self._program, open("new", "wb"))

    def add_command(self, new_cmd, pos):
        """ Add given command on given position, when pos=-1, append command """
        if pos == -1:
            self._program.append(new_cmd)
            logging.debug("new command is added on program end")
        else:
            self._program.insert(pos, new_cmd)
            logging.debug("new command is added on position %d" % pos)

    def remove_command(self, pos):
        """ remove last command or command on position pos """
        if pos == -1:
            try:
                self._program.pop()
            except IndexError:
                return -1
        else:
            try:
                self._program.pop(pos)
            except:
                return -1

    def numberOfCommands(self):
        """ return length of program """
        return len(self._program)
