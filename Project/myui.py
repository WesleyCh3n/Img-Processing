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
        MainWindow.resize(1189, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 581, 601))
        self.groupBox.setObjectName("groupBox")
        self.inputLb = QtWidgets.QLabel(self.groupBox)
        self.inputLb.setGeometry(QtCore.QRect(10, 30, 561, 561))
        self.inputLb.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLb.setObjectName("inputLb")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 50, 581, 601))
        self.groupBox_2.setObjectName("groupBox_2")
        self.outputLb = QtWidgets.QLabel(self.groupBox_2)
        self.outputLb.setGeometry(QtCore.QRect(10, 30, 561, 561))
        self.outputLb.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLb.setObjectName("outputLb")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 361, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.drawPb = QtWidgets.QPushButton(self.layoutWidget)
        self.drawPb.setObjectName("drawPb")
        self.gridLayout.addWidget(self.drawPb, 0, 0, 1, 1)
        self.wrapPb = QtWidgets.QPushButton(self.layoutWidget)
        self.wrapPb.setObjectName("wrapPb")
        self.gridLayout.addWidget(self.wrapPb, 0, 1, 1, 1)
        self.pdfPb = QtWidgets.QPushButton(self.layoutWidget)
        self.pdfPb.setObjectName("pdfPb")
        self.gridLayout.addWidget(self.pdfPb, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 650, 1171, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 1151, 91))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1189, 22))
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
        self.inputLb.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output"))
        self.outputLb.setText(_translate("MainWindow", "TextLabel"))
        self.drawPb.setText(_translate("MainWindow", "Draw Point"))
        self.wrapPb.setText(_translate("MainWindow", "Wrap Image"))
        self.pdfPb.setText(_translate("MainWindow", "PDF"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Log"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
