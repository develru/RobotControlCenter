__author__ = 'develru'

import sys
from PySide import QtGui
import controlcenter

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    cc = controlcenter.ControlWindow()
    cc.show()
    app.exec_()

