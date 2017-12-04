""" unittest file
"""
import unittest

import sys

sys.path.append('../src')

import serial_communication as sc

class serialTestCase(unittest.TestCase):

  def setUp(self):
    """ """

    self.serial = sc.Serial_communication(5)
    
  def tearDown(self):
    """ """
    self.serial.close()
    
  def test_class_init(self):
    """ """
    
    self.assertEqual(self.serial.serial_com, [])
    self.assertFalse(self.serial.is_active)
    self.assertEqual(self.serial.port_number, 5)

if __name__ == '__main__':
    unittest.main()