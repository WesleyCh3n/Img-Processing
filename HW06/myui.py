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
        MainWindow.resize(967, 747)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 461, 481))
        self.groupBox.setObjectName("groupBox")
        self.inputLb = QtWidgets.QLabel(self.groupBox)
        self.inputLb.setGeometry(QtCore.QRect(10, 30, 441, 441))
        self.inputLb.setText("")
        self.inputLb.setObjectName("inputLb")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 180, 461, 481))
        self.groupBox_2.setObjectName("groupBox_2")
        self.outputLb = QtWidgets.QLabel(self.groupBox_2)
        self.outputLb.setGeometry(QtCore.QRect(10, 30, 441, 441))
        self.outputLb.setText("")
        self.outputLb.setObjectName("outputLb")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 241, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.trapBn = QtWidgets.QPushButton(self.layoutWidget)
        self.trapBn.setObjectName("trapBn")
        self.gridLayout.addWidget(self.trapBn, 0, 0, 1, 1)
        self.wavyBn = QtWidgets.QPushButton(self.layoutWidget)
        self.wavyBn.setObjectName("wavyBn")
        self.gridLayout.addWidget(self.wavyBn, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.sB = QtWidgets.QSpinBox(self.layoutWidget)
        self.sB.setObjectName("sB")
        self.gridLayout.addWidget(self.sB, 2, 1, 1, 1)
        self.cirBn = QtWidgets.QPushButton(self.layoutWidget)
        self.cirBn.setObjectName("cirBn")
        self.gridLayout.addWidget(self.cirBn, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.dsB = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.dsB.setObjectName("dsB")
        self.gridLayout.addWidget(self.dsB, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 10, 241, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(530, 10, 421, 171))
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 221, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.htsB = QtWidgets.QSpinBox(self.layoutWidget1)
        self.htsB.setObjectName("htsB")
        self.gridLayout_2.addWidget(self.htsB, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.hmsB = QtWidgets.QSpinBox(self.layoutWidget1)
        self.hmsB.setObjectName("hmsB")
        self.gridLayout_2.addWidget(self.hmsB, 1, 1, 1, 1)
        self.houBn = QtWidgets.QPushButton(self.layoutWidget1)
        self.houBn.setObjectName("houBn")
        self.gridLayout_2.addWidget(self.houBn, 2, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(240, 30, 171, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 680, 941, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.menuFile.addAction(self.actionOpen_Image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Geometric Transformation"))
        self.trapBn.setText(_translate("MainWindow", "Trapezoid"))
        self.wavyBn.setText(_translate("MainWindow", "Wavy"))
        self.label.setText(_translate("MainWindow", "Amplitude"))
        self.cirBn.setText(_translate("MainWindow", "Circular"))
        self.label_2.setText(_translate("MainWindow", "Frequency"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Wavelet Transformation"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Hough Transformation"))
        self.label_3.setText(_translate("MainWindow", "Threshold"))
        self.label_4.setText(_translate("MainWindow", "MinLineLength"))
        self.houBn.setText(_translate("MainWindow", "Find Line"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
