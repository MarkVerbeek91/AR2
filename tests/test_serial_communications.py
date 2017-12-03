""" pytest file
"""

import sys

sys.path.append('../src')

from serial_communication import serial_coms


def assert_open_port():
  """ some comment
  """
  assert False

def test_make_class():
  """
  """

  serCom = serial_coms()
  
  assert True

def test_class_init():
  """
  """
  
  serCom = serial_coms()
  
  assert serCom.serial_com == [] 
  assert serCom.is_active  == False

