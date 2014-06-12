__author__ = 'develru'

from PySide import QtGui, QtCore
import uiMainWindow
import uiToolWindow


class ControlWindow(QtGui.QMainWindow, uiMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ControlWindow, self).__init__(parent)
        self.setupUi(self)
        tool_win = ToolWindow()
        self.mdiArea.addSubWindow(tool_win)


class ToolWindow(QtGui.QWidget, uiToolWindow.Ui_toolWin):
    def __init__(self, parent=None):
        super(ToolWindow, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        event.ignore()
        QtGui.QMessageBox.warning(self, 'Warning', 'The tool window is not to close!')