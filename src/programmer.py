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



class movement():
  def __init__(self, pos, vel, acc, type):
    self.pos = pos
    self.acc = acc
    self.vel = vel
    self.type = 'linear' # only one supported, is implemented in arduino software
    
    # TODO: type linear movement
    
    # TODO: type sinus movement
    
    
class Programmer():

  def __init__(self, progName):
  
    try:
      # print("Trying to open %s" % progName)
      self.Prog = pickle.load(open(progName,"rb"))
    except:
      # print("Program does not exist, creating new one")
      self.Prog = ['##BEGINNING OF PROGRAM##','Tab Number 1']
      
      try: 
        pickle.dump(self.Prog,open(progName,"wb"))   
      except:
        pickle.dump(self.Prog,open("new","wb"))
    
    self.program = []
    self.current_line = -1
    
    # TODO: load protocol 
    
    fileID = open('../conf/conf_commands.csv')
    csvID  = csv.reader(fileID, delimiter=',')
    
    self._commands = []
    for row in csvID:
      # print(row)
      new_cmd = program_line.Program_line(int(row[0]), row[1], row[2], '', '')
      self._commands.append(new_cmd)
    
    self.number_of_joints = 6
    self.controller = controller.Controller(self.number_of_joints)
    
  def add_command(self, new_cmd, var):
    if var == -1:
      self.program.append(new_cmd)
    else:
      self.program.insert(var, new_cmd)
  
  def remove_command(self, var):
    if var == -1:
      try:
        self.program.pop()
      except: 
        return -1
    else:
      try:
        self.program.pop(var)
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
    if self.controller.running:
      print('stopping program')      
      self.controller.stop = True
    else:
      print('no programming running')
  
  def run_program_line(self, var):
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
    new_cmd = self._commands[0]
    new_cmd.data = 'some very numbery string'
    self.add_command(new_cmd, -1)
    
  def teachReplaceSelected(self):
    new_cmd = self._commands[0]
    new_cmd.data = 'some very numbery string'
    self.add_command(new_cmd, -1)
    
  def waitInputOn(self):
    new_cmd = self._commands[2]
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)
    
  def waitInputOff(self):
    new_cmd = self._commands[3]
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)
    
  def setOutputOn(self):
    new_cmd = self._commands[4]
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)
    
  def setOutputOff(self):
    new_cmd = self._commands[5]
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)
    
  def tabNumber(self):
    new_cmd = self._commands[6]
    new_cmd.data = 'some number'
    self.add_command(new_cmd, -1)
    
    
  def progViewselect(self, line):  
    print(line)
    pass

