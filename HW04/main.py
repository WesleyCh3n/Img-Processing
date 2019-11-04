import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle
import cv2
import math
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setupUi(self)
		self.path = False
		self.actionOpen_File.triggered.connect(self.openImg_clicked)
		self.dftBn.clicked.connect(self.fftBn_clicked)
		self.idLowBn.clicked.connect(self.idLowBn_clicked)
		self.bLowBn.clicked.connect(self.bLowBn_clicked)
		self.GauLowBn.clicked.connect(self.GauLowBn_clicked)
		self.idHighBn.clicked.connect(self.idHighBn_clicked)
		self.bHighBn.clicked.connect(self.bHighBn_clicked)
		self.GauHighBn.clicked.connect(self.GauHighBn_clicked)
		self.homoBn.clicked.connect(self.homoBn_clicked)
		# inImg = cv2.imread('C1HW04_IMG01_2019.jpg', 0)

	def openImg_clicked(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		if self.path[0] == '': return QMessageBox.warning(self, "WARNING", "The input image is empty")
		self.inImg = cv2.imread(self.path[0])
		outImg = self.MatToQImage(self.inImg)
		self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio))

	def fftBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		magnitude_spectrum, ang1 = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1], angleInDegrees=True) 
		magnitude_spectrum = 20*np.log(magnitude_spectrum)
		cv2.normalize(magnitude_spectrum, magnitude_spectrum,  0, 255,cv2.NORM_MINMAX)
		ang = cv2.phase(dft[:,:,0], dft[:,:,0])
		# fMin = np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]).min())
		# fMax = np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]).max())
		# fFinal = 255*((np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))-fMin)/(fMax-fMin))
		# cv2.normalize(fFinal, fFinal,  0, 255, cv2.NORM_MINMAX)
		cv2.normalize(ang, ang, 0, 255,cv2.NORM_MINMAX)
		print(ang.max())
		back = cv2.idft(dft,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg1 = self.MatToQImage(ang)
		outImg = self.MatToQImage(magnitude_spectrum)
		self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio))
		self.outputLb.setPixmap(outImg1.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def idLowBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.uint8)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				if radius <= 10:
					mask[u, v, 0] = 1
					mask[u, v, 1] = 1
				else:
					mask[u, v, 0] = 0
					mask[u, v, 1] = 0
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def bLowBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0/((1+(radius/40))**4)
				mask[u, v, 1] = 1.0/((1+(radius/40))**4)
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def GauLowBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = math.exp((-1*radius**2)/(2*(1**2)))
				mask[u, v, 1] = math.exp((-1*radius**2)/(2*(1**2)))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def idHighBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.uint8)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				if radius > 10:
					mask[u, v, 0] = 1
					mask[u, v, 1] = 1
				else:
					mask[u, v, 0] = 0
					mask[u, v, 1] = 0
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def bHighBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0 - (1.0/((1.0+(radius/40.0))**2))
				mask[u, v, 1] = 1.0 - (1.0/((1.0+(radius/40.0))**2))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def GauHighBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0 - math.exp((-1*radius**2)/(2*(1**2)))
				mask[u, v, 1] = 1.0 - math.exp((-1*radius**2)/(2*(1**2)))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def homoBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		gammaH = 3.0
		gammaL = 0.4
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = (gammaH - gammaL)*(1.0 - math.exp(-2*(radius**2)/(20.0)**2))+gammaL
				mask[u, v, 1] = (gammaH - gammaL)*(1.0 - math.exp(-2*(radius**2)/(20.0)**2))+gammaL
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))
		
	def MatToQImage(self, mat, swapped=True, qpixmap=True):
		mat[mat >= 255] = 255
		mat[mat <= 0] = 0
		if mat.ndim == 2:
			mat = np.repeat(mat[:, :, np.newaxis], 3, axis=2)
		if mat.dtype != np.uint8:
			mat = mat.astype(np.uint8)
		height, width, channel = mat.shape
		bytesPerLine = 3 * width
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
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w.show()
    sys.exit(app.exec_())