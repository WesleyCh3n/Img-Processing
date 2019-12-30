from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from myui import *
import cv2
import qdarkstyle
import matplotlib.pyplot as plt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pB_clicked)

    def pB_clicked(self):
        def onclick(event):
            if event.xdata != None and event.ydata != None:
                print(event.xdata, event.ydata)
                plt.plot(event.xdata, event.ydata, '.')
                fig.canvas.draw()

        img = cv2.imread('./img.jpg')
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.imshow(img)

        cid = fig.canvas.mpl_connect('button_press_event', onclick)

        plt.show()

if __name__ == "__main__":
    App = QApplication([])
    App.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = MainWindow()
    w.show()
    App.exec_()
