""" """

import unittest

import sys

sys.path.append('../src')

import programmer
from programmer import program_line

class program_linteTestCAse(unittest.TestCase):
  
  def test_program_line_init(self):
    prog_line = program_line('name', 'type', 'data', 'comment')
    
    self.assertEqual(prog_line.name, 'name')
    self.assertEqual(prog_line.type, 'type')
    self.assertEqual(prog_line.data, 'data')
    self.assertEqual(prog_line.comment, 'comment')
  
  def test_program_line_print(self):
    pass
    
    # prog_line = program_line('name', 'type', 'data', 'comment')
    
    
      

class programmerTestCase(unittest.TestCase):

  def setUp(self):
    """ """
    print("\nCreating new programmer\n")
    self.programmer = programmer.Programmer('')
    

    
  def test_class_init(self):
    """ """
    self.assertEqual(self.programmer.program, [])
    
    # open programmer no file exist
    
    # open programmer file exist
    
    # check for correct message
    
    
    
  def test_add_command(self):
    """ """
    new_cmd = program_line('foo', 1, 'bar', 'baz')
    self.programmer.add_command(new_cmd, -1)
    
    self.assertEqual(self.programmer.program[0].name, 'foo')
    self.assertEqual(self.programmer.program[0].type, 1)
    self.assertEqual(self.programmer.program[0].data, 'bar')
    self.assertEqual(self.programmer.program[0].comment, 'baz')
  
  def test_add_command_multible(self):
    """ """
    new_cmd = program_line('foo', 1, -1, 'baz')
    for ii in range(1,5):
      new_cmd.data = ii
      new_cmd.print_program_line()
      self.programmer.add_command(new_cmd, -1)
      
  
    self.assertEqual(self.programmer.numberOfCommands(),4)
    
    for ii in range(1,5):
      print(self.programmer.program[ii-1].data)
      self.assertEqual(self.programmer.program[ii-1].data, ii)
  
  def test_remove_command(self):
    """remove last command from program"""

    self.assertEqual(self.programmer.remove_command(-1), -1)
    
    # for cmd in self.programmer.program:
      # print(cmd.data)
    
    
    
    
    
    # self.assertEqual(self.programmer.program[0].name, 'foo')
    # self.assertEqual(self.programmer.program[0].type, 1)
    # self.assertEqual(self.programmer.program[0].data, 3)
    # self.assertEqual(self.programmer.program[0].comment, 'baz')
    
    
    
if __name__ == '__main__':
  unittest.main()