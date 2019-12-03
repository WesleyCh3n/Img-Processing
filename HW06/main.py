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
        self.wavyBn.clicked.connect(self.wavyBn_clicked)
        self.cirBn.clicked.connect(self.cirBn_clicked)
        self.houBn.clicked.connect(self.houBn_clicked)

        self.htsB.setRange(1, 100)
        self.htsB.setValue(51)
        self.hmsB.setRange(1, 100)
        self.hmsB.setValue(50)
        self.sB.setRange(1, 100)
        self.sB.setValue(50)
        self.dsB.setRange(0.01, 100)
        self.dsB.setValue(2)
        self.dsB.setSingleStep(0.1)

        self.wrapObj = wrap()
        self.wrapObj.progress.connect(self.progressBar.setValue)
        self.wrapObj.processImg.connect(self.showImg)

    def actionOpen_file_triggered(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
        self.inImg = cv2.imread(self.path[0])
        self.wrapObj.inImg = self.inImg
        self.showImg(self.inImg, True)

    def trapBn_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.wrapObj.trapFlag = True
        self.wrapObj.start()

    def wavyBn_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.wrapObj.amp = self.sB.value()
        self.wrapObj.freq = self.dsB.value()
        self.wrapObj.wavyFlag = True
        self.wrapObj.start()

    def cirBn_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.wrapObj.cirFlag = True
        self.wrapObj.start()

    def houBn_clicked(self):
        if self.path == False: return QMessageBox.warning(self, "WARNING", "The input image is empty")
        img = cv2.cvtColor(self.inImg, cv2.COLOR_BGR2GRAY)
        outImg = np.copy(self.inImg)
        edgesImg = cv2.Canny(img ,50,150,apertureSize = 3) 
        lines = cv2.HoughLinesP(edgesImg, 1, np.pi/360, self.htsB.value(), None, self.hmsB.value(), 10)
        numbers, dummy, points = lines.shape
        len_sum = 0
        for x1, y1, x2, y2 in lines.reshape((numbers,points)):
            cv2.line(outImg, (x1,y1), (x2,y2), (0,255,0), 5)
            len_sum += np.sqrt((x1-x2)**2+(y1-y2)**2)
        for x1, y1, x2, y2 in lines.reshape((numbers,points)):
            cv2.putText(outImg, f"{np.sqrt((x1-x2)**2+(y1-y2)**2):.2f} pixels", (int(round((x2+x1)/2)), int(round((y1+y2)/2))), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
        self.textBrowser.append(f"Total pixel length is {len_sum:.2f}")
        self.textBrowser.append(f"There are {numbers} lines\n"+"="*16)
        self.showImg(outImg)
        
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

    
