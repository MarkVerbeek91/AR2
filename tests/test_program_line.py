"""
    Test the ProgramLine Class, ServoData and MoveData Classes
"""

import unittest
import sys

sys.path.append('../src')

from program_line import ProgramLine
from program_line import MoveData
from program_line import ServoData

class ProgramLineTestCase(unittest.TestCase):
    """ Test the ProgramLine Class, ServoData and MoveData Classes """

    def test_program_line_init(self):
        """ test program line init """
        prog_line = ProgramLine(1, 'name', 'type', 'data', 'comment')

        self.assertEqual(prog_line.get_id(), 1)
        self.assertEqual(prog_line.get_description(), 'name')
        self.assertEqual(prog_line.get_protocol(), 'type')
        self.assertEqual(prog_line.data, 'data')
        self.assertEqual(prog_line.comment, 'comment')

    def test_program_line_print(self):
        """ test program line return stirng function """
        pass

    # prog_line = program_line('name', 'type', 'data', 'comment')

    def test_program_line_command(self):
        """ test program line commands """
        pos = [1, 2, 3, 4, 5, 6]
        movement = MoveData(pos, 'lin', 42, 24)
        cmd = ProgramLine(1, 'Move', 'MV', movement, 'position 1')

        self.assertEqual(cmd.command(), 'MVA1B2C3D4E5F6X1Y42Z24')

        servo1 = ServoData(1, False)
        cmd = ProgramLine(2, 'Servo Off', 'WF', servo1, 'gripper')

        self.assertEqual(cmd.command(), 'WF10')

        servo1 = ServoData(1, True)

        cmd = ProgramLine(2, 'Servo Off', 'WF', servo1, 'gripper')
        self.assertEqual(cmd.command(), 'WF11')

    def test_movedata(self):
        """ test the get function of MoveData """
        pos = [1, 2, 3, 4, 5, 6]
        movement = MoveData(pos, 'lin', 42, 24)

        self.assertEqual(movement.get(), 'A1B2C3D4E5F6X1Y42Z24')

    def test_servodata(self):
        """ test the get function of ServoData """
        servo = ServoData(1, True)
        self.assertEqual(servo.get(), '11')
        servo = ServoData(2, False)
        self.assertEqual(servo.get(), '20')
