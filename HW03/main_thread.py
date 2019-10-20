import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle
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
		self.threadClass.msg.connect(self.status)
		self.threadClass.output.connect(self.show_img)

		self.threadClass_2 = thread_2()
		self.threadClass_2.output.connect(self.show_img)

		self.tableWidget.setColumnCount(5)
		self.tableWidget.setRowCount(5)
		# self.model = QStandardItemModel(5,5,self)
		# self.tableWidget.setModel(model)
		# for row in range(5):
		# 	for col in range(10):
		# 		item = QtGui.QStandardItem((row, col))
		# 		self.model.setItem(row, col, item)


		self.actionOpen_File.triggered.connect(self.openImg_click)
		self.sfPb.clicked.connect(self.sfPb_click)
		self.edgePb.clicked.connect(self.edgePb_click)
		self.gussPb.clicked.connect(self.gussPb_click)
		self.midPb.clicked.connect(self.midPb_click)
		self.minPb.clicked.connect(self.minPb_click)
		self.maxPb.clicked.connect(self.maxPb_click)

	def openImg_click(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		self.inImg = cv2.imread(self.path[0])
		self.textB.append("Open image complete")
		outImg = self.MatToQImage(self.inImg)
		self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

	def sfPb_click(self):
		self.threadClass.inMat = self.inImg
		self.threadClass.sliderValue = self.sizesB.value()
		self.textB.append("Correlation Start...")
		self.threadClass.start()

	def edgePb_click(self):
		print(type(self.inImg))
		self.threadClass_2.inMat = self.inImg
		self.threadClass_2.start()

	def gussPb_click(self):
		inImg = cv2.GaussianBlur(self.inImg, (5,5), 0)
		outImg = self.MatToQImage(inImg)
		self.imgLb_out.setPixmap(outImg.scaled(self.imgLb_out.width(),self.imgLb_out.height(),Qt.KeepAspectRatio))

	def midPb_click(self):
		inImg = cv2.medianBlur(self.inImg, 9)
		outImg = self.MatToQImage(inImg)
		self.imgLb_out.setPixmap(outImg.scaled(self.imgLb_out.width(),self.imgLb_out.height(),Qt.KeepAspectRatio))

	def minPb_click(self):
		kernel = np.ones((7,7),np.uint8)
		inImg = cv2.erode(self.inImg, kernel)
		outImg = self.MatToQImage(inImg)
		self.imgLb_out.setPixmap(outImg.scaled(self.imgLb_out.width(),self.imgLb_out.height(),Qt.KeepAspectRatio))

	def maxPb_click(self):
		kernel = np.ones((7,7),np.uint8)
		inImg = cv2.dilate(self.inImg, kernel)
		outImg = self.MatToQImage(inImg)
		self.imgLb_out.setPixmap(outImg.scaled(self.imgLb_out.width(),self.imgLb_out.height(),Qt.KeepAspectRatio))

	def updatePb(self, val):
		self.proB.setValue(val)

	def status(self, messege):
		self.textB.append(messege)

	def show_img(self, inImg):
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
	output = pyqtSignal(np.ndarray)
	val = pyqtSignal(int)
	msg = pyqtSignal(str)
	sliderValue = 1
	inMat = False
	def __init__(self, parent = None):
		super(thread, self).__init__(parent)

	def run(self):
		def padded(mask, ch):
			ch_add = [[0,0,0],[0,0,0]]
			z_c = np.zeros((ch[0].shape[0], int((mask-1)/2)), dtype=np.uint8)
			z_r = np.zeros((int((mask-1)/2), (ch[0].shape[1]+int(mask-1))), dtype=np.uint8)
			for i in range(3):
				ch_add[0][i] = np.c_[z_c, ch[i], z_c]
				ch_add[1][i] = np.r_[z_r, ch_add[0][i], z_r]
			return ch_add[1]

		mask = np.ones((self.sliderValue, self.sliderValue), dtype=np.uint8)
		self.msg.emit("The mask you use is\n"+str(mask))
		ch_pd = padded(self.sliderValue, cv2.split(self.inMat))
		ch_ori = cv2.split(self.inMat)
		self.msg.emit("Correlation Start...\nPlease wait for the progress...")

		for i in range(3):
			for y in range(cv2.split(self.inMat)[i].shape[0]):
					for x in range(cv2.split(self.inMat)[i].shape[1]):
						ch_ori[i][y, x] = (mask*ch_pd[i][y:y+mask.shape[0], x:x+mask.shape[0]]).sum()*(1/mask.sum())
					proInt = int(101*(i*cv2.split(self.inMat)[i].shape[0]+y)/(3*cv2.split(self.inMat)[i].shape[0]))
					self.val.emit(proInt)

		b,g,r=ch_ori
		outImg = cv2.merge([b,g,r])

		self.output.emit(outImg)
		self.msg.emit("Progress Complete!")

class thread_2(QThread):
	output = pyqtSignal(np.ndarray)
	# val = pyqtSignal(int)
	# sliderValue = 1
	inMat = False
	def __init__(self, parent = None):
		super(thread_2, self).__init__(parent)

	def run(self):
		def padded(mask, ch):
			ch_add = [0, 0] #fisrt element add_column second Final output
			z_c = np.zeros((ch[0].shape[0], int((mask-1)/2)), dtype=np.uint8)
			z_r = np.zeros((int((mask-1)/2), (ch.shape[1]+int(mask-1))), dtype=np.uint8)
			ch_add[0] = np.c_[z_c, ch, z_c]
			ch_add[1] = np.r_[z_r, ch_add[0], z_r]
			return ch_add[1]
		# Convert to grayscale loss dimension, use np.newaxis and repeat to expand to 3d dimension
		grayImg = cv2.cvtColor(self.inMat, cv2.COLOR_BGR2GRAY)
		lgMask = np.array([[0, 0, 1, 0, 0],\
						   [0, 1, 2, 1, 0],\
						   [1, 2,-16,2, 1],\
						   [0, 1, 2, 1, 0],\
						   [0, 0, 1, 0, 0],])*(-1)
		
		pdMat = padded(5, grayImg)
		afterMat = grayImg
		for y in range(self.inMat.shape[0]):
			for x in range(self.inMat.shape[1]):
				afterMat[y, x] = (lgMask*pdMat[y:y+lgMask.shape[0], x:x+lgMask.shape[0]]).sum()
		print(afterMat)
		# printcv2.threshold#(laplace, signImage, 0, 255, cv::THRESH_BINARY);
		outImg = np.repeat(afterMat[:, :, np.newaxis], 3, axis=2)
		self.output.emit(outImg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    #w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(235,219,178)")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w.show()
    sys.exit(app.exec_())