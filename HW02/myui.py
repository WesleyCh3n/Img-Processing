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
        MainWindow.resize(844, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 821, 91))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 801, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grayaBn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.grayaBn.setObjectName("grayaBn")
        self.horizontalLayout.addWidget(self.grayaBn)
        self.graybBn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.graybBn.setObjectName("graybBn")
        self.horizontalLayout.addWidget(self.graybBn)
        self.subBn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.subBn.setObjectName("subBn")
        self.horizontalLayout.addWidget(self.subBn)
        self.eqBn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.eqBn.setObjectName("eqBn")
        self.horizontalLayout.addWidget(self.eqBn)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lsB = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lsB.setAlignment(QtCore.Qt.AlignCenter)
        self.lsB.setObjectName("lsB")
        self.horizontalLayout.addWidget(self.lsB)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.ssB = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.ssB.setAlignment(QtCore.Qt.AlignCenter)
        self.ssB.setObjectName("ssB")
        self.horizontalLayout.addWidget(self.ssB)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 801, 44))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.bSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bSlider.setObjectName("bSlider")
        self.horizontalLayout_2.addWidget(self.bSlider)
        self.briSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.briSlider.setOrientation(QtCore.Qt.Horizontal)
        self.briSlider.setObjectName("briSlider")
        self.horizontalLayout_2.addWidget(self.briSlider)
        self.conSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.conSlider.setOrientation(QtCore.Qt.Horizontal)
        self.conSlider.setObjectName("conSlider")
        self.horizontalLayout_2.addWidget(self.conSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 110, 389, 369))
        self.layoutWidget.setObjectName("layoutWidget")
        self.grid1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.grid1.setContentsMargins(0, 0, 0, 0)
        self.grid1.setObjectName("grid1")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 401, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imgLb = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imgLb.setGeometry(QtCore.QRect(0, 0, 391, 351))
        self.imgLb.setText("")
        self.imgLb.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLb.setObjectName("imgLb")
        self.scrollArea.setWidget(self.imgLb)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionReset)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grayaBn.setText(_translate("MainWindow", "A. Grayscale"))
        self.graybBn.setText(_translate("MainWindow", "B. Grayscale"))
        self.subBn.setText(_translate("MainWindow", "Substraction"))
        self.eqBn.setText(_translate("MainWindow", "Equalization"))
        self.label_4.setText(_translate("MainWindow", "Enlarge"))
        self.label_5.setText(_translate("MainWindow", "Shrink"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "Binary Threshold"))
        self.label_2.setText(_translate("MainWindow", "Brightness"))
        self.label_3.setText(_translate("MainWindow", "Contrast"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
