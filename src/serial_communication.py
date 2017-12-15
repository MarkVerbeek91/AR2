""" 
  Serial communication Class

  To keep the serial communication separate from the controller a serial 
  coms class is created that takes care of most communication with any 
  serial port.
"""
try:
  import serial
except ImportError:
  print("opening alternative")
  import serial_custom as serial
  # import Serial as serial

class Serial_communication():
  """ """

  def __init__(self, port_number):
    """  """
    self.serial_com  = []
    self.is_active   = False
    self.port_number = port_number

  def close(self):
    """ close com port when open """
    if self.is_active:
      self.serial_com.close()
      self.is_active   = False
    else:
      print('port was not open')
      
  @staticmethod
  def open(self):
    """ open com port when closed """
    if not self.is_active:
      port = "COM" + str(self.port_number)
      baud = 9600 
      self.serial_com = serial.Serial(port, baud)
      self.is_active  = True
    else:
      print("port was already open")
      
  def send_command(self, command):
    """ Send command to port when commands ends with \n """
    if command[-1:] == '\n':
      return self.serial_com.write(command)
    else:
      print("command not properly formatted")