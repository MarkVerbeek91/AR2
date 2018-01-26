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
    
    self.current_line = 0
    
  def executeRow(self, program_line):
    """ Execute program line """
    print(program_line._ID)
        
    if not self.calibrateRobot:
      print("Warning: robot not calibrated")
    
    if not self.serCom.is_active:
      print("Serial Port not open")
      return 
      
    if program_line._ID == 1:
      """ executing a movement """
      
      cmd = program_line.command()+'\n'
      response = self.serCom.send_command(cmd)
      
      
      
    elif program_line._ID == 2:
      """ waiting """
      time.sleep(program_line.data)
      response = True
    elif program_line._ID == 3:
      """ waiting on input ON """
      wait_time = 1 # seconds
      while not self.stop and wait_time > 0:
        cmd = program_line.command()+'\n'
        response = self.serCom.send_command(cmd)
        time.sleep(0.1)
        wait_time -= 0.1
      
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
    elif program_line._ID == 12:
      """ Start of program (recursive?) """
      pass
    elif program_line._ID == 13:
      """ A marker line, to nothing """
      pass
    elif program_line._ID == 14:
      """ Jump to a marker """
      program.current_line = program_line.data
      pass
    elif program_line._ID == 15:
      """ This is a commend ignore """
      pass
    else:
      print('not doing anything')
    
    try:
      return response
    except UnboundLocalError:
      return "command not defined"
  
  def executeProgram(self, program, program_line_nr = -1):
    """ Executing program """
    
    if self.running:
      print('controller busy')
      return
  
    self.current_line = 0
    self.running = True
    
    if program_line_nr == -1:
      self.executeRow(program._program[program_line_nr])
    
    for prog_line in program._program:
      if not self.stop:
        print(prog_line)
        self.executeRow(prog_line)
        self.current_line += 1
        
        time.sleep(1)
      else:
        print('program needed stopping')
        self.stop = False
        break
  
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