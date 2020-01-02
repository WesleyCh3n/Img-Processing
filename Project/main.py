from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from myui import *
import cv2
import numpy as np
import pandas as pd
import qdarkstyle
import matplotlib.pyplot as plt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.path = ''
        self.x = []
        self.y = []

        self.drawPb.clicked.connect(self.drawPb_clicked)
        self.wrapPb.clicked.connect(self.wrapPb_clicked)
        self.actionOpen_Image.triggered.connect(self.openImg_clicked)

    def openImg_clicked(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp *.png)")
        self.inImg = cv2.imread(self.path[0])
        self.showImg(self.inImg, True)

    def drawPb_clicked(self):
        self.x, self.y =  [], []
        def onclick(event):
            if event.xdata != None and event.ydata != None:
                self.x.append(event.xdata)
                self.y.append(event.ydata)
                plt.plot(event.xdata, event.ydata, '.')
                fig.canvas.draw()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        drawImg = np.copy(self.inImg)
        plt.imshow(drawImg)
        plt.imshow(cv2.cvtColor(drawImg, cv2.COLOR_BGR2RGB))

        cid = fig.canvas.mpl_connect('button_press_event', onclick)

        plt.show()

    def wrapPb_clicked(self):
        wrapImg = np.copy(self.inImg)
        print(self.x, self.y)
        arr = np.c_[self.x, self.y]
        print(arr)
        pt1 = np.float32(np.round(arr))
        pt2 = np.float32([[0,0],[2480,0],[0,3508],[2480,3508]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        result = cv2.warpPerspective(wrapImg, matrix,(2480,3508))
        plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.show()
        return 0

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

    def showImg(self, input, inLb = False):
        outImg = self.MatToQImage(input)
        if inLb == True:
            self.inputLb.setPixmap(outImg.scaled(self.inputLb.width(),self.inputLb.height(),Qt.KeepAspectRatio)) 
        else:
            self.outputLb.setPixmap(outImg.scaled(self.outputLb.width(),self.outputLb.height(),Qt.KeepAspectRatio)) 

if __name__ == "__main__":
    App = QApplication([])
    App.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = MainWindow()
    w.show()
    App.exec_()
