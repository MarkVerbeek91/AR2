""" """

class Joint():

  def __init__(self):
    self.short_name         = ''
    self.AngleLimitNegative = 0
    self.AngleLimitPositive = 0
    self.StepLimit          = 0
    self.DegreePerStep      = 0
    self.CurrentStep        = 0
    self.CurrentAngle       = 0
    
  