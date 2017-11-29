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
    

class programmerTestCase(unittest.TestCase):

  def setUp(self):
    """ """

    self.programmer = programmer.Programmer('', '')
    

    
  def test_class_init(self):
    """ """
    pass
    
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
      self.programmer.add_command(new_cmd, -1)
  
  def test_remove_command(self):
    """remove last command from program"""

    
    for cmd in self.programmer.program:
      print(cmd.data)
    
    
    self.programmer.remove_command(-1)
    
    
    self.assertEqual(self.programmer.program[0].name, 'foo')
    self.assertEqual(self.programmer.program[0].type, 1)
    self.assertEqual(self.programmer.program[0].data, 3)
    self.assertEqual(self.programmer.program[0].comment, 'baz')
    
    
    
if __name__ == '__main__':
  unittest.main()