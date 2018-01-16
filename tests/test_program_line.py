"""

"""
import unittest
import sys

sys.path.append('../src')

import program_line
from program_line import move_data
from program_line import servo_data


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

  def test_program_line_command(self):
    """ """
    pos = [ 1, 2, 3, 4, 5, 6 ]
    movement = move_data(pos, 'lin', 42, 24)
    cmd = program_line.Program_line(1, 'Move', 'MV', movement, 'position 1')
    
    self.assertEqual(cmd.command(), 'MVA1B2C3D4E5F6X1Y42Z24')
  
    servo1 = servo_data(1, False)
    cmd = program_line.Program_line(2, 'Servo Off', 'WF', servo1, 'gripper') 
    
    self.assertEqual(cmd.command(), 'WF10')
      
    servo1 = servo_data(1, True)
      
    cmd = program_line.Program_line(2, 'Servo Off', 'WF', servo1, 'gripper') 
    self.assertEqual(cmd.command(), 'WF11')
    
  def test_movedata(self):
  
    pos = [ 1, 2, 3, 4, 5, 6 ]
    movement = move_data(pos, 'lin', 42, 24)
    
    self.assertEqual(movement.get(), 'A1B2C3D4E5F6X1Y42Z24')
      
  def test_servodata(self):
    """ """
    servo = servo_data(1, True)
    self.assertEqual(servo.get(), '11')
    servo = servo_data(2, False)
    self.assertEqual(servo.get(), '20')
    
      