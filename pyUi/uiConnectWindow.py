# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectWindow.ui'
#
# Created: Fri Jun 20 09:25:31 2014
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

class Ui_winConnect(object):
    def setupUi(self, winConnect):
        winConnect.setObjectName(_fromUtf8("winConnect"))
        winConnect.resize(400, 158)
        self.verticalLayout = QtGui.QVBoxLayout(winConnect)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(winConnect)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lEHost = QtGui.QLineEdit(winConnect)
        self.lEHost.setObjectName(_fromUtf8("lEHost"))
        self.verticalLayout.addWidget(self.lEHost)
        self.label_2 = QtGui.QLabel(winConnect)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lEPort = QtGui.QLineEdit(winConnect)
        self.lEPort.setObjectName(_fromUtf8("lEPort"))
        self.verticalLayout.addWidget(self.lEPort)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.connectBtn = QtGui.QPushButton(winConnect)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.horizontalLayout.addWidget(self.connectBtn)
        self.cancelBtn = QtGui.QPushButton(winConnect)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(winConnect)
        QtCore.QMetaObject.connectSlotsByName(winConnect)

    def retranslateUi(self, winConnect):
        winConnect.setWindowTitle(_translate("winConnect", "Connect to robot", None))
        self.label.setText(_translate("winConnect", "Host", None))
        self.lEHost.setText(_translate("winConnect", "localhost", None))
        self.label_2.setText(_translate("winConnect", "Port", None))
        self.lEPort.setInputMask(_translate("winConnect", "D000; ", None))
        self.lEPort.setText(_translate("winConnect", "9999", None))
        self.connectBtn.setText(_translate("winConnect", "Connect", None))
        self.cancelBtn.setText(_translate("winConnect", "Cancel", None))

