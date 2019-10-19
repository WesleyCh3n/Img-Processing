import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np
import time

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.threadClass = thread()
		self.threadClass.test.connect(self.updatePb)
		self.pB.clicked.connect(self.pB_click)
		

	def pB_click(self):
		self.threadClass.path = "Hi"
		self.threadClass.start()

	def updatePb(self, val):
		self.proB.setValue(val)

class thread(QThread):
	test = pyqtSignal(int)
	path = False
	def __init__(self, parent = None):
		super(thread, self).__init__(parent)

	def run(self):
		print(self.path)
		for i in range(100):
			self.test.emit(i)
			time.sleep(0.5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())