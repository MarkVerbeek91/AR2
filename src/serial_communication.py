""" Class file for serial communication 

"""

import serial

class Serial_communication():
  """ """

  def __init__(self, port_number):
    """ """

    self.serial_com  = []
    self.is_active   = False
    self.port_number = port_number

  def close(self):
    if self.is_active:
      self.serial_com.close()
    else:
      print('port was not open')
      
  @staticmethod
  def setCom(self):
    """ """
    port = "COM" + self.port_number  
    baud = 9600 
    serial_com = serial.Serial(port, baud)
