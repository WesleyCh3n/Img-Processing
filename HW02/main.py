import sys
from myui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

class MainWindow(QMainWindow, Ui_MainWindow):

    inImg = QImage()
    path = False
    histo = []
    setHisto = QBarSet("256 Grayscale")
    yLimit = 5000 
    for i in range(256):
            histo.append(0)

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.bSlider.setRange(0, 255)
        self.bSlider.setSingleStep(1)

        self.briSlider.setRange(-255, 255)
        self.briSlider.setSingleStep(1)

        self.conSlider.setRange(-128, 128)
        self.conSlider.setSingleStep(1)

        self.lsB.setRange(1,10)
        self.lsB.setSingleStep(1)
        self.lsB.setSuffix("%")

        self.ssB.setRange(0.1, 1.0)
        self.ssB.setSingleStep(0.1)
        self.ssB.setValue(1.0)
        self.ssB.setSuffix("%")
        chartView = QChartView(self.showchart())
        self.grid1.addWidget(chartView, 1, 1) 

        self.actionOpen_File.triggered.connect(self.openImg_click)
        self.actionReset.triggered.connect(self.reset_click)
        self.grayaBn.clicked.connect(self.grayaBn_click)
        self.graybBn.clicked.connect(self.graybBn_click)
        self.subBn.clicked.connect(self.subBn_click)
        self.eqBn.clicked.connect(self.eqBn_click)
        self.bSlider.sliderReleased.connect(self.bSlider_change)
        self.briSlider.sliderReleased.connect(self.briSlider_change)
        self.conSlider.sliderReleased.connect(self.conSlider_change)
        self.lsB.valueChanged.connect(self.lsB_change)
        self.ssB.valueChanged.connect(self.ssB_change)

    def showchart(self):
        for i in range(256):
            self.setHisto.append(0)
        series = QBarSeries()
        series.append(self.setHisto)
        chart = QChart()
        chart.setTheme(QChart.ChartThemeDark)
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axisX = QValueAxis()
        axisX.setRange(0,255)
        axisX.setLabelFormat("%u")
        axisX.setGridLineVisible(True)
        axisX.setTickCount(4)
        axisX.setMinorTickCount(1)
        axisX.setTitleText("X")
        chart.addAxis(axisX, Qt.AlignBottom)

        axisY = QValueAxis()
        axisY.setRange(0,self.yLimit)
        axisY.setLabelFormat("%u")
        axisY.setGridLineVisible(True)
        axisY.setTickCount(5)
        axisY.setMinorTickCount(1)
        axisY.setTitleText("Frequency")
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)
        font = QFont("Helvetica", 15)
        chart.setTitleFont(font)
        chart.setTitle("Histogram")
        chart.legend().setVisible(False);
        # chart.legend().setAlignment(Qt.AlignTop);
        return chart

    def openImg_click(self):
        self.path = QFileDialog.getOpenFileName(self,"Open file","","Images(*.jpg *.bmp)")
        self.inImg.load(self.path[0])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def reset_click(self):
        if self.path == False :return 0
        self.histo = [0 for i in range(256)]
        self.inImg.load(self.path[0])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))
        self.bSlider.setValue(0)
        self.briSlider.setValue(0)
        self.conSlider.setValue(0)
        self.lsB.setValue(1)
        self.ssB.setValue(1.0)

    def grayaBn_click(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave = (oldColor.red()+oldColor.green()+oldColor.blue())/3
                val = qRgb(ave,ave,ave)
                self.histo[int(ave)] += 1
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def graybBn_click(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave = oldColor.red()*0.299 + oldColor.green()*0.587 + oldColor.blue()*0.114
                val = qRgb(ave,ave,ave)
                self.histo[int(ave)] += 1
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def subBn_click(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave1 = (oldColor.red()+oldColor.green()+oldColor.blue())/3
                ave2 = oldColor.red()*0.299 + oldColor.green()*0.587 + oldColor.blue()*0.114
                func = lambda x, y:0 if (x-y) <= 0 else (x-y)*150 if ((x-y)*255) < 255 else 255
                self.histo[int(func(ave2, ave1))] += 1
                val = qRgb(func(ave2, ave1),func(ave2, ave1),func(ave2, ave1))
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def eqBn_click(self):
        if self.path == False: return QMessageBox.warning(self, "Warning", "The input image is empty")
        self.histo = [0 for i in range(256)]
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave = (oldColor.red()+oldColor.green()+oldColor.blue())/3
                self.histo[int(ave)] += 1
        sum_ = 0
        tfunc = [0 for i in range(256)]
        for i in range(256):
            sum_ += self.histo[i]/ (self.inImg.width()*self.inImg.height())
            tfunc[i] = int(sum_ * i)
        # print(tfunc[:])
        self.histo = [0 for i in range(256)]
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave = (oldColor.red()+oldColor.green()+oldColor.blue())/3
                val = qRgb(tfunc[int(ave)], tfunc[int(ave)],tfunc[int(ave)])
                self.histo[tfunc[int(ave)]] += 1
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def bSlider_change(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        thresh = self.bSlider.value()
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                ave = (oldColor.red()+oldColor.green()+oldColor.blue())/3
                func = lambda x, y:255 if x > y else 0
                val = qRgb(func(ave, thresh),func(ave, thresh),func(ave, thresh))
                self.histo[func(ave, thresh)] += 1
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def briSlider_change(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        thresh = self.briSlider.value()
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                func = lambda c, t: c + t if (c + t)>=0 and (c + t)<=255 else 255 if (c + t)>255 else 0
                val = qRgb(func(oldColor.red(), thresh),func(oldColor.green(), thresh),func(oldColor.blue(), thresh))
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def conSlider_change(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        self.histo = [0 for i in range(256)]
        thresh = self.conSlider.value()
        self.inImg.load(self.path[0])
        for x in range(self.inImg.width()):
            for y in range(self.inImg.height()):
                oldColor = QColor(self.inImg.pixel(x,y))
                # func = lambda x, y: ((259*(x+255))/(255*(259-x)))*(y-128)+128
                func = lambda x, y: ((256*(x+256))/(256*(256-x)))*(y-128)+128
                limit = lambda x: 255 if x>255 else 0 if x<0 else x
                val = qRgb(limit(int(func(thresh, oldColor.red()))),limit(int(func(thresh, oldColor.green()))),limit(int(func(thresh, oldColor.blue()))))
                self.inImg.setPixel(x,y,val)
        for i in range(256):
            self.setHisto.replace(i,self.histo[i])
        outImg = QPixmap.fromImage(self.inImg)
        self.imgLb.setPixmap(outImg.scaled(self.imgLb.width(),self.imgLb.height(),Qt.KeepAspectRatio))

    def lsB_change(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        thresh = self.lsB.value()
        self.inImg.load(self.path[0])
        new_image = QImage(QSize(int(self.inImg.width()*thresh), int(self.inImg.height()*thresh)),QImage.Format_RGB32);
        for x in range(int(self.inImg.width()*thresh)):
            for y in range(int(self.inImg.height()*thresh)):
                oldColor = QColor(self.inImg.pixel(int(x/thresh),int(y/thresh)))
                val = qRgb(oldColor.red(),oldColor.green(),oldColor.blue())
                new_image.setPixel(x,y, val)
        outImg = QPixmap.fromImage(new_image)
        self.imgLb.setPixmap(outImg)

    def ssB_change(self):
        if self.path == False :return QMessageBox.warning(self, "WARNING", "The input image is empty")
        thresh = self.ssB.value()
        self.inImg.load(self.path[0])
        new_image = QImage(QSize(int(self.inImg.width()*thresh), int(self.inImg.height()*thresh)),QImage.Format_RGB32);
        for x in range(int(self.inImg.width()*thresh)):
            for y in range(int(self.inImg.height()*thresh)):
                oldColor = QColor(self.inImg.pixel(int(x/thresh),int(y/thresh)))
                val = qRgb(oldColor.red(),oldColor.green(),oldColor.blue())
                new_image.setPixel(x,y, val)
        outImg = QPixmap.fromImage(new_image)
        self.imgLb.setPixmap(outImg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color:rgb(40,40,40);color:rgb(150,100,150)")
    w.show()
    sys.exit(app.exec_())