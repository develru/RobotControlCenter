__author__ = 'develru'

# from PySide import QtGui
from PyQt4 import QtGui
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
        """
        Override the close event, because wo don't allow to close this window.
        :param event: The received event.
        :return: None
        """

        event.ignore()
        QtGui.QMessageBox.warning(self, 'Warning', 'The tool window is not to close!')

    def activate_camera(self):
        pass