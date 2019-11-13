from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import qdarkstyle
from colorTransThread import colorTrans

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
        self.XYZPb.clicked.connect(self.XYZPb_clicked)
        self.LabPb.clicked.connect(self.LabPb_clicked)
        self.YUVPb.clicked.connect(self.YUVPb_clicked)
        self.pseudoPb.clicked.connect(self.pseudoPb_clicked)
        self.kmeanPb.clicked.connect(self.kmeanPb_clicked)

        self.springRb.clicked.connect(self.checkSignal)
        self.summerRb.clicked.connect(self.checkSignal)
        self.autumnRb.clicked.connect(self.checkSignal)
        self.winterRb.clicked.connect(self.checkSignal)
        self.hotRb.clicked.connect(self.checkSignal)
        self.coolRb.clicked.connect(self.checkSignal)
        self.twilightRb.clicked.connect(self.checkSignal)
        self.rainbowRb.clicked.connect(self.checkSignal)

        self.kmeanSd.setToolTip("The range is from 2 to 10")
        self.kmeanSd.valueChanged.connect(self.kLbShow)

        self.threadObj = colorTrans()
        self.threadObj.progress.connect(self.pB.setValue)
        self.threadObj.processImg.connect(self.showImg)

    def actionOpen_File_triggered(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
        self.inImg = cv2.imread(self.path[0])
        self.threadObj.inImg = self.inImg
        self.showImg(self.inImg, True)

    def RGBPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.showImg(self.inImg)

    def CMYPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        inImg = 255 - self.inImg
        self.showImg(inImg)
    
    def HSIPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.threadObj.hsiFlag = True
        self.threadObj.start()

    def XYZPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.threadObj.xyzFlag = True
        self.threadObj.start()

    def LabPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.threadObj.LabFlag = True
        self.threadObj.start()

    def YUVPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.threadObj.yuvFlag = True
        self.threadObj.start()

    def pseudoPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        inImg = self.inImg

        pseudoImg = np.copy(inImg)
        grayImg = cv2.imread(self.path[0], 0)
        rows, cols,pseudoImg dims = self.inImg.shape
        colorMap = cv2.applyColorMap(np.arange(256).reshape(1,256,1).astype(np.uint8),self.groupButton.checkedId())
        for i in range(rows):
            for j in range(cols):
                pseudoImg[i, j, :] = colorMap[0,grayImg[i,j],:]

        outImg = cv2.applyColorMap(inImg, self.groupButton.checkedId())
        self.showImg(outImg)
    
    def kmeanPb_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        inImg = self.inImg
        flatImg = inImg.reshape((-1,3)).astype(np.float32)
        criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, center = cv2.kmeans(flatImg, self.kmeanSd.value(), None, criteria, 10, cv2.KMEANS_PP_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        outputImg = res.reshape((inImg.shape))
        self.showImg(outputImg)
    
    def kLbShow(self):
        self.kLb.setText("K = "+str(self.kmeanSd.value()))
    
    def checkSignal(self):
        colorMap = cv2.applyColorMap(np.arange(256).reshape(1,256,1).astype(np.uint8),self.groupButton.checkedId())
        self.showImg(colorMap, cmapLb=True)

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
    
    def showImg(self, input, inLb = False, cmapLb = False):
        outImg = self.MatToQImage(input)
        if inLb == True:
            self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio)) 
        elif cmapLb == True:
            self.cmapLb.setPixmap(outImg.scaled(self.cmapLb.width(),self.inputLb.height()))
        else:
            self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio)) 

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = MainWindow()
    w.show()
    app.exec_()