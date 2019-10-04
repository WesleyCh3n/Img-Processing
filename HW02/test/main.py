import sys
from myuiR import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		qpixmap = QPixmap(2000,2000)
		qpixmap.fill(Qt.white)
		self.label_2.setPixmap(qpixmap)
		self.label.setPixmap(qpixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())