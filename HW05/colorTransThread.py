import cv2
import numpy as np
from PyQt5.QtCore import *

class colorTrans(QThread):
    progress = pyqtSignal(int)
    processImg = pyqtSignal(np.ndarray)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.hsiFlag = False
    
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

    def run(self):
        if self.hsiFlag == True:
            self.HSY()
            self.hsiFlag == False