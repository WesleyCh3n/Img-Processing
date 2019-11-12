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
        self.XYZPb.clicked.connect(self.XYZPb_clicked)
        self.LabPb.clicked.connect(self.LabPb_clicked)
        self.YUVPb.clicked.connect(self.YUVPb_clicked)
        self.pseudoPb.clicked.connect(self.pseudoPb_clicked)
        self.kmeanPb.clicked.connect(self.kmeanPb_clicked)

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
                    den = np.sqrt((r-g)**2+(r-b)*(g-b))
                    if den == 0: H =0
                    else:
                        theta = np.arccos(0.5*((r-g)+(r-b))/den)
                        if b <= g: H = theta
                        else: H = 2*np.pi - theta
                else: H = 0
                hsiImg[i,j,2] = H / 2*np.pi *255
                hsiImg[i,j,1] = S * 255
                hsiImg[i,j,0] = I * 255
        self.showImg(hsiImg)

    def XYZPb_clicked(self):
        inImg = self.inImg/255.0
        inImg = self.inImg/255.0
        rows, cols, dims = self.inImg.shape
        for i in range(rows):
            for j in range(cols):
                b, g, r = inImg[i, j, :]
                x = (0.412453*r + 0.357580*g + 0.180423*b)*255
                y = (0.212671*r + 0.715160*g + 0.072169*b)*255
                z = (0.019334*r + 0.119193*g + 0.950227*b)*255
                xyzImg[i, j, :] = z, y, x
        self.showImg(xyzImg)

    def LabPb_clicked(self):
        inImg = self.inImg/255.0
        LabImg = self.inImg/255.0
        rows, cols, dims = self.inImg.shape
        funcH = lambda q: q**(1/3) if q > 0.008856 else (7.787*q + 16/116)
        for i in range(rows):
            for j in range(cols): 
                b, g, r = inImg[i, j, :]
                x = (0.412453*r + 0.357580*g + 0.180423*b)*255
                y = (0.212671*r + 0.715160*g + 0.072169*b)*255
                z = (0.019334*r + 0.119193*g + 0.950227*b)*255 
                L = 116*funcH(y/1)-16
                a = 500*(funcH(x/0.950456)-funcH(y))
                b_ = 200*(funcH(y/1)-funcH(z/1.088754))
                LabImg[i,j,:] = L*2.55, a+128, b_+128
        self.showImg(LabImg)

    def YUVPb_clicked(self):
        inImg = self.inImg/255.0 
        YUVImg = self.inImg/255.0
        rows, cols, dims = self.inImg.shape
        for i in range(rows):
            for j in range(cols):
                b, g, r = inImg[i, j, :]
                Y = 0.299*r + 0.587*g + 0.114*b
                U = (r-Y)*0.713 + 128
                V = (b-Y)*0.564 + 128
                YUVImg[i, j, :] = Y*255, U, V
        self.showImg(YUVImg)

    def pseudoPb_clicked(self):
        # print(self.summerRb.isChecked())
        inImg = self.inImg
        grayImg = cv2.imread(self.path[0], 0)
        pseudoImg = np.copy(inImg)
        rows, cols, dims = self.inImg.shape
        colorMap = cv2.applyColorMap(np.arange(256).reshape(1,256,1).astype(np.uint8),6)
        outImg = self.MatToQImage(colorMap)
        self.cmapLb.setPixmap(outImg.scaled(self.cmapLb.width(),self.inputLb.height())) 

        for i in range(rows):
            for j in range(cols):
                pseudoImg[i, j, :] = colorMap[0,grayImg[i,j],:]

        # outImg = cv2.applyColorMap(inImg, cv2.COLORMAP_SUMMER)
        self.showImg(pseudoImg)
    
    def kmeanPb_clicked(self):
        inImg = self.inImg
        flatImg = inImg.reshape((-1,3)).astype(np.float32)
        criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, center = cv2.kmeans(flatImg, 2, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        outputImg = res.reshape((inImg.shape))
        self.showImg(outputImg)

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