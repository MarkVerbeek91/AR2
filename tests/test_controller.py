""" """

import unittest
import sys
import csv

sys.path.append('../src')

import controller
import program_line

class controllerTestcase(unittest.TestCase):
  """ """
  
  def setUp(self):
    """ """
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
    
    self._commands = []
    for row in csvID:
      # print(row)
      new_cmd = program_line.Program_line(int(row[0]), row[1], row[2], 1, '')
      respone = self.controller.executeRow(new_cmd)
      if row[0] == 0 and response == row[1]:
        self.assertTrue()
        
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