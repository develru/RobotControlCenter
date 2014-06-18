from pyUi import uiLogWindow, uiMainWindow, uiToolWindow, uiConnectWindow
# from PySide import QtGui
from PyQt4 import QtGui

__author__ = 'develru'


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect_win = ConnectWindow()
        #self.mdiArea.addSubWindow(self.connect_win)
        #self.connect_win.hide()

        self.connectBtn.clicked.connect(self.connect_to_robot)

    def connect_to_robot(self):
        self.mdiArea.addSubWindow(self.connect_win)
        self.connect_win.show()
        self.tBrLog.append('Connect pressed')


class LogWindow(QtGui.QWidget, uiLogWindow.Ui_logWin):

    def __init__(self, parent=None):
        super(LogWindow, self).__init__(parent)
        self.setupUi(self)


class ConnectWindow(QtGui.QWidget, uiConnectWindow.Ui_winConnect):

    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setupUi(self)