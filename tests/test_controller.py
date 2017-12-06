""" """

import unittest
import sys

sys.path.append('../src')

import controller

class controllerTestcase(unittest.TestCase):
  """ """
  
  def setUp(self):
    """ """
    self.controller = controller.Controller(6)
    
  def test_controllerInit(self):
    """ """
    
    self.assertEqual(len(self.controller.joints), 6)
    self.assertFalse(self.controller.calibrated)
    
  def test_calibrateRobot(self):
    
    self.assertFalse(self.controller.calibrated)
    self.controller.calibrateRobot()
    self.assertTrue(self.controller.calibrated)
    

  def test_return_joint_status(self):
    self.controller.return_joint_status()
    
  # def suite():
    # suite = unittest.TestSuite()
    # suite.addTest(controllerTestcase('test_controllerInit'))
    
    # return suite