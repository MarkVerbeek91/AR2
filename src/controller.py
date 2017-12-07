"""
  Controller class
  
  This class takes a program and execute its by communicating it with the 
  arduino controller (or simulated serial bridge)
  
  
"""

import joint
import serial_communication as sc
import program_line

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
    self.running    = False
    self.stop       = False
    
  def executeRow(self, program_line):
    """ Execute program line """
    print(program_line._ID)
    
    if self.running:
      print('controller buzy')
      return 
    
    self.running = True
    
    if program_line._ID == 1:
      """ executing a movement """
      print('executing something')
      
      if self.serCom.is_active:
        cmd = str(program_line._protocol)+str(program_line.data)+'\n'
        response = self.serCom.send_command(cmd)
      else:
        print("Serial Port not open")
    elif program_line._ID == 2:
      """ waiting """
      time.sleep(program_line.data)
      response = True
    elif program_line._ID == 3:
      """ waiting on input ON """
      wait_time = 1 # seconds
      while not self.stop and wait_time > 0:
        response = self.serCom.send_command("input status")
        time.sleep(0.1)
        wait_time -= 0.1
      pass
    elif program_line._ID == 4:
      """ waiting on input OFF """
      pass
    elif program_line._ID == 5:
      """ setting output ON """
      pass
    elif program_line._ID == 6:
      """ setting output OFF """
      pass
    elif program_line._ID == 7:
      """ Conditional input ON """
      pass
    elif program_line._ID == 8:
      """ Conditional input OFF """
      pass
    elif program_line._ID == 9:
      """ Conditional register EQUAL """
      pass
    elif program_line._ID == 10:
      """ Conditional register SMALLER """
      pass
    elif program_line._ID == 11:
      """ Conditional register BIGGER """
      pass
    else:
      print('not doing anything')
    
    self.running = False
    try:
      return response
    except UnboundLocalError:
      return "command not defined"
  
  def executeProgram(self, program):
    """ Executing program """
    
    if self.running:
      print('controller busy')
      return
  
    for prog_line in program:
      if not self.stop:
        print(prog_line)
        self.executeRow(prog_line)
        time.sleep(1)
      else:
        print('program needed stopping')
  
    self.running = False
  
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
      
  def return_joint_status(self):
    std = ''
    
    for joint in self.joints:
      std += str(joint.CurrentStep)
    
    print(std)
    return std
      
    # reset value in gui. 