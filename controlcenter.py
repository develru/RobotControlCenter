__author__ = 'develru'

from PySide import QtGui, QtCore
import uiMainWindow


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.mdiArea.addSubWindow(self.toolWindow)
        self.toolWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinMaxButtonsHint)