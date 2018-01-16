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
    self.assertEqual(self.program.current_line, -1)
    self.assertEqual(self.program._program, [])
    
  def test_add_command(self):
    """ Test adding of a command """
    #print('\nAdding command and check format')
    new_cmd = program_line.Program_line(1, 'foo', 1, 'bar', 'baz')
    self.program.add_command(new_cmd, -1)
    
    self.assertEqual(self.program._program[0]._ID, 1)
    self.assertEqual(self.program._program[0]._desciption, 'foo')
    self.assertEqual(self.program._program[0]._protocol, 1 )
    self.assertEqual(self.program._program[0].data, 'bar')
    self.assertEqual(self.program._program[0].comment, 'baz')
    
  
  def test_add_command_multible(self):
    """ Test adding multible commands """
    #print('\nAdding multible commands')
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
    #print('\nProgram is empty so no can command can be removed')
    self.assertEqual(self.program.remove_command(-1), -1)
        
    #print('adding 4 commands to program')
    for ii in range(1,5):
      new_cmd = program_line.Program_line(1, 'foo', 1, ii, 'baz')
      self.program.add_command(new_cmd, -1)    
    
    #print('removing one command')
    self.program.remove_command(-1)
    
    #print('check if there are 3 remaining commands')
    self.assertEqual(self.program.numberOfCommands(),3)
    
    # self.assertEqual(self.programmer.program[0].name, 'foo')
    # self.assertEqual(self.programmer.program[0].type, 1)
    # self.assertEqual(self.programmer.program[0].data, 3)
    # self.assertEqual(self.programmer.program[0].comment, 'baz')
  
