""" """

import unittest
import sys

sys.path.append('../src')

import joint

class Joint_test(unittest.TestCase):
  """ """

  def setUp(self):
    self.Joint = joint.Joint(0, 300, 1400, 0.5, 0, 0)

  def test_joint_init(self):
    Joint = joint.Joint(0, 0, 0, 0, 0, 0)

    self.assertEqual(Joint.angle_limit_negative, 0)
    self.assertEqual(Joint.angle_limit_positive, 0)
    self.assertEqual(Joint.step_limit_max, 0)
    self.assertEqual(Joint._degree_per_step, 0)
    self.assertEqual(Joint.current_step, 0)
    self.assertEqual(Joint._current_angle, 0)

  def test_step_positive(self):

    self.assertTrue(self.Joint.jog_step(10))
    self.assertFalse(self.Joint.jog_step(1400))
    self.assertEqual(self.Joint.current_step, 10)

  def test_step_negative(self):
    self.assertFalse(self.Joint.jog_step(-10))

    self.Joint.jog_step(50)
    self.assertTrue(self.Joint.jog_step(-10))
    self.assertEqual(self.Joint.current_step, 40)

  def test_angle_postive(self):
    pass

