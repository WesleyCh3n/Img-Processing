import cv2
import numpy as np
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from myui import *
from wrapthread import wrap

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.path = False
        self.inImg = False

        self.actionOpen_Image.triggered.connect(self.actionOpen_file_triggered)
        self.trapBn.clicked.connect(self.trapBn_clicked)        

        self.wrapObj = wrap()
        self.wrapObj.progress.connect(self.progressBar.setValue)
        self.wrapObj.processImg.connect(self.showImg)

    def actionOpen_file_triggered(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
        self.inImg = cv2.imread(self.path[0])
        #self.threadObj.inImg = self.inImg
        self.showImg(self.inImg, True)

    def trapBn_clicked(self):
        self.wrapObj.inImg = self.inImg
        self.wrapObj.trapFlag = True
        self.wrapObj.start()

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

    
