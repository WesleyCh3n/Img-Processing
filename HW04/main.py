import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle
import cv2
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
		self.imgShowLb.setPixmap(outImg1.scaled(self.imgShowLb.width(),self.imgShowLb.height(),Qt.KeepAspectRatio))

	def idLowBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		crow, ccol = int(rows/2) , int(cols/2)
		mask = np.zeros((rows, cols, 2), np.uint8)
		mask[crow-30:crow+30, ccol-30:ccol+30] = 1
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		back[back <= 0] = 0
		back[back >= 255] = 255
		outImg = self.MatToQImage(back)
		self.imgShowLb.setPixmap(outImg.scaled(self.imgShowLb.width(),self.imgShowLb.height(),Qt.KeepAspectRatio))

	def bLowBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		rows, cols = inImg.shape
		crow, ccol = int(rows/2) , int(cols/2)
		mask = np.zeros((rows, cols), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - crow)/2)**2+((v - ccol)/2)**2)**(1/2)
				mask[u, v] = 1.0/((1+(radius/40))**4)
		mask = np.repeat(mask[:, :, np.newaxis], 2, axis=2)
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		back = cv2.idft(f_ishift,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.imgShowLb.setPixmap(outImg.scaled(self.imgShowLb.width(),self.imgShowLb.height(),Qt.KeepAspectRatio))

	# def 

	def MatToQImage(self, mat, swapped=True, qpixmap=True):
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