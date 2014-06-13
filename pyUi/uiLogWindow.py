# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\logWindow.ui'
#
# Created: Fri Jun 13 20:31:08 2014
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

class Ui_logWin(object):
    def setupUi(self, logWin):
        logWin.setObjectName(_fromUtf8("logWin"))
        logWin.resize(838, 176)
        self.verticalLayout = QtGui.QVBoxLayout(logWin)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tBrLog = QtGui.QTextBrowser(logWin)
        self.tBrLog.setObjectName(_fromUtf8("tBrLog"))
        self.verticalLayout.addWidget(self.tBrLog)

        self.retranslateUi(logWin)
        QtCore.QMetaObject.connectSlotsByName(logWin)

    def retranslateUi(self, logWin):
        logWin.setWindowTitle(_translate("logWin", "Status", None))

