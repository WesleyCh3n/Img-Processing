from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import qdarkstyle

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.path = False
        self.inImg = False
        self.actionOpen_File.triggered.connect(self.actionOpen_File_triggered)
        self.RGBPb.clicked.connect(self.RGBPb_clicked)
        self.CMYPb.clicked.connect(self.CMYPb_clicked)
        self.HSIPb.clicked.connect(self.HSIPb_clicked)

    def actionOpen_File_triggered(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
        self.inImg = cv2.imread(self.path[0])
        self.showImg(self.inImg, True)

    def RGBPb_clicked(self):
        self.showImg(self.inImg)

    def CMYPb_clicked(self):
        inImg = 255 - self.inImg
        self.showImg(inImg)
    
    def HSIPb_clicked(self):
        rows, cols, dims = self.inImg.shape
        inImg = self.inImg / 255.0
        hsiImg = inImg
        for i in range(rows):
            for j in range(cols):
                b, g, r = inImg[i, j, :]
                I = (r+g+b)/3.0
                if (r+g+b) == 0: S = 0
                else: S = 1-3.0/(r+g+b)*min((r,g,b))
                if S != 0:
                    den = np.sqrt()
                




        self.showImg(hsiImg)
                

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
    
    def showImg(self, input, inLB = False):
        outImg = self.MatToQImage(input)
        if inLB == True:
            self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio)) 
        else:
            self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio)) 

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = MainWindow()
    w.show()
    app.exec_()