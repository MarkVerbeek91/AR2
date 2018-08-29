"""
    Main script of the AR2 control software

    A Gui is initiated and started.

    Probably the controller and programmer should be started here to...
"""

from __future__ import print_function

import sys

import gui

if sys.platform == 'win32':
    """ Set variables for pc env """
    PLATFORM = 'pc'

elif sys.platform == 'linux':
    """ Set variables for pi env """
    PLATFORM = 'pi'

def main():
    """ start gui """

    # pdb.set_trace()

    ar2_gui = gui.GuiAR2()
    ar2_gui.CreateTab1()

    ar2_gui.start()

    print('program exited')

if __name__ == "__main__":
    """ start program """
    main()
