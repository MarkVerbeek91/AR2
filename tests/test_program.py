""" """

import unittest
import sys
import csv

sys.path.append('../src')

import program
import program_line

class programTestcase(unittest.TestCase):
  """ """
  
  def setUp(self):
    """ """
    
    self.program = program.Program()
    
  def test_programInit(self):
    """ Test whether the program is initialised correctly """
    
  def test_add_command(self):
    """ """
    new_cmd = program_line.Program_line(1, 'foo', 1, 'bar', 'baz')
    self.program.add_command(new_cmd, -1)
    
    self.assertEqual(self.program._program[0]._ID, 1)
    self.assertEqual(self.program._program[0]._desciption, 'foo')
    self.assertEqual(self.program._program[0]._protocol, 1 )
    self.assertEqual(self.program._program[0].data, 'bar')
    self.assertEqual(self.program._program[0].comment, 'baz')
  
  def test_add_command_multible(self):
    """ """
    
    for ii in range(1,5):
      new_cmd = program_line.Program_line(1, 'foo', 1, ii, 'baz')
      self.program.add_command(new_cmd, -1)
 
    self.assertEqual(self.program.numberOfCommands(),4)
    
    for ii in range(1,5):
      
      self.assertEqual(self.program._program[ii-1].data, ii)
    # self.assertEqual(self.programmer.program[1].data, 2)
    # self.assertEqual(self.programmer.program[2].data, 3)
    # self.assertEqual(self.programmer.program[3].data, 4)
  
  def test_remove_command(self):
    """remove last command from program"""

    self.assertEqual(self.program.remove_command(-1), -1)
        
    for ii in range(1,5):
      new_cmd = program_line.Program_line(1, 'foo', 1, ii, 'baz')
      self.program.add_command(new_cmd, -1)    
    
    self.program.remove_command(-1)
    
    self.assertEqual(self.program.numberOfCommands(),3)
    
    # self.assertEqual(self.programmer.program[0].name, 'foo')
    # self.assertEqual(self.programmer.program[0].type, 1)
    # self.assertEqual(self.programmer.program[0].data, 3)
    # self.assertEqual(self.programmer.program[0].comment, 'baz')
  
