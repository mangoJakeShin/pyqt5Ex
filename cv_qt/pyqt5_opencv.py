from PyQt5 import uic
import sys
import cv2
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QComboBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
import os
import numpy as np
from PIL import Image

form_class = uic.loadUiType("test.ui")[0]

class MyApp(QWidget,form_class):
    src = ""
    tmp = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.show()

    def initUI(self):
        # pass
        self.openBtn.clicked.connect(self.openImg)
        self.applyBtn.clicked.connect(self.applyImg)
        #self.saveBtn.clicked.connect(self.saveImg())


    def openImg(self):
        self.fname = QFileDialog.getOpenFileName(self)
        self.imgname = self.fname[0]
        if (os.path.isfile(self.imgname)):
            self.src = cv2.imread(self.imgname)
            pix = QPixmap(self.imgname)
            self.orgImg.setPixmap(pix)


    def saveImg(self):
        dstname = self.fname + "change.%i" + ".jpg"
        cv2.imwrite(dstname, self.src)
        print(dstname + " saved")

    def applyImg(self):
        if (self.blurBtn.isChecked()):
            self.blurImg()
            print('blur done')
        #
        # if (self.sharpBtn.ischecked()):
        #     self.sharpImg()
        #     print('sharpening done')

        if (self.grayChk.isChecked()):
            self.grayImg()
            print('gray done')


        self.applyShow()

    def sharpImg(self):
        kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.tmp = cv2.filter2D(self.src, -1, kernel)

    def grayImg(self):
        self.tmp = cv2.cvtColor(self.src,cv2.COLOR_BGR2GRAY)
        return

    def blurImg(self):
        self.tmp = cv2.blur(self.src,(5,5))

    def applyShow(self):
        print(self.src.shape)
        if (len(self.tmp) == 0):
            return

        else:
            tmpPix = QImage(self.tmp.data, self.src.shape[1], self.src.shape[0],  QImage.Format_RGB888)
            tmpPixMap = QPixmap.fromImage(tmpPix)
            self.tgtImg.setPixmap(tmpPixMap)


if __name__ == '__main__':


    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
