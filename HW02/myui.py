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
        MainWindow.resize(903, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 871, 81))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graybBn = QtWidgets.QPushButton(self.tab)
        self.graybBn.setGeometry(QtCore.QRect(130, 10, 101, 25))
        self.graybBn.setObjectName("graybBn")
        self.grayaBn = QtWidgets.QPushButton(self.tab)
        self.grayaBn.setGeometry(QtCore.QRect(10, 10, 101, 25))
        self.grayaBn.setObjectName("grayaBn")
        self.subBn = QtWidgets.QPushButton(self.tab)
        self.subBn.setGeometry(QtCore.QRect(250, 10, 101, 25))
        self.subBn.setObjectName("subBn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bSlider = QtWidgets.QSlider(self.tab_2)
        self.bSlider.setGeometry(QtCore.QRect(20, 30, 160, 16))
        self.bSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bSlider.setObjectName("bSlider")
        self.briSlider = QtWidgets.QSlider(self.tab_2)
        self.briSlider.setGeometry(QtCore.QRect(200, 30, 160, 16))
        self.briSlider.setOrientation(QtCore.Qt.Horizontal)
        self.briSlider.setObjectName("briSlider")
        self.conSlider = QtWidgets.QSlider(self.tab_2)
        self.conSlider.setGeometry(QtCore.QRect(380, 30, 160, 16))
        self.conSlider.setOrientation(QtCore.Qt.Horizontal)
        self.conSlider.setObjectName("conSlider")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 121, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 121, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.reSlider = QtWidgets.QSlider(self.tab_2)
        self.reSlider.setGeometry(QtCore.QRect(560, 30, 160, 16))
        self.reSlider.setOrientation(QtCore.Qt.Horizontal)
        self.reSlider.setObjectName("reSlider")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(580, 10, 121, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 110, 389, 369))
        self.layoutWidget.setObjectName("layoutWidget")
        self.grid1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.grid1.setContentsMargins(0, 0, 0, 0)
        self.grid1.setObjectName("grid1")
        self.imgLb = QtWidgets.QLabel(self.centralwidget)
        self.imgLb.setGeometry(QtCore.QRect(30, 110, 371, 371))
        self.imgLb.setText("")
        self.imgLb.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLb.setObjectName("imgLb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.graybBn.setText(_translate("MainWindow", "B. Grayscale"))
        self.grayaBn.setText(_translate("MainWindow", "A. Grayscale"))
        self.subBn.setText(_translate("MainWindow", "Substraction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "Binary Threshold"))
        self.label_2.setText(_translate("MainWindow", "Brightness"))
        self.label_3.setText(_translate("MainWindow", "Contrast"))
        self.label_4.setText(_translate("MainWindow", "Resize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
