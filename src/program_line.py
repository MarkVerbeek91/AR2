""" 


"""

class Program_line():
  def __init__(self, ID, Desciption, protocol, data, comment):
    """  """
    self._ID         = ID
    self._desciption = Desciption
    self._protocol   = protocol
    self.data        = data
    self.comment     = comment
    
  def print_program_line(self):
    """ print program line information to screen """
    
    return str("%s; %s, %s" % (self._desciption, self.data, self.comment))
    