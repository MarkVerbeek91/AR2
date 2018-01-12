""" """

import unittest

import sys

sys.path.append('../src')

import programmer
import program
import program_line

class programmerTestCase(unittest.TestCase):

  def setUp(self):
    """ """
    print("\nCreating new programmer\n")
    self.programmer = programmer.Programmer('')

    
  def test_class_init(self):
    """ Test if class is correctly initialised """
    #self.assertIsInstance(self.programmer.program, program)
    self.assertEqual(len(self.programmer._commands), 15)
    
    self.assertEqual(len(self.programmer.controller.joints), 
                         self.programmer.number_of_joints)
    
    # open programmer no file exist
    
    # open programmer file exist
    
    # check for correct message
    
    
    
    
  def test_add_and_run_command(self):
    """ """
       
    self.programmer.teachInsertBelSelected()

    self.programmer.run_program_line(1)
    
    
    
if __name__ == '__main__':
  unittest.main()
  
  
  
