"""   Joint Class

  This class stores all data for a joint and (perhaps) does some checks
  of movements/actions are allowed.
"""

class Joint():
    """ place to keep data of each joint on one place"""

    def __init__(self, aln, alp, slm, dps, cus, cua):
        """ set all internal values """
        self.angle_limit_negative = aln
        self.angle_limit_positive = alp
        self.step_limit_min = 0
        self.step_limit_max = slm    # maximum number of steps for range
        self._degree_per_step = dps
        self.current_step = cus
        self._current_angle = cua
        self.short_name = 'empty'

    def jog_step(self, step_size):
        """ check if step can be made """
        if self.current_step + step_size < self.step_limit_max and \
           self.current_step + step_size > self.step_limit_min:
            self.current_step += step_size
            return_value = True
        else:
            return_value = False

        return return_value

    def jog_angle(self, angle_size):
        """ check if angle change can be made """
        return False
