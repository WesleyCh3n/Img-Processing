import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
	path = False

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.actionOpen_File.triggered.connect(self.openImg_click)

	def openImg_click(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		print(self.path)
		img = cv2.imread(self.path[0])
		inImg = self.MatToQImage(img)
		outImg = QPixmap.fromImage(inImg)
		self.label.setPixmap(outImg.scaled(self.label.width(),self.label.height(),Qt.KeepAspectRatio))
		# cv2.imshow("image", img)
		# cv2.waitKey(0) 
		# cv2.destroyAllWindows()
	def MatToQImage(self, mat, swapped=True):
		print(type(mat))
		height, width = mat.shape[:2]
		dim = 1 if mat.ndim == 2 else mat.shape[2]
		bytesPerLine = dim * width
		qimage = QtGui.QImage(mat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
		if swapped:
			qimage = qimage.rgbSwapped()
			return qimage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())