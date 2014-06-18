from pyUi import uiLogWindow, uiMainWindow, uiToolWindow, uiConnectWindow
from PyQt4 import QtGui
from connection import ControlConnection

__author__ = 'develru'


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect_win = ConnectWindow()
        self._connect_subwindow = self.mdiArea.addSubWindow(self.connect_win)
        self._connect_subwindow.hide()

        self._connection = ControlConnection()

        self.connectBtn.clicked.connect(self.connect_to_robot)

        # Connect window
        self.connect_win.cancelBtn.clicked.connect(self.cancel_connect_window)
        self.connect_win.connectBtn.clicked.connect(self.start_connection)

    def connect_to_robot(self):
        self._connect_subwindow.show()
        self.tBrLog.append('Connect pressed')

    def cancel_connect_window(self):
        self._connect_subwindow.close()

    def start_connection(self):
        self._connection.connect_to_host('localhost', 9999)


class LogWindow(QtGui.QWidget, uiLogWindow.Ui_logWin):

    def __init__(self, parent=None):
        super(LogWindow, self).__init__(parent)
        self.setupUi(self)


class ConnectWindow(QtGui.QWidget, uiConnectWindow.Ui_winConnect):

    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setupUi(self)