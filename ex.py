# km = 0
# cm = 0
# mm = 0
# m = 0
#
# list = []
#
# list.append(km)
# list.append(cm)
# list.append(mm)
# list.append(m)
#
#
# for i in list:
#     print(i)

# 단위 환산기

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    km = 0
    cm = 0
    mm = 0
    m = 0
    kmtxt = str(km) + " km"
    cmtxt = str(cm) + ' cm'
    mmtxt = str(mm) + ' mm'
    mtxt = str(m) + ' m'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.value = "0"
        self.unit = "mm"
        qle = QLineEdit(self)
        qle.move(20, 20)
        qle.textChanged[str].connect(self.onChanged)

        grid = QGridLayout()

        # input
        self.lbl = QLabel(self)
        # grid.addWidget(self.lbl, 0,0)
        self.lbl.move(100, 50)

        self.inputlbl = QLabel('hi', self)
        # grid.addWidget((self.inputlbl,1,0))
        self.inputlbl.move(20, 55)

        cb = QComboBox(self)
        cb.addItem('mm')
        cb.addItem('cm')
        cb.addItem('m')
        cb.addItem('km')
        cb.move(50, 50)

        self.measurelbl = QLabel('Choose a measurement', self)
        # grid.addWidget(self.measurelbl,2,0)
        self.measurelbl.move(20, 80)

        self.kmlbl = QLabel("hell")
        self.kmlbl.move(30, 100)
        self.mlbl = QLabel("mlbl")
        self.mlbl.move(80, 100)
        self.cmlbl = QLabel("cmlbl")
        self.cmlbl.move(30, 150)
        self.mmlbl = QLabel("mmlbl ")
        self.mmlbl.move(80, 150)




        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        print((self.kmtxt))
        self.measureChange(text)
        print(self.kmtxt)
        self.kmlbl.setText(self.kmtxt)
        self.kmlbl.adjustSize()
        self.mlbl.setText(self.mtxt)
        self.mlbl.adjustSize()
        self.cmlbl.setText(self.cmtxt)
        self.cmlbl.adjustSize()
        self.mmlbl.setText(self.mmtxt)
        self.mmlbl.adjustSize()

    def measureChange(self, text):
        print(self.inputlbl.text())
        a = float(self.inputlbl.text())
        if text == 'mm':
            self.mm = a
            self.cm = a / 10
            self.m = a / 1000
            self.km = a / 1000000
        elif text == 'cm':
            self.mm = a * 10
            self.cm = a
            self.m = a / 100
            self.km = a / 100000

        elif text == 'm':
            self.mm = a * 1000
            self.cm = a * 100
            self.m = a
            self.km = a / 1000

        elif text == 'km':
            self.mm = a * 1000000
            self.cm = a * 100000
            self.m = a * 1000
            self.km = a

        self.kmtxt = str(self.km) + " km"
        self.cmtxt = str(self.cm) + ' cm'
        self.mmtxt = str(self.mm) + ' mm'
        self.mtxt = str(self.m) + ' m'

    def onChanged(self, text):
        self.inputlbl.setText(text)
        self.inputlbl.adjustSize()
        self.value = text



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())










