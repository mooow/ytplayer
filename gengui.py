# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(279, 292)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditSearchString = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchString.setInputMask("")
        self.lineEditSearchString.setObjectName("lineEditSearchString")
        self.gridLayout_2.addWidget(self.lineEditSearchString, 1, 0, 1, 1)
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.gridLayout_2.addWidget(self.pushButtonSearch, 1, 1, 1, 1)
        self.listViewQueue = QtWidgets.QListView(self.centralwidget)
        self.listViewQueue.setObjectName("listViewQueue")
        self.gridLayout_2.addWidget(self.listViewQueue, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButtonSearch.clicked.connect(MainWindow.search)
        self.lineEditSearchString.returnPressed.connect(MainWindow.search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ytPlayer GUI"))
        self.lineEditSearchString.setPlaceholderText(_translate("MainWindow", "search on Youtube.com!"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))

