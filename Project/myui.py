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
        MainWindow.resize(779, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drawPb = QtWidgets.QPushButton(self.centralwidget)
        self.drawPb.setGeometry(QtCore.QRect(30, 20, 91, 24))
        self.drawPb.setObjectName("drawPb")
        self.inputLb = QtWidgets.QLabel(self.centralwidget)
        self.inputLb.setGeometry(QtCore.QRect(30, 60, 351, 401))
        self.inputLb.setObjectName("inputLb")
        self.wrapPb = QtWidgets.QPushButton(self.centralwidget)
        self.wrapPb.setGeometry(QtCore.QRect(140, 20, 91, 24))
        self.wrapPb.setObjectName("wrapPb")
        self.outputLb = QtWidgets.QLabel(self.centralwidget)
        self.outputLb.setGeometry(QtCore.QRect(400, 60, 351, 401))
        self.outputLb.setObjectName("outputLb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.menuFile.addAction(self.actionOpen_Image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.drawPb.setText(_translate("MainWindow", "Draw Point"))
        self.inputLb.setText(_translate("MainWindow", "TextLabel"))
        self.wrapPb.setText(_translate("MainWindow", "Wrap Image"))
        self.outputLb.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
