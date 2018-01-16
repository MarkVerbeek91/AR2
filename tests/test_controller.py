""" """

import unittest
import sys
import csv

sys.path.append('../src')

import controller
import program_line
from program_line import move_data
from program_line import servo_data

class empty_data():
  """ """
  
  def __init__(self):
    pass
    
  def get(self):
    return ''

class controllerTestcase(unittest.TestCase):
  """ """
  
  def setUp(self):
    """ Setting up controller """
    self.nr_joint = 6
    self.controller = controller.Controller(self.nr_joint)
    
  def test_controllerInit(self):
    """ Test whether the controller is initialised correctly """
    
    self.assertEqual(len(self.controller.joints), self.nr_joint)
    self.assertTrue(self.controller.serCom.open)
    self.assertFalse(self.controller.calibrated)
    self.assertFalse(self.controller.running)
    self.assertFalse(self.controller.stop)
    
  def test_executeRow(self):
    """ Check for each default command if the response is good """
    
    fileID = open('../conf/conf_commands.csv')
    csvID  = csv.reader(fileID, delimiter=',')
    
    
   
  def test_executeMovement(self):
    """ """
    pos = [ 1, 2, 3, 4, 5, 6 ]
    movement = move_data(pos, 'lin', 42, 24)
    command = program_line.Program_line(1, 'Move', 'MV', movement, 'position 1')
   
    self.assertEqual(self.controller.executeRow(command), 'MVA1B2C3D4E5F6X1Y42Z24\n')
   
  def test_waitOnInputOn(self):
    """ """
    servo = servo_data(1, False)
  
   
  def test_program1(self):
    """ Run program 1 """
  
    
  
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