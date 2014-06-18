from controlcenter import controlcenter

__author__ = 'develru'

import sys
# from PySide import QtGui
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    cc = controlcenter.ControlWindow()
    cc.show()
    app.exec_()

