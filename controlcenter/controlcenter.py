from pyUi import uiMainWindow, uiConnectWindow, uiDriveWindow
from PyQt4 import QtGui, QtNetwork
from connection import ControlConnection

__author__ = 'develru'


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)

        # Members
        self._TCP_socket = QtNetwork.QTcpSocket()
        self.connect_win = ConnectWindow()
        self.drive_win = DriveWindow()
        self._connection = ControlConnection()

        # Subwindows
        self._connect_subwindow = self.mdiArea.addSubWindow(self.connect_win)
        self._connect_subwindow.hide()
        self._drive_subwindow = self.mdiArea.addSubWindow(self.drive_win)
        self._drive_subwindow.hide()

        # Signals
        self.connectBtn.clicked.connect(self.connect_to_robot)
        self.btnManualDrive.clicked.connect(self.start_manuel_drive)

        # Connect window signals
        self.connect_win.cancelBtn.clicked.connect(self.cancel_connect_window)
        self.connect_win.connectBtn.clicked.connect(self.start_connection)

    def connect_to_robot(self):
        self._connect_subwindow.show()

    def cancel_connect_window(self):
        self._connect_subwindow.close()

    def start_manuel_drive(self):
        self._drive_subwindow.show()

    def start_connection(self):
        host = self.connect_win.lEHost.text()
        port = int(self.connect_win.lEPort.text())
        self.tBrLog.append('Connect to host: {0} on port: {1}'.format(host, port))
        self._TCP_socket.connectToHost(host, port)
        self._TCP_socket.waitForConnected(-1)
        self._TCP_socket.waitForReadyRead(-1)
        message = self._TCP_socket.readData(10)
        self.tBrLog.append('Message: {0}'.format(message))

        if 'Connected' in message:
            self._connect_subwindow.close()
            self.btnManualDrive.setEnabled(True)
        else:
            QtGui.QMessageBox.critical(self, 'Connection error!', 'The connection failed!')


class ConnectWindow(QtGui.QWidget, uiConnectWindow.Ui_winConnect):

    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setupUi(self)


class DriveWindow(QtGui.QWidget, uiDriveWindow.Ui_Form):

    def __init__(self, parent=None):
        super(DriveWindow, self).__init__(parent)
        self.setupUi(self)