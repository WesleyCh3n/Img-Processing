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
		img = cv2.imread(self.path[0])
		print(img.dtype.name)
		b,g,r = cv2.split(img)
		print(b.dtype.name)
		# b = np.split(img, 3, axis=2)[0].squeeze(axis=2).astype(np.uint8)
		# g = np.split(img, 3, axis=2)[1].squeeze(axis=2).astype(np.uint8)
		# r = np.split(img, 3, axis=2)[2].squeeze(axis=2).astype(np.uint8)
		new_img = cv2.merge([r,g,b])
		# new_img = np.stack((\
		# 	np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8),\
		# 	np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8),\
		# 	r), axis=2)
		print(new_img)
		outImg = self.MatToQImage(new_img)		
		self.label.setPixmap(outImg.scaled(self.label.width(),self.label.height(),Qt.KeepAspectRatio))

	def MatToQImage(self, mat, swapped=True, qpixmap=True):
		height, width = mat.shape[:2]
		dim = 1 if mat.ndim == 2 else mat.shape[2]
		bytesPerLine = dim * width
		qimage = QtGui.QImage(mat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
		if swapped:
			if qpixmap:
				qimage = qimage.rgbSwapped()
				final = QPixmap.fromImage(qimage)
				return final
			else:	
				qimage = qimage.rgbSwapped()
				return qimage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())