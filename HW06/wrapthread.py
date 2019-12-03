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

    def trap(self):
        rows, cols, dims = self.inImg.shape
        transImg = np.zeros((rows, cols, 3), np.uint8)
        for y in range(rows):
            for x in range(cols):
                transImg[int(3*y/4+x*y/(rows*cols))][int(x+y/4-x*y/(2*rows))] = self.inImg[y][x]
            self.progress.emit(y*101/rows)
        self.processImg.emit(transImg)
    
    def resetFlag(self):
        self.trapFlag == False

    def run(self):
        if self.trapFlag == True:
            self.trap()
        self.resetFlag()