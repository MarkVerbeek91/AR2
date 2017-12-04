""" """

class Joint():

  def __init__(self, ALN, ALP, SL, DPS, CS, CA):
    self.AngleLimitNegative = ALN
    self.AngleLimitPositive = ALP
    self.StepLimitMin       = 0
    self.StepLimit          = SL    # maximum number of steps for range
    self._DegreePerStep     = DPS
    self.CurrentStep        = CS
    self._CurrentAngle      = CA
    
  def jog_step(self, stepSize):
    if self.CurrentStep + stepSize < self.StepLimit and \
       self.CurrentStep + stepSize > self.StepLimitMin:
      self.CurrentStep += stepSize
      return True
    else:
      return False
    
  def jog_angle(self, angleSize):
    return False
