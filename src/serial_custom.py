"""
  Custom serial class
  
  To test some (minor) controller features without the availebility of 
  real ardiuno a serial connection simulator is needed
"""


class Serial():
  """ """
  def __init__(self, port, baudrate):
    self.port = port
    self.baud = baudrate
    self.active = False
    
  def open(self):
    self.active = True
    
  def close(self):
    self.active = False
    
  def write(self, cmd):
    print(cmd)
    
    # TODO: added Arduino behavior here
    
    return cmd
    