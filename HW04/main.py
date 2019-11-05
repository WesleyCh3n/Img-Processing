from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import qdarkstyle
import cv2
import math
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setupUi(self)
		self.path = False
		self.inImg = False
		self.cutOffValue = 0
		self.actionOpen_File.triggered.connect(self.openImg_clicked)
		self.dftBn.clicked.connect(self.fftBn_clicked)
		self.idftBn.clicked.connect(self.idftBn_clicked)
		self.idLowBn.clicked.connect(self.idLowBn_clicked)
		self.bLowBn.clicked.connect(self.bLowBn_clicked)
		self.GauLowBn.clicked.connect(self.GauLowBn_clicked)
		self.idHighBn.clicked.connect(self.idHighBn_clicked)
		self.bHighBn.clicked.connect(self.bHighBn_clicked)
		self.GauHighBn.clicked.connect(self.GauHighBn_clicked)
		self.homoBn.clicked.connect(self.homoBn_clicked)
		self.motionBlurBn.clicked.connect(self.motionBlurBn_clicked)
		self.WeinerBn.clicked.connect(self.WeinerBn_clicked)
		self.invBn.clicked.connect(self.invBn_clicked)

		self.cutoffSb.valueChanged.connect(self.cutoffSb_valueChanged)

	def openImg_clicked(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
		if self.path[0] == '': return QMessageBox.warning(self, "WARNING", "The input image is empty")
		self.inImg = cv2.imread(self.path[0], 0)
		outImg = self.MatToQImage(self.inImg)
		self.oriLb.setPixmap(outImg.scaled(self.oriLb.width(),self.oriLb.height(),Qt.KeepAspectRatio))
		self.inputLb.setPixmap(outImg.scaled(577, 479, Qt.KeepAspectRatio))

	def fftBn_clicked(self):
		inImg = cv2.imread(self.path[0], 0)
		dft = cv2.dft(np.float32(inImg), flags = cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
		ang = cv2.phase(dft[:,:,0], dft[:,:,1])
		cv2.normalize(magnitude_spectrum, magnitude_spectrum,  0, 255,cv2.NORM_MINMAX)
		cv2.normalize(ang, ang, 0, 255,cv2.NORM_MINMAX)
		# Add function
		fMin = np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]).min())
		fMax = np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]).max())
		magnitude_spectrumF = 255*((np.log(1+cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))-fMin)/(fMax-fMin))
		angF = cv2.phase(dft[:,:,0], dft[:,:,1])
		cv2.normalize(magnitude_spectrumF, magnitude_spectrumF,  0, 300,cv2.NORM_MINMAX)
		cv2.normalize(angF, angF, 0, 300,cv2.NORM_MINMAX)
		# show image		
		outImg = self.MatToQImage(magnitude_spectrum)
		outImg1 = self.MatToQImage(ang)
		outImg2 = self.MatToQImage(magnitude_spectrumF)
		outImg3 = self.MatToQImage(angF)
		self.mLb.setPixmap(outImg.scaled(self.mLb.width(),self.mLb.height(),Qt.KeepAspectRatio))
		self.pLb.setPixmap(outImg1.scaled(self.pLb.width(),self.pLb.height(),Qt.KeepAspectRatio))
		self.mfLb.setPixmap(outImg2.scaled(self.mfLb.width(),self.mfLb.height(),Qt.KeepAspectRatio))
		self.pfLb.setPixmap(outImg3.scaled(self.pfLb.width(),self.pfLb.height(),Qt.KeepAspectRatio))
		return dft, dft_shift

	def idftBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		back = cv2.idft(dft,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
		outImg = self.MatToQImage(back)
		self.idftLb.setPixmap(outImg.scaled(self.idftLb.width(),self.idftLb.height(),Qt.KeepAspectRatio))

	def idLowBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.uint8)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				if radius <= self.cutOffValue:
					mask[u, v, 0] = 1
					mask[u, v, 1] = 1
				else:
					mask[u, v, 0] = 0
					mask[u, v, 1] = 0
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def bLowBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0/((1+(radius/self.cutOffValue))**4)
				mask[u, v, 1] = 1.0/((1+(radius/self.cutOffValue))**4)
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def GauLowBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = math.exp((-1*radius**2)/(2*(self.cutOffValue**2)))
				mask[u, v, 1] = math.exp((-1*radius**2)/(2*(self.cutOffValue**2)))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def idHighBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.uint8)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				if radius > self.cutOffValue:
					mask[u, v, 0] = 1
					mask[u, v, 1] = 1
				else:
					mask[u, v, 0] = 0
					mask[u, v, 1] = 0
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def bHighBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0 - (1.0/((1.0+(radius/self.cutOffValue))**2))
				mask[u, v, 1] = 1.0 - (1.0/((1.0+(radius/self.cutOffValue))**2))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def GauHighBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = 1.0 - math.exp((-1*radius**2)/(2*(self.cutOffValue**2)))
				mask[u, v, 1] = 1.0 - math.exp((-1*radius**2)/(2*(self.cutOffValue**2)))
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def homoBn_clicked(self):
		dft, dft_shift = self.fftBn_clicked()
		rows, cols = self.inImg.shape
		mask = np.zeros((rows, cols, 2), np.float32)
		gammaH = self.HSb.value()
		gammaL = self.LSb.value()
		for u in range(rows):
			for v in range(cols):
				radius = (((u - int(rows/2))/2)**2+((v - int(cols/2))/2)**2)**(1/2)
				mask[u, v, 0] = (gammaH - gammaL)*(1.0 - math.exp(-2*(radius**2)/(self.cutOffValue)**2))+gammaL
				mask[u, v, 1] = (gammaH - gammaL)*(1.0 - math.exp(-2*(radius**2)/(self.cutOffValue)**2))+gammaL
		filterOut = dft_shift*mask
		f_ishift = np.fft.ifftshift(filterOut)
		outImg = self.MatToQImage(f_ishift, idft=True)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def motionBlurBn_clicked(self):
		T = self.TSb.value()
		inImg = cv2.imread(self.path[0], 0)
		mask = np.eye(T, dtype=float)/T
		result = cv2.filter2D(inImg, -1, mask)
		outImg = self.MatToQImage(result)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def WeinerBn_clicked(self):
		K = self.kSb.value()
		T = self.TSb.value()
		inImg = cv2.imread(self.path[0], 0)
		kernel = np.eye(T, dtype=np.float32)/T
		blurImg = cv2.filter2D(inImg, -1, kernel)
		outImg = self.MatToQImage(blurImg)
		self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio))

		dftInImg = np.fft.fft2(blurImg)
		kernel = np.fft.fft2(kernel, s = blurImg.shape)
		kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)

		dftInImg = dftInImg * kernel
		dftInImg = np.abs(np.fft.ifft2(dftInImg))
		outImg = self.MatToQImage(dftInImg)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def invBn_clicked(self):
		np.seterr(divide='ignore',invalid='ignore')
		inImg = cv2.imread(self.path[0], 0)
		kernel = np.eye(30, dtype=np.float32)/30
		blurImg = cv2.filter2D(inImg, -1, kernel)

		dftInImg = np.fft.fft2(blurImg)	
		dftKernel = np.fft.fft2(kernel, s = inImg.shape)
		
		dftInImgNorm = dftInImg/abs(dftInImg.max())
		kernelNorm = dftKernel/abs(kernel.max())

		rows, cols = inImg.shape
		result = np.copy(dftInImgNorm)
		for u in range(rows):
			for v in range(cols):
				result[u, v] = dftInImgNorm[u, v] / kernelNorm[u, v]
		resultNorm = result / abs(result.max())
		F = resultNorm * abs(dftInImg.max())
		out = np.abs(np.fft.ifft2(F))
		outImg = self.MatToQImage(out)
		self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio))

	def cutoffSb_valueChanged(self):
		self.cutOffValue = self.cutoffSb.value()

	def MatToQImage(self, mat, swapped=True, qpixmap=True, idft=False):
		if idft == True:
			mat = cv2.idft(mat,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
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