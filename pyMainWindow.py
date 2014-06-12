# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created: Thu Jun 12 20:21:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 614)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.toolWindow = QtGui.QWidget()
        self.toolWindow.setObjectName("toolWindow")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.toolWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.connectBtn = QtGui.QPushButton(self.toolWindow)
        self.connectBtn.setObjectName("connectBtn")
        self.verticalLayout_2.addWidget(self.connectBtn)
        self.cameraBtn = QtGui.QPushButton(self.toolWindow)
        self.cameraBtn.setObjectName("cameraBtn")
        self.verticalLayout_2.addWidget(self.cameraBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        self.menuControl = QtGui.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuControl.addAction(self.actionConnect)
        self.menuControl.addSeparator()
        self.menuControl.addAction(self.actionExit)
        self.menubar.addAction(self.menuControl.menuAction())
        self.toolBar.addAction(self.actionConnect)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL("triggered(QAction*)"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Control Center", None, QtGui.QApplication.UnicodeUTF8))
        self.toolWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.connectBtn.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraBtn.setText(QtGui.QApplication.translate("MainWindow", "Activate Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.menuControl.setTitle(QtGui.QApplication.translate("MainWindow", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

