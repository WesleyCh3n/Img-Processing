from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from myui import *
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import qdarkstyle

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.path = ''
        self.x = []
        self.y = []

        self.drawPb.clicked.connect(self.drawPb_clicked)
        self.wrapPb.clicked.connect(self.wrapPb_clicked)
        self.pdfPb.clicked.connect(self.pdfPb_clicked)
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
        self.df = None
        wrapImg = np.copy(cv2.cvtColor(self.inImg, cv2.COLOR_BGR2GRAY))
        kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
        wrapImg = cv2.filter2D(wrapImg, -1, kernel)
        print(self.x, self.y)
        arr = np.c_[self.x, self.y]
        print(arr)
        pt1 = np.float32(np.round(arr))
        pt2 = np.float32([[0,0],[2480,0],[0,3508],[2480,3508]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        result = cv2.warpPerspective(wrapImg, matrix,(2480,3508))

        df = pytesseract.image_to_data(result, output_type=Output.DATAFRAME)
        df['text'].replace('', np.nan, inplace=True)
        df.dropna(subset=['text'], inplace=True)
        self.df = df
        for i in range(len(df['level'])):
            (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

        self.showImg(result)
        plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.show()

    def pdfPb_clicked(self):
        pdf = FPDF('P','pt','A4')
        pdf.add_page()
        pdf.add_font('Times', '', './times-new-roman.ttf', uni=True)
        pdf.set_font('Times', '', 10)
        for i in range(len(self.df['level'])):
            (x, y, w, h) = (self.df['left'].iloc[i], self.df['top'].iloc[i], self.df['width'].iloc[i], self.df['height'].iloc[i])
            pdf.set_xy(x*(595/2479), y*(842/3580))
            pdf.cell(0, 0, self.df['text'].iloc[i])
        pdf.output('output.pdf')
        QMessageBox.warning(self, "STATUS", "Output Complete!")

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
