# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driveWindow.ui'
#
# Created: Sun Jun 22 13:38:02 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(287, 343)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnLeft = QtGui.QPushButton(Form)
        self.btnLeft.setObjectName(_fromUtf8("btnLeft"))
        self.verticalLayout.addWidget(self.btnLeft)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnForward = QtGui.QPushButton(Form)
        self.btnForward.setAutoFillBackground(False)
        self.btnForward.setObjectName(_fromUtf8("btnForward"))
        self.verticalLayout_2.addWidget(self.btnForward)
        self.btnStop = QtGui.QPushButton(Form)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.verticalLayout_2.addWidget(self.btnStop)
        self.btnBackward = QtGui.QPushButton(Form)
        self.btnBackward.setObjectName(_fromUtf8("btnBackward"))
        self.verticalLayout_2.addWidget(self.btnBackward)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnRight = QtGui.QPushButton(Form)
        self.btnRight.setObjectName(_fromUtf8("btnRight"))
        self.verticalLayout_3.addWidget(self.btnRight)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnLeft.setText(_translate("Form", "Left", None))
        self.btnForward.setText(_translate("Form", "Forward", None))
        self.btnStop.setText(_translate("Form", "Stop", None))
        self.btnBackward.setText(_translate("Form", "Backward", None))
        self.btnRight.setText(_translate("Form", "Right", None))

