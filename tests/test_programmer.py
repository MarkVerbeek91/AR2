""" """

import unittest

import sys

sys.path.append('../src')

import programmer
from programmer import program_line


      

class programmerTestCase(unittest.TestCase):

  def setUp(self):
    """ """
    print("\nCreating new programmer\n")
    self.programmer = programmer.Programmer('')
    self.programmer.clear_program()

    
  def test_class_init(self):
    """ """
    self.assertEqual(self.programmer.program, [])
    self.assertEqual(self.programmer.current_line, -1)
    self.assertEqual(len(self.programmer._commands), 15)
    
    self.assertEqual(len(self.programmer.controller.joints), self.programmer.number_of_joints)
    
    # open programmer no file exist
    
    # open programmer file exist
    
    # check for correct message
    
    
    
  def test_add_command(self):
    """ """
    new_cmd = program_line.Program_line(1, 'foo', 1, 'bar', 'baz')
    self.programmer.add_command(new_cmd, -1)
    
    self.assertEqual(self.programmer.program[0]._ID, 1)
    self.assertEqual(self.programmer.program[0]._desciption, 'foo')
    self.assertEqual(self.programmer.program[0]._protocol, 1 )
    self.assertEqual(self.programmer.program[0].data, 'bar')
    self.assertEqual(self.programmer.program[0].comment, 'baz')
  
  def test_add_command_multible(self):
    """ """
    
    for ii in range(1,5):
      new_cmd = program_line.Program_line(1, 'foo', 1, ii, 'baz')
      self.programmer.add_command(new_cmd, -1)
 
    self.assertEqual(self.programmer.numberOfCommands(),4)
    
    for ii in range(1,5):
      
      self.assertEqual(self.programmer.program[ii-1].data, ii)
    # self.assertEqual(self.programmer.program[1].data, 2)
    # self.assertEqual(self.programmer.program[2].data, 3)
    # self.assertEqual(self.programmer.program[3].data, 4)
  
  def test_remove_command(self):
    """remove last command from program"""

    self.assertEqual(self.programmer.remove_command(-1), -1)
        
    for ii in range(1,5):
      new_cmd = program_line.Program_line(1, 'foo', 1, ii, 'baz')
      self.programmer.add_command(new_cmd, -1)    
    
    self.programmer.remove_command(-1)
    
    self.assertEqual(self.programmer.numberOfCommands(),3)
    
    # self.assertEqual(self.programmer.program[0].name, 'foo')
    # self.assertEqual(self.programmer.program[0].type, 1)
    # self.assertEqual(self.programmer.program[0].data, 3)
    # self.assertEqual(self.programmer.program[0].comment, 'baz')
    
  def test_add_and_run_command(self):
    """ """
       
    self.programmer.teachInsertBelSelected()

    self.programmer.run_program_line(1)
    
    
    
if __name__ == '__main__':
  unittest.main()
  
  
  
