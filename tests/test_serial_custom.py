""" """

import unittest
import sys

sys.path.append('../src')
import serial_custom as serial

class serialTestcase(unittest.TestCase):
  """ """
  
  def setUp(self):
    """ """
    port = 5
    baudrate = 9600
    self.serial = serial.Serial(port, baudrate)
    
  def test_serialInit(self):
    """ """
    
    self.assertEqual(self.serial.port, 5)
    self.assertEqual(self.serial.baud, 9600)
        
  def test_serialWrite(self):
    
    # TODO: added test for arduino behavior here when implemented
    cmd = "some test command"
    cmd_res = self.serial.write(cmd)
    self.assertEqual(cmd, cmd_res)
    