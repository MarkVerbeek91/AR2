"""

"""
import unittest
import sys

sys.path.append('../src')

import program_line

class program_lineTestCAse(unittest.TestCase):
  
  def test_program_line_init(self):
    prog_line = program_line.Program_line(1, 'name', 'type', 'data', 'comment')
    
    self.assertEqual(prog_line._ID, 1)
    self.assertEqual(prog_line._desciption, 'name')
    self.assertEqual(prog_line._protocol, 'type')
    self.assertEqual(prog_line.data, 'data')
    self.assertEqual(prog_line.comment, 'comment')
  
  def test_program_line_print(self):
    pass
    
    # prog_line = program_line('name', 'type', 'data', 'comment')
    
    