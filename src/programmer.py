""" """

import pickle

class program_line():
  def __init__(self, name, type, data, comment):
    self.name = name
    self.type = type
    self.data = data
    self.comment = comment
    
  def print_program_line(self):
    
    print("%s; %i; %s, %s" % (self.name, self.type, self.data, self.comment))

class movement():
  def __init__(self, pos, vel, acc, type):
    self.pos = pos
    self.acc = acc
    self.vel = vel
    self.type = type
    
    self.ang = '' # calc angles 
    
    # TODO: type lineair movement
    
    # TODO: type sinus movement
    
    
class Programmer():

  def __init__(self, progName):
  
    try:
      print("Trying to open %s" % progName)
      self.Prog = pickle.load(open(progName,"rb"))
    except:
      print("Program does not exist, creating new one")
      self.Prog = ['##BEGINNING OF PROGRAM##','Tab Number 1']
      
      try: 
        pickle.dump(self.Prog,open(progName,"wb"))   
      except:
        pickle.dump(self.Prog,open("new","wb"))
    
    self.program = []
    self.current_line = -1
  
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
  
  def insertReturn(self, pos):
    new_cmd = program_line('return', 1, 'none', '')
    self.add_command(new_cmd, pos)
 
  def waitTime(self, pos, waitTime):
    new_cmd = program_line('wait', 2, waitTime, 'seconds')
    add_command(new_cmd, pos)
    
  def teachInsertBelSelected(self):
    pass
 
  def teachReplaceSelected(self):
    pass
    
  
    
  def waitInputOn(self):
    pass
    
  def waitInputOff(self):
    pass
    
  def setOutputOn(self):
    pass
    
  def setOutputOff(self):
    pass
    
  def tabNumber(self):
    pass
    
    
  def progViewselect(self, line):  
    print(line)
    pass

