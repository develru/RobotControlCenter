# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\toolWindow.ui'
#
# Created: Fri Jun 13 20:06:40 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_toolWin(object):
    def setupUi(self, toolWin):
        toolWin.setObjectName("toolWin")
        toolWin.resize(255, 300)
        self.verticalLayout = QtGui.QVBoxLayout(toolWin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectBtn = QtGui.QPushButton(toolWin)
        self.connectBtn.setObjectName("connectBtn")
        self.verticalLayout.addWidget(self.connectBtn)
        self.activateCamBtn = QtGui.QPushButton(toolWin)
        self.activateCamBtn.setEnabled(False)
        self.activateCamBtn.setObjectName("activateCamBtn")
        self.verticalLayout.addWidget(self.activateCamBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(toolWin)
        QtCore.QMetaObject.connectSlotsByName(toolWin)

    def retranslateUi(self, toolWin):
        toolWin.setWindowTitle(QtGui.QApplication.translate("toolWin", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.connectBtn.setText(QtGui.QApplication.translate("toolWin", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.activateCamBtn.setText(QtGui.QApplication.translate("toolWin", "Activate the camera", None, QtGui.QApplication.UnicodeUTF8))

