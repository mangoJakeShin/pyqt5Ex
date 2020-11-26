#단위 환산기

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

        qle = QLineEdit(self)
        qle.move(20, 20)
        qle.textChanged[str].connect(self.onChanged)

        #input
        self.lbl = QLabel(self)
        self.lbl.move(100,50)
        self.inputlbl = QLabel('hi',self)
        self.inputlbl.move(20,55)



        self.measurelbl = QLabel('Choose a measurement', self)
        self.measurelbl.move(20, 80)

        # self.kmlbl = QLabel(self.kmtxt,self)
        # self.kmlbl.move(30, 80)
        #
        # self.mlbl = QLabel(self.mtxt, self)
        # self.kmlbl.move(30, 130)
        #
        # self.kmlbl = QLabel(self.kmtxt, self)
        # self.kmlbl.move(30, 80)
        #
        # self.kmlbl = QLabel(self.kmtxt, self)
        # self.kmlbl.move(30, 80)

        cb = QComboBox(self)
        cb.addItem('mm')
        cb.addItem('cm')
        cb.addItem('m')
        cb.addItem('km')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.measureChange(text)
        self.measurelbl.setText(self.inputlbl.text() +" " + text + " is equal to"
                                + "\n\n" + str(self.mm) + " mm"
                                + "\t" + str(self.cm) + " cm"
                                +"\n\n" + str(self.m) + " m"
                                +"\t\t" + str(self.km) + " km"
                                )
        self.measurelbl.adjustSize()

    def measureChange(self,text):
        a = float(self.inputlbl.text())
        if text == 'mm':
            b = 0
        elif text == 'cm':
            b = 1
        elif text == 'm':
            b = -3
        elif text == 'km':
            b = -6

        self.mm = a / (10 ** (0 - b))
        self.cm = a / (10 ** (1 - b))
        self.m = a / (10 ** (3 - b))
        self.km = a / (10 ** (6 - b))


    def onChanged(self, text):
        self.inputlbl.setText(text)
        self.inputlbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())










