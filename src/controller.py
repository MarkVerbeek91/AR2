""" """

import joint
import serial_communication as sc
from string import ascii_uppercase

class Controller():

  def __init__(self):
    self.joints = []
    for ii in range(0,6):
      self.joints.append(joint.Joint())
    
    #TODO: add init values of joints
    
    self.serCom     = sc.Serial_communication(5)
    self.serCom.open(self.serCom)
    self.calibrated = False
    
  def executeRow(self, program_line):
    print(program_line.type)
    
    if program_line.type == 1:
      print('executing something')
    else:
      print('not doing anything')
    
    
    
  def calibrateRobot(self):
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