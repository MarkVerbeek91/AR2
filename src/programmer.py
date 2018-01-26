"""
  Programmer class

  This class keeps a list of program line (aka commands) that are programmed.
  And feeds it to the controller when the program is executed.
"""

import controller
import program
import program_line
from program_line import move_data
from program_line import servo_data

# import threading
import pickle
import csv
import logging
import threading

class empty_data():
  """ """
  
  def __init__(self):
    pass
    
  def get(self):
    return ''

class Programmer():

  def __init__(self, progName = ''):
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
    self.program_name = progName
    self.program = program.Program()
    
    # setup controller
    self.number_of_joints = 6
    self.controller = controller.Controller(self.number_of_joints)

  def manAddItem(self):
    print("hello")

  def run_program(self):
    print('starting program')
        
    def threadProg(controller):
    # TODO: start program in threat
      print(controller)
      controller.executeProgram(self.program)

    t = threading.Thread(target=threadProg, args=(self.controller,))
    t.start()

  def clear_program(self):
    """ """
    self.program.clear_program()
    
  def save_program(self):
    """ """
    self.program.save_program(self.program_name)
    
  def stop_program(self):
    """ tell the controller to stop when it's running """
    if self.controller.running:
      print('stopping program')
      self.controller.stop = True
    else:
      print('no program is running')

  def run_program_line(self, var):
    """ let the controller execute a single program line """
        
    def threadProg(controller, var):
    # TODO: start program in threat
      print(controller)
      controller.executeProgram(self.program, program_line_nr = var)

    t = threading.Thread(target=threadProg, args=(self.controller, var))
    t.start()

  def insertReturn(self, pos):
    new_cmd = program_line.Program_line('return', 1, 'none', '')
    self.program.add_command(new_cmd, pos)

  def waitTime(self):
    new_cmd = self._commands['WT']
    new_cmd.data = 5 # TODO, get this from somewhere
    self.program.add_command(new_cmd, -1)

  def teachInsertBelSelected(self):
    new_cmd = self._commands['MV']
    pos = [ 1, 2, 3, 4, 5, 6 ]
    new_cmd.data = move_data(pos, 'lin', 42, 24)
    self.program.add_command(new_cmd, -1)

  def teachReplaceSelected(self):
    new_cmd = self._commands['MV']
    pos = [ 1, 2, 3, 4, 5, 6 ]
    new_cmd.data = move_data(pos, 'lin', 42, 24)
    self.program.add_command(new_cmd, -1)

  def waitInputOn(self):
    new_cmd = self._commands['WN']
    new_cmd.data = empty_data()
    self.program.add_command(new_cmd, -1)

  def waitInputOff(self):
    new_cmd = self._commands['WF']
    new_cmd.data = empty_data()
    self.program.add_command(new_cmd, -1)

  def setOutputOn(self):
    new_cmd = self._commands['SN']
    new_cmd.data = 'some number'
    self.program.add_command(new_cmd, -1)

  def setOutputOff(self):
    new_cmd = self._commands['SF']
    new_cmd.data = 'some number'
    self.program.add_command(new_cmd, -1)

  def tabNumber(self):
    new_cmd = self._commands['X3']
    new_cmd.data = 'some number'
    self.program.add_command(new_cmd, -1)

  def addComment(self):
    new_cmd = self._commands['AD']
    new_cmd.comment = 'default message'
    self.program.add_command(new_cmd, -1)
    
  def progViewselect(self, line):
    print(line)
