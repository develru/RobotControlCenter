# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sun Jun 22 13:37:05 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(831, 614)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.connectBtn = QtGui.QPushButton(self.groupBox)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.verticalLayout_3.addWidget(self.connectBtn)
        self.cameraBtn = QtGui.QPushButton(self.groupBox)
        self.cameraBtn.setEnabled(False)
        self.cameraBtn.setObjectName(_fromUtf8("cameraBtn"))
        self.verticalLayout_3.addWidget(self.cameraBtn)
        self.btnManualDrive = QtGui.QPushButton(self.groupBox)
        self.btnManualDrive.setEnabled(False)
        self.btnManualDrive.setObjectName(_fromUtf8("btnManualDrive"))
        self.verticalLayout_3.addWidget(self.btnManualDrive)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.horizontalLayout.addWidget(self.mdiArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tBrLog = QtGui.QTextBrowser(self.centralwidget)
        self.tBrLog.setObjectName(_fromUtf8("tBrLog"))
        self.verticalLayout.addWidget(self.tBrLog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuControl = QtGui.QMenu(self.menubar)
        self.menuControl.setObjectName(_fromUtf8("menuControl"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuControl.addAction(self.actionConnect)
        self.menuControl.addSeparator()
        self.menuControl.addAction(self.actionExit)
        self.menubar.addAction(self.menuControl.menuAction())
        self.toolBar.addAction(self.actionConnect)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control Center", None))
        self.groupBox.setTitle(_translate("MainWindow", "Tools", None))
        self.connectBtn.setText(_translate("MainWindow", "Connect", None))
        self.cameraBtn.setText(_translate("MainWindow", "Activate the Camera", None))
        self.btnManualDrive.setText(_translate("MainWindow", "Manual Drive Mode", None))
        self.menuControl.setTitle(_translate("MainWindow", "Control", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

