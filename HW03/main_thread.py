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
		self.proB.setValue(0)
		self.threadClass = thread()
		self.threadClass.val.connect(self.updatePb)
		self.threadClass.test.connect(self.show_img)
		self.sfLb.clicked.connect(self.sfLb_click)


	def sfLb_click(self):
		self.threadClass.path = "/home/y0ch3n/Documents/GitHub/Img-Processing/HW03/bird.jpg"
		self.textB.append("Start")
		self.threadClass.start()

	def updatePb(self, val):
		self.proB.setValue(val)

	def show_img(self, inImg, str_):
		self.textB.append(str_)
		outImg = self.MatToQImage(inImg)
		self.imgLb_out.setPixmap(outImg.scaled(self.imgLb_out.width(),self.imgLb_out.height(),Qt.KeepAspectRatio))

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

class thread(QThread):
	test = pyqtSignal(np.ndarray, str)
	val = pyqtSignal(int)
	path = False
	def __init__(self, parent = None):
		super(thread, self).__init__(parent)

	def run(self):
		inImg = cv2.imread(self.path)
		mask_s = 5
		mask = np.ones((mask_s, mask_s), dtype=np.uint8)
		def padded(mask, ch):
			ch_add = [[0,0,0],[0,0,0]]
			z_c = np.zeros((ch[0].shape[0], int((mask-1)/2)), dtype=np.uint8)
			z_r = np.zeros((int((mask-1)/2), (ch[0].shape[1]+int(mask-1))), dtype=np.uint8)
			for i in range(3):
				ch_add[0][i] = np.c_[z_c, ch[i], z_c]
				ch_add[1][i] = np.r_[z_r, ch_add[0][i], z_r]
			return ch_add[1]

		ch_pd = padded(mask_s, cv2.split(inImg))
		ch_ori = cv2.split(inImg)
		for i in range(3):
			for y in range(cv2.split(inImg)[i].shape[0]):
					for x in range(cv2.split(inImg)[i].shape[1]):
						ch_ori[i][y, x] = (mask*ch_pd[i][y:y+mask.shape[0], x:x+mask.shape[0]]).sum()*(1/mask.sum())
					proInt = int(101*(i*cv2.split(inImg)[i].shape[0]+y)/(3*cv2.split(inImg)[i].shape[0]))
					self.val.emit(proInt)

		b,g,r=ch_ori
		outImg = cv2.merge([b,g,r])

		self.test.emit(outImg, "Finish")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())