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
		self.actionOpen_File.triggered.connect(self.openImg_click)

	def openImg_click(self):
		self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg)")
		if self.path[0] == '': return QMessageBox.warning(self, "WARNING", "The input image is empty")
		self.inImg = cv2.imread(self.path[0])
		outImg = self.MatToQImage(self.inImg)
		self.imgShowLb.setPixmap(outImg.scaled(self.imgShowLb.width(),self.imgShowLb.height(),Qt.KeepAspectRatio))

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
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w.show()
    sys.exit(app.exec_())