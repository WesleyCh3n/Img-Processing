import cv2
import numpy as np
from PyQt5.QtCore import *

class colorTrans(QThread):
    progress = pyqtSignal(int)
    processImg = pyqtSignal(np.ndarray)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.hsiFlag = False
        self.xyzFlag = False
        self.LabFlag = False
        self.yuvFlag = False
    
    def HSY(self):
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
            self.progress.emit(i*101/rows)
        self.processImg.emit(hsiImg)

    def XYZ(self):
        inImg = self.inImg/255.0
        xyzImg = self.inImg/255.0
        rows, cols, dims = self.inImg.shape
        for i in range(rows):
            for j in range(cols):
                b, g, r = inImg[i, j, :]
                x = (0.412453*r + 0.357580*g + 0.180423*b)*255
                y = (0.212671*r + 0.715160*g + 0.072169*b)*255
                z = (0.019334*r + 0.119193*g + 0.950227*b)*255
                xyzImg[i, j, :] = z, y, x
            self.progress.emit(i*101/rows)
        self.processImg.emit(xyzImg)
    
    def Lab(self):
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
                # LabImg[i,j,:] = L*2.55, a+128, b_+128
                LabImg[i,j,:] = b_+128, a+128, L*2.55
            self.progress.emit(i*101/rows)
        self.processImg.emit(LabImg)
    
    def YUV(self):
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
                YUVImg[i, j, :] = V, U, Y*255
            self.progress.emit(i*101/rows)
        self.processImg.emit(YUVImg) 

    def resetFlag(self):
        self.hsiFlag = False
        self.xyzFlag = False
        self.LabFlag = False
        self.yuvFlag = False

    def run(self):
        if self.hsiFlag == True:
            self.HSY()
        if self.xyzFlag == True:
            self.XYZ()
        if self.LabFlag == True:
            self.Lab()
        if self.yuvFlag == True:
            self.YUV()
        self.resetFlag()