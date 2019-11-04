# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dftBn = QtWidgets.QPushButton(self.centralwidget)
        self.dftBn.setGeometry(QtCore.QRect(40, 30, 80, 24))
        self.dftBn.setObjectName("dftBn")
        self.imgShowLb = QtWidgets.QLabel(self.centralwidget)
        self.imgShowLb.setGeometry(QtCore.QRect(390, 110, 351, 331))
        self.imgShowLb.setObjectName("imgShowLb")
        self.inputLb = QtWidgets.QLabel(self.centralwidget)
        self.inputLb.setGeometry(QtCore.QRect(10, 110, 351, 331))
        self.inputLb.setObjectName("inputLb")
        self.idftBn = QtWidgets.QPushButton(self.centralwidget)
        self.idftBn.setGeometry(QtCore.QRect(140, 30, 80, 24))
        self.idftBn.setObjectName("idftBn")
        self.idLowBn = QtWidgets.QPushButton(self.centralwidget)
        self.idLowBn.setGeometry(QtCore.QRect(240, 30, 101, 24))
        self.idLowBn.setObjectName("idLowBn")
        self.bLowBn = QtWidgets.QPushButton(self.centralwidget)
        self.bLowBn.setGeometry(QtCore.QRect(360, 30, 101, 24))
        self.bLowBn.setObjectName("bLowBn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dftBn.setText(_translate("MainWindow", "FFT"))
        self.imgShowLb.setText(_translate("MainWindow", "TextLabel"))
        self.inputLb.setText(_translate("MainWindow", "TextLabel"))
        self.idftBn.setText(_translate("MainWindow", "iDFT"))
        self.idLowBn.setText(_translate("MainWindow", "ideal filter Low"))
        self.bLowBn.setText(_translate("MainWindow", "Butterworth Low"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
