__author__ = 'develru'

from PySide import QtGui
import pyMainWindow


class ControlWindow(QtGui.QMainWindow, pyMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.mdiArea.addSubWindow(self.toolWindow)