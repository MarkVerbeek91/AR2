"""
  Controller class
  
  This class takes a program and execute its by communicating it with the 
  arduino controller (or simulated serial bridge)
  
  
"""

import joint
import serial_communication as sc
from string import ascii_uppercase

import time

class Controller():

  def __init__(self, number_of_joints):
    """ Setup  """
    self.joints = []
    for ii in range(0,number_of_joints):
      self.joints.append(joint.Joint(-1,-1,-1,-1,-1,-1))
    
    #TODO: add init values of joints
    
    self.serCom     = sc.Serial_communication(5)
    self.serCom.open(self.serCom)
    self.calibrated = False
    
  def executeRow(self, program_line):
    """ Execute program line """
    print(program_line._ID)
    
    if program_line._ID == 1:
      print('executing something')
      
      if self.serCom.is_active:
        cmd = str(program_line._protocol)+str(program_line.data)+'\n'
        self.serCom.send_command(cmd)
      else:
        print("Serial Port not open")
    elif program_line._ID == 2:
      
      time.sleep(program_line.data)
      
    else:
      print('not doing anything')
    
    
    
  def calibrateRobot(self):
    """ Do a full robot calibration """
    command = "LL"
    
    for joint in self.joints:
      command = command + joint.short_name + str(joint.StepLimit)
      
    command = command + "\n"

    response = self.serCom.send_command("pass\n")
    
    if (response == "pass\n"):
      self.calibrated = True
    else:
      print(response)
    # reset value in gui. 