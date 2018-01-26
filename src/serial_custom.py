"""
    Custom serial class

    To test some (minor) controller features without the availebility of
    real ardiuno a serial connection simulator is needed
"""


class Serial():
    """ Custrom serial communication class """

    def __init__(self, port, baudrate):
        """ set port number and baudrate """
        self.port = port
        self.baud = baudrate

    def write(self, cmd):
        """ mimic behavior of arduino """
        print(cmd)

        # TODO: added Arduino behavior here

        return cmd
