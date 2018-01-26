"""


"""

class Program_line():
    """ """
    def __init__(self, id, desciption, protocol, data, comment):
        """  """
        self._ID         = id
        self._desciption = desciption
        self._protocol   = protocol
        self.data        = data
        self.comment     = comment

    def print_program_line(self):
        """ return program line information in string format """
        return str("%s; %s, %s" % (self._desciption, self.data, self.comment))

    def command(self):
        """ """
        return self._protocol+self.data.get()

class servo_data():
    """ """

    def __init__(self, servo_nr, state):
        """ """
        self.servo_nr = servo_nr
        self.state    = state

    def get(self):
        """ """
        return str(self.servo_nr) + str(int(self.state))

class move_data():
    """ """
    def __init__(self, position, movement_type, acc, dec):
        """ """
        self.joint_pos = position
        self.movement_type = movement_type
        self.acceleration  = acc
        self.deceleration  = dec

    def get(self):
        """ """
        names = ['A', 'B', 'C', 'D', 'E', 'F']

        data = ''
        for ii, elm in enumerate(names):
            data += elm + str(self.joint_pos[ii])

        if self.movement_type is 'lin':
            data += 'X1'
        else:
            data += 'XX'

        return data + 'Y' + str(self.acceleration) + 'Z' + str(self.deceleration)

