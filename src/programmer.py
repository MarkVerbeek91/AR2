""" """

import pickle

class program_line():
  def __init__(self, name, type, data, comment):
    self.name = name
    self.type = type
    self.data = data
    self.comment = comment
    

class Programmer():

  def __init__(self, progView, progName):
  
    self.progView = progView
    
    try:
      self.Prog = pickle.load(open(progName,"rb"))
    except:
      self.Prog = ['##BEGINNING OF PROGRAM##','Tab Number 1']
      
      try: 
        pickle.dump(self.Prog,open(progName,"wb"))   
      except:
        pickle.dump(self.Prog,open("new","wb"))
    
    self.program = []
  
  def add_command(self, new_cmd, var):
    if var == -1:
      self.program.append(new_cmd)
    else:
      self.program.insert(var, new_cmd)
  
  def remove_command(self, var):
    if var == -1:
      self.program.pop()
    else:
      self.program.pop(var)
  
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