""" """

import pickle


class Programmer():

  def __init__(self, progFrame, progName):
  
    self.progFrame = progFrame
    
    try:
      self.Prog = pickle.load(open(progName,"rb"))
    except:
      self.Prog = ['##BEGINNING OF PROGRAM##','Tab Number 1']
      
      try: 
        pickle.dump(self.Prog,open(progName,"wb"))   
      except:
        pickle.dump(self.Prog,open("new","wb"))
    
  
  def manAddItem(self):
    print("hello")
    
  def teachInsertBelSelected(self):
    pass
 
  def teachReplaceSelected(self):
    pass
    
  def waitTime(self):
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