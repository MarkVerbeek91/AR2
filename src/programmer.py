"""
  Programmer class

  This class keeps a list of program line (aka commands) that are programmed.
  And feeds it to the controller when the program is executed.
"""

import controller
import program_line

# import threading
import pickle
import csv
import logging

class Programmer():

  def __init__(self, progName):
    """ Load program (not doing anything yet), 
        and fill default command list """
      
    # setup logging
    logging.basicConfig(filename='../logs/AR2.warning.log', level=logging.WARNING)    
    logging.basicConfig(filename='../logs/AR2.debug.log',   level=logging.DEBUG)    
    logging.basicConfig(filename='../logs/AR2.info.log',    level=logging.INFO)    

    # load protocol
    fileID = open('../conf/conf_commands.csv')
    csvID  = csv.reader(fileID, delimiter=',')

    self._commands = {}
    for row in csvID:
      new_cmd = program_line.Program_line(int(row[0]), row[2], row[1], '', '')
      self._commands[row[1]] = new_cmd
      
    # initialise program
    self.program = []
    self.current_line = -1

    self.load_program('default')
      
      
    # setup controller
    self.number_of_joints = 6
    self.controller = controller.Controller(self.number_of_joints)

  def clear_program(self):
    self.program = []
    
  def load_program(self, program_name):
    """ Load program from file into memory """
    
    folder = "../samples/"
    
    try:
      self.Prog = pickle.load(open(folder+progName,"rb"))
    except:
      new_cmd = self._commands['AD']
      new_cmd.comment = '##BEGINNING OF PROGRAM##'
      self.add_command(new_cmd, -1)
      
      try:
        pickle.dump(self.program,open(folder+progName,"wb"))
      except:
        pickle.dump(self.program,open(folder+"new","wb"))
    
  
    
  def add_command(self, new_cmd, pos):
    """ Add given command on given position, when pos=-1, append command """
    if pos == -1:
      self.program.append(new_cmd)
      logging.debug("new command is added on program end")
    else:
      self.program.insert(pos, new_cmd)
      logging.debug("new command is added on position %d" % pos)

  def remove_command(self, pos):
    """ remove last command or command on position pos """
    if pos == -1:
      try:
        self.program.pop()
      except:
        return -1
    else:
      try:
        self.program.pop(pos)
      except :
        return -1

  def numberOfCommands(self):
    return len(self.program)

  def manAddItem(self):
    print("hello")

  def run_program(self):
    print('starting program')

    # TODO: start program in threat
    self.controller.executeProgram(self.program)

  def stop_program(self):
    """ tell the controller to stop when it's running """
    if self.controller.running:
      print('stopping program')
      self.controller.stop = True
    else:
      print('no programming running')

  def run_program_line(self, var):
    """ let the controller execute a single program line """
    self.controller.executeRow(self.program[var-1])

  def insertReturn(self, pos):
    new_cmd = program_line.Program_line('return', 1, 'none', '')
    self.add_command(new_cmd, pos)

  def waitTime(self):
    new_cmd = self._commands[1]
    new_cmd.data = 5 # TODO, get this from somewhere
    self.add_command(new_cmd, -1)

  def teachInsertBelSelected(self):
    print("gallo")
    new_cmd = self._commands['MV']
    new_cmd.data = 'some very numbery string'
    self.add_command(new_cmd, -1)

  def teachReplaceSelected(self):
    new_cmd = self._commands['MV']
    new_cmd.data = 'some very numbery string'
    self.add_command(new_cmd, -1)

  def waitInputOn(self):
    new_cmd = self._commands['WN']
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)

  def waitInputOff(self):
    new_cmd = self._commands['WF']
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)

  def setOutputOn(self):
    new_cmd = self._commands['SN']
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)

  def setOutputOff(self):
    new_cmd = self._commands['SF']
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)

  def tabNumber(self):
    new_cmd = self._commands['X3']
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)

  def addComment(self):
    new_cmd = self._commands['AD']
    new_cmd.comment = 'default message'
    self.add_command(new_cmd, -1)
    
  def progViewselect(self, line):
    print(line)
