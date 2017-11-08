
import unittest

import sys

sys.path.append('../src')

from serial_communication import serial_coms

class serialTestCase(unittest.TestCase):

  def setUp(self):
    """ """

    self.serial = serial_coms()
    
  def tearDown(self):
    """ """
    self.serial.close()
    
  def test_class_init(self):
    """ """
    
    self.assertEqual(self.serial.serial_com, [])
    self.assertFalse(self.serial.is_active)
    self.assertEqual(self.serial.port_number, -1)

if __name__ == '__main__':
    unittest.main()