from pyUi import uiLogWindow, uiMainWindow, uiToolWindow, uiConnectWindow
# from PySide import QtGui
from PyQt4 import QtGui

__author__ = 'develru'


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.tool_win = ToolWindow()
        self.mdiArea.addSubWindow(self.tool_win)
        self.connect_win = ConnectWindow()
        #self.mdiArea.addSubWindow(self.connect_win)
        #self.connect_win.hide()

        self.tool_win.connectBtn.clicked.connect(self.connect_to_robot)

    def connect_to_robot(self):
        self.mdiArea.addSubWindow(self.connect_win)
        self.connect_win.show()
        self.tBrLog.append('Connect pressed')


class ToolWindow(QtGui.QWidget, uiToolWindow.Ui_toolWin):
    def __init__(self, parent=None):
        super(ToolWindow, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        """
        Override the close event, because wo don't allow to close this window.
        :param event: The received event.
        :return: None
        """

        event.ignore()
        QtGui.QMessageBox.warning(self, 'Warning', 'The tool window is not to close!')

    def activate_camera(self):
        pass


class LogWindow(QtGui.QWidget, uiLogWindow.Ui_logWin):

    def __init__(self, parent=None):
        super(LogWindow, self).__init__(parent)
        self.setupUi(self)

class ConnectWindow(QtGui.QWidget, uiConnectWindow.Ui_winConnect):

    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setupUi(self)