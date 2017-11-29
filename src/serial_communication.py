""" Class file for serial communication 

"""
try:
  import serial
except ImportError:
  pass
  # import Serial as serial

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
  def open(self):
    """ """
    port = "COM" + self.port_number  
    baud = 9600 
    serial_com = serial.Serial(port, baud)

  def send_command(self, command):
    if command[-1:] == '\n':
      self.serial_com.write(command)
    else:
      print("command not properly formatted")