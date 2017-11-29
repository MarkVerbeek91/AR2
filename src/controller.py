""" """

import joint
import serial_communication
from string import ascii_uppercase

class Controller():

  def __init__(self, ):
    self.joints[6] = joint.Joint()
    self.serCom    = serial_communication.Serial()
    self.serCom.open()
    self.calibrated = False
    
  def executeRow():
    pass
    
    
    
  def calibrateRobot(self):
    command = "LL"
    
    for joint in self.joints:
      command = command + joint.short_name + str(joint.Steplimit)
      
    command = command + "\n"

    response = self.serCom.write(command)
    
    if (response == "pass\n"):
      self.calibrated = True
    
    # reset value in gui. 