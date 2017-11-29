""" 
"""

import gui
import joint

import controller
import programmer

import sys

import time

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
  
  GUI = gui.GuiAR2()
  GUI.CreateTab1()
  
  GUI.start()
  

if __name__ == "__main__":
  main()
  
