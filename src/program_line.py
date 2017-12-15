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
    print("%s; %i; %s, %s" % (self.name, self.type, self.data, self.comment))