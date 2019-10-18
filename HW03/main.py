import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
	inImg = False

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)

		self.inImg = cv2.imread('/Users/YoChen/Documents/GitHub/Img-Processing/HW03/bird.jpg')
		outImg = self.MatToQImage(self.inImg)
		self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

		self.actionOpen_File.triggered.connect(self.openImg_click)
		self.sfLb.clicked.connect(self.sfLb_click)

	def openImg_click(self):
		# path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		# self.inImg = cv2.imread(path[0])
		outImg = self.MatToQImage(self.inImg)
		self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

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

	def sfLb_click(self):
		def padded(mask, ch):
			ch_add = [[0,0,0],[0,0,0]]
			z_c = np.zeros((ch[0].shape[0], int((mask-1)/2)), dtype=np.uint8)
			z_r = np.zeros((int((mask-1)/2), (ch[0].shape[1]+int(mask-1))), dtype=np.uint8)
			for i in range(3):
				ch_add[0][i] = np.c_[z_c, ch[i], z_c]
				ch_add[1][i] = np.r_[z_r, ch_add[0][i], z_r]
			return ch_add[1]

		b, g, r = cv2.split(self.inImg)
		mask_s = 5
		mask = np.ones((mask_s, mask_s), dtype=np.uint8)
		a = padded(mask_s, cv2.split(self.inImg))
		print(a)
		# for y in range(self.inImg.shape[0]):
		# 	for x in range(self.inImg,shape[1]):

		return 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())