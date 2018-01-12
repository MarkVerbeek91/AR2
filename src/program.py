"""
  Program class

  This class keep track of programs that are programmed.
  And feeds it to the controller when a program is executed.
"""

import program_line

# import threading
import pickle
import csv
import logging

class Program():

  def __init__(self):
    """ Load program (not doing anything yet), 
        and fill default command list """
    
    self.current_line = -1
    self._program = []
    

  def clear_program(self):
    self._program = []
    
  def load_program(self, program_name):
    """ Load program from file into memory """
    
    folder = "../samples/"
    
    try:
      self._program = pickle.load(open(folder+program_name,"rb"))
      print(self.program)
    except IOError:
      print("could not find program")
      new_cmd = self._commands['AD']
      new_cmd.comment = '##BEGINNING OF PROGRAM##'
      self.add_command(new_cmd, -1)
      
      try:
        pickle.dump(self._program,open(folder+program_name,"wb"))
      except:
        pickle.dump(self._program,open(folder+"new","wb"))
    
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
      except:
        return -1
    else:
      try:
        self._program.pop(pos)
      except :
        return -1

  def numberOfCommands(self):
    return len(self._program)
