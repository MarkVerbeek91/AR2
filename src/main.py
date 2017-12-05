""" 
  Main script of the AR2 control software
  
  A Gui is initiated and started. 
  
  Probably the controller and programmer should be started here to...
"""

import sys
import time

import gui
import joint
import controller
import programmer

if sys.platform == 'win32':
  PLATFORM = 'pc'
  
  """ Set variables for pc env
  """
  
elif sys.platform == 'linux':
  PLATFORM = 'pi'
  
  """ Set variables for pi env
  """
  
def main():
  """
  """
  
  # pdb.set_trace()
  
  GUI = gui.GuiAR2()
  GUI.CreateTab1()
  
  GUI.start()
  
  print('program exited')

if __name__ == "__main__":
  main()
  
