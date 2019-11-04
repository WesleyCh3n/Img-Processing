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
        MainWindow.resize(1162, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dftBn = QtWidgets.QPushButton(self.centralwidget)
        self.dftBn.setGeometry(QtCore.QRect(50, 20, 80, 24))
        self.dftBn.setObjectName("dftBn")
        self.outputLb = QtWidgets.QLabel(self.centralwidget)
        self.outputLb.setGeometry(QtCore.QRect(550, 110, 471, 441))
        self.outputLb.setObjectName("outputLb")
        self.inputLb = QtWidgets.QLabel(self.centralwidget)
        self.inputLb.setGeometry(QtCore.QRect(10, 110, 461, 441))
        self.inputLb.setObjectName("inputLb")
        self.idftBn = QtWidgets.QPushButton(self.centralwidget)
        self.idftBn.setGeometry(QtCore.QRect(50, 50, 80, 24))
        self.idftBn.setObjectName("idftBn")
        self.idLowBn = QtWidgets.QPushButton(self.centralwidget)
        self.idLowBn.setGeometry(QtCore.QRect(140, 20, 101, 24))
        self.idLowBn.setObjectName("idLowBn")
        self.bLowBn = QtWidgets.QPushButton(self.centralwidget)
        self.bLowBn.setGeometry(QtCore.QRect(250, 20, 101, 24))
        self.bLowBn.setObjectName("bLowBn")
        self.GauLowBn = QtWidgets.QPushButton(self.centralwidget)
        self.GauLowBn.setGeometry(QtCore.QRect(360, 20, 101, 24))
        self.GauLowBn.setObjectName("GauLowBn")
        self.idHighBn = QtWidgets.QPushButton(self.centralwidget)
        self.idHighBn.setGeometry(QtCore.QRect(140, 50, 101, 24))
        self.idHighBn.setObjectName("idHighBn")
        self.bHighBn = QtWidgets.QPushButton(self.centralwidget)
        self.bHighBn.setGeometry(QtCore.QRect(250, 50, 101, 24))
        self.bHighBn.setObjectName("bHighBn")
        self.GauHighBn = QtWidgets.QPushButton(self.centralwidget)
        self.GauHighBn.setGeometry(QtCore.QRect(360, 50, 101, 24))
        self.GauHighBn.setObjectName("GauHighBn")
        self.homoBn = QtWidgets.QPushButton(self.centralwidget)
        self.homoBn.setGeometry(QtCore.QRect(510, 40, 101, 24))
        self.homoBn.setObjectName("homoBn")
        self.motionBlurBn = QtWidgets.QPushButton(self.centralwidget)
        self.motionBlurBn.setGeometry(QtCore.QRect(640, 40, 101, 24))
        self.motionBlurBn.setObjectName("motionBlurBn")
        self.WeinerBn = QtWidgets.QPushButton(self.centralwidget)
        self.WeinerBn.setGeometry(QtCore.QRect(760, 40, 101, 24))
        self.WeinerBn.setObjectName("WeinerBn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 22))
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
        self.outputLb.setText(_translate("MainWindow", "TextLabel"))
        self.inputLb.setText(_translate("MainWindow", "TextLabel"))
        self.idftBn.setText(_translate("MainWindow", "iDFT"))
        self.idLowBn.setText(_translate("MainWindow", "ideal Low"))
        self.bLowBn.setText(_translate("MainWindow", "Butterworth Low"))
        self.GauLowBn.setText(_translate("MainWindow", "Gaussian Low"))
        self.idHighBn.setText(_translate("MainWindow", "ideal High"))
        self.bHighBn.setText(_translate("MainWindow", "Butterworth High"))
        self.GauHighBn.setText(_translate("MainWindow", "Gaussian High"))
        self.homoBn.setText(_translate("MainWindow", "Homomophic"))
        self.motionBlurBn.setText(_translate("MainWindow", "Motion Blur"))
        self.WeinerBn.setText(_translate("MainWindow", "Wiener Filter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
