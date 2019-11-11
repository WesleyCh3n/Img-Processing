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
        MainWindow.resize(1045, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 101))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 281, 58))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RGVPb = QtWidgets.QPushButton(self.widget)
        self.RGVPb.setObjectName("RGVPb")
        self.gridLayout.addWidget(self.RGVPb, 0, 0, 1, 1)
        self.CMYPb = QtWidgets.QPushButton(self.widget)
        self.CMYPb.setObjectName("CMYPb")
        self.gridLayout.addWidget(self.CMYPb, 0, 1, 1, 1)
        self.HSIPb = QtWidgets.QPushButton(self.widget)
        self.HSIPb.setObjectName("HSIPb")
        self.gridLayout.addWidget(self.HSIPb, 0, 2, 1, 1)
        self.XYZPb = QtWidgets.QPushButton(self.widget)
        self.XYZPb.setObjectName("XYZPb")
        self.gridLayout.addWidget(self.XYZPb, 1, 0, 1, 1)
        self.LabPb = QtWidgets.QPushButton(self.widget)
        self.LabPb.setObjectName("LabPb")
        self.gridLayout.addWidget(self.LabPb, 1, 1, 1, 1)
        self.YUVPb = QtWidgets.QPushButton(self.widget)
        self.YUVPb.setObjectName("YUVPb")
        self.gridLayout.addWidget(self.YUVPb, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 500, 500))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.inputLb = QtWidgets.QLabel(self.groupBox_2)
        self.inputLb.setGeometry(QtCore.QRect(20, 30, 460, 460))
        self.inputLb.setObjectName("inputLb")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(530, 140, 500, 500))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.outputLb = QtWidgets.QLabel(self.groupBox_3)
        self.outputLb.setGeometry(QtCore.QRect(20, 30, 460, 460))
        self.outputLb.setObjectName("outputLb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_2.setObjectName("actionOpen_File_2")
        self.menuFile.addAction(self.actionOpen_File_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Color Transformation"))
        self.RGVPb.setText(_translate("MainWindow", "RGB"))
        self.CMYPb.setText(_translate("MainWindow", "CMY"))
        self.HSIPb.setText(_translate("MainWindow", "HSI"))
        self.XYZPb.setText(_translate("MainWindow", "XYZ"))
        self.LabPb.setText(_translate("MainWindow", "L*a*b"))
        self.YUVPb.setText(_translate("MainWindow", "YUV"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input"))
        self.inputLb.setText(_translate("MainWindow", "Input"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output"))
        self.outputLb.setText(_translate("MainWindow", "output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File_2.setText(_translate("MainWindow", "Open File"))
