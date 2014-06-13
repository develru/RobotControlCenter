# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\toolWindow.ui'
#
# Created: Fri Jun 13 20:25:13 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_toolWin(object):
    def setupUi(self, toolWin):
        toolWin.setObjectName(_fromUtf8("toolWin"))
        toolWin.resize(255, 300)
        self.verticalLayout = QtGui.QVBoxLayout(toolWin)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.connectBtn = QtGui.QPushButton(toolWin)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.verticalLayout.addWidget(self.connectBtn)
        self.activateCamBtn = QtGui.QPushButton(toolWin)
        self.activateCamBtn.setEnabled(False)
        self.activateCamBtn.setObjectName(_fromUtf8("activateCamBtn"))
        self.verticalLayout.addWidget(self.activateCamBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(toolWin)
        QtCore.QMetaObject.connectSlotsByName(toolWin)

    def retranslateUi(self, toolWin):
        toolWin.setWindowTitle(_translate("toolWin", "Tools", None))
        self.connectBtn.setText(_translate("toolWin", "Connect", None))
        self.activateCamBtn.setText(_translate("toolWin", "Activate the camera", None))

