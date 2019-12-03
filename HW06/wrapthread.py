from PyQt5.QtCore import *
import cv2
import numpy as np

class wrap(QThread):
    progress = pyqtSignal(int)
    processImg = pyqtSignal(np.ndarray)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inImg = False
        self.trapFlag = False
        self.wavyFlag = False
        self.cirFlag = False
        self.amp = 50
        self.freq = 2

    def trap(self):
        rows, cols, dims = self.inImg.shape
        transImg = np.zeros((rows, cols, 3), np.uint8)
        for y in range(rows):
            for x in range(cols):
                transImg[int(3*y/4+x*y/(rows*cols))][int(x+y/4-x*y/(2*rows))] = self.inImg[y][x]
            self.progress.emit(y*101/rows)
        self.processImg.emit(transImg)
    
    def wavy(self):
        rows, cols, dims = self.inImg.shape
        transImg = np.zeros((rows, cols, 3), np.uint8)
        for y in range(rows):
            for x in range(cols):
                x_offset = x + int(self.amp * np.sin(self.freq * np.pi * y / 150)) 
                y_offset = y + int(self.amp * np.cos(self.freq * np.pi * x / 150))
                if x_offset > 0 and y_offset > 0:
                    if y_offset<rows and x_offset < cols:
                        transImg[y][x] = self.inImg[(y_offset)%rows][(x_offset)%cols]
            self.progress.emit(y*101/rows)
        self.processImg.emit(transImg)

    def cir(self):
        rows, cols, dims = self.inImg.shape
        transImg = np.zeros((rows, cols, 3), np.uint8)
        xR = rows/2.0
        yR = cols/2.0
        for y in range(cols):
            for x in range(rows):
                x_ratio = (x - xR)/xR
                y_ratio = (y - yR)/yR
                x_mod = x_ratio * np.sqrt(1 - y_ratio**2/2) * xR + xR
                y_mod = y_ratio * np.sqrt(1 - x_ratio**2/2) * yR + yR
                transImg[int(x_mod)][int(y_mod)] = self.inImg[x][y]
            self.progress.emit(y*101/rows)
        self.processImg.emit(transImg)
        
    def resetFlag(self):
        self.trapFlag = False
        self.wavyFlag = False
        self.cirFlag = False
    
    def run(self):
        if self.trapFlag == True:
            self.trap()
        if self.wavyFlag == True:
            self.wavy()
        if self.cirFlag == True:
            self.cir()
        self.resetFlag()
