""" """

import unittest
import sys

sys.path.append('../src')

import joint

import unittest
  
class Joint_test(unittest.TestCase):
  """ """
  
  def setUp(self):
    self.Joint = joint.Joint(0, 300, 1400, 0.5, 0, 0)
  
  def test_joint_init(self):
    Joint = joint.Joint(0, 0, 0, 0, 0, 0)
    
    self.assertEqual(Joint.AngleLimitNegative, 0)
    self.assertEqual(Joint.AngleLimitPositive, 0)
    self.assertEqual(Joint.StepLimit, 0)
    self.assertEqual(Joint.DegreePerStep, 0)
    self.assertEqual(Joint.CurrentStep, 0)
    self.assertEqual(Joint.CurrentAngle, 0)
    
  def test_step_positive(self):
    
    self.assertTrue(self.Joint.jog_step(10))
    self.assertFalse(self.Joint.jog_step(1400))
    self.assertEqual(self.Joint.CurrentStep, 10)
  
  def test_step_negative(self):
    self.assertFalse(self.Joint.jog_step(-10))
    
    self.Joint.jog_step(50)
    self.assertTrue(self.Joint.jog_step(-10))
    self.assertEqual(self.Joint.CurrentStep, 40)
    
  def test_angle_postive(self):
    pass
    
