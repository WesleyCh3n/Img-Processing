import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np
import time

class MainWindow(QMainWindow, Ui_MainWindow):
	path = False
	inImg = False
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)

		self.proB.setValue(0)
		self.sizesB.setRange(1,11)
		self.sizesB.setSingleStep(2)

		self.threadClass = thread()
		self.threadClass.val.connect(self.updatePb)
		self.threadClass.output.connect(self.show_img)
		self.actionOpen_File.triggered.connect(self.openImg_click)
		self.sfLb.clicked.connect(self.sfLb_click)

	def openImg_click(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		self.inImg = cv2.imread(self.path[0])
		outImg = self.MatToQImage(self.inImg)
		self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

	def sfLb_click(self):
		self.threadClass.inMat = self.inImg
		self.threadClass.sliderValue = self.sizesB.value()
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
	output = pyqtSignal(np.ndarray, str)
	val = pyqtSignal(int)
	sliderValue = 1
	inMat = False
	def __init__(self, parent = None):
		super(thread, self).__init__(parent)

	def run(self):
		mask = np.ones((self.sliderValue, self.sliderValue), dtype=np.uint8)
		def padded(mask, ch):
			ch_add = [[0,0,0],[0,0,0]]
			z_c = np.zeros((ch[0].shape[0], int((mask-1)/2)), dtype=np.uint8)
			z_r = np.zeros((int((mask-1)/2), (ch[0].shape[1]+int(mask-1))), dtype=np.uint8)
			for i in range(3):
				ch_add[0][i] = np.c_[z_c, ch[i], z_c]
				ch_add[1][i] = np.r_[z_r, ch_add[0][i], z_r]
			return ch_add[1]

		ch_pd = padded(self.sliderValue, cv2.split(self.inMat))
		ch_ori = cv2.split(self.inMat)
		print(mask)
		print(mask.sum())
		for i in range(3):
			for y in range(cv2.split(self.inMat)[i].shape[0]):
					for x in range(cv2.split(self.inMat)[i].shape[1]):
						ch_ori[i][y, x] = (mask*ch_pd[i][y:y+mask.shape[0], x:x+mask.shape[0]]).sum()*(1/mask.sum())
					proInt = int(101*(i*cv2.split(self.inMat)[i].shape[0]+y)/(3*cv2.split(self.inMat)[i].shape[0]))
					self.val.emit(proInt)

		b,g,r=ch_ori
		outImg = cv2.merge([b,g,r])

		self.output.emit(outImg, "Finish.\n==========================")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(235,219,178)")
    w.show()
    sys.exit(app.exec_())