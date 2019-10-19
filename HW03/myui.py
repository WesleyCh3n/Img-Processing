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
        MainWindow.resize(812, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 801, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.imgLb = QtWidgets.QLabel(self.tab)
        self.imgLb.setGeometry(QtCore.QRect(20, 150, 351, 361))
        self.imgLb.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLb.setObjectName("imgLb")
        self.imgLb_out = QtWidgets.QLabel(self.tab)
        self.imgLb_out.setGeometry(QtCore.QRect(400, 150, 351, 361))
        self.imgLb_out.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLb_out.setObjectName("imgLb_out")
        self.sfLb = QtWidgets.QPushButton(self.tab)
        self.sfLb.setGeometry(QtCore.QRect(260, 20, 91, 24))
        self.sfLb.setObjectName("sfLb")
        self.textE = QtWidgets.QTextEdit(self.tab)
        self.textE.setGeometry(QtCore.QRect(110, 20, 51, 24))
        self.textE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textE.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textE.setObjectName("textE")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 24, 91, 16))
        self.label.setObjectName("label")
        self.sizesB = QtWidgets.QSpinBox(self.tab)
        self.sizesB.setGeometry(QtCore.QRect(190, 20, 48, 26))
        self.sizesB.setObjectName("sizesB")
        self.proB = QtWidgets.QProgressBar(self.tab)
        self.proB.setGeometry(QtCore.QRect(20, 550, 761, 23))
        self.proB.setProperty("value", 24)
        self.proB.setObjectName("proB")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(70, 60, 271, 251))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 22))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgLb.setText(_translate("MainWindow", "TextLabel"))
        self.imgLb_out.setText(_translate("MainWindow", "TextLabel"))
        self.sfLb.setText(_translate("MainWindow", "Sptial Filter"))
        self.label.setText(_translate("MainWindow", "Coefficients :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
