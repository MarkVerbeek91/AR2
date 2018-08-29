"""


"""

class ProgramLine():
    """ store program line data in a nice way"""
    def __init__(self, id, description, protocol, data, comment):
        """ init """
        self._id = id
        self._description = description
        self._protocol = protocol
        self.data = data
        self.comment = comment

    def print_program_line(self):
        """ return program line information in string format """
        return str("%s; %s, %s" % (self._description, self.data, self.comment))

    def command(self):
        """ """
        return self._protocol+self.data.get()

    def get_id(self):
        """ return program line id """
        return self._id

    def get_description(self):
        """ return program line description """
        return self._description

    def get_protocol(self):
        """ return program line protocol """
        return self._protocol

class ServoData():
    """ store servo data in a nice way """

    def __init__(self, servo_nr, state):
        """ init """
        self.servo_nr = servo_nr
        self.state = state

    def get(self):
        """ return servo data as command string """
        return str(self.servo_nr) + str(int(self.state))

class MoveData():
    """ store move data in a nice way """
    def __init__(self, position, movement_type, acc, dec):
        """ init """
        self.joint_pos = position
        self.movement_type = movement_type
        self.acceleration = acc
        self.deceleration = dec

    def get(self):
        """ return move data as command string """
        names = ['A', 'B', 'C', 'D', 'E', 'F']

        data = ''
        for i, elm in enumerate(names):
            data += elm + str(self.joint_pos[i])

        if self.movement_type is 'lin':
            data += 'X1'
        else:
            data += 'XX'

        return data + 'Y' + str(self.acceleration) + 'Z' + str(self.deceleration)
