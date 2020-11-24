import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QToolButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Button(QToolButton):
    fontsize = 20

    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.setFont(QFont('Times', self.fontsize))


# class opperButton(QToolButton):
#     fontsize = 30
#
#     def __init__(self, text, parent= None):
#         super(opperButton, self).__init__(parent)
#
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
#         self.setText(text)
#         self.setFont(QFont('Arial', self.fontsize))
#         self.opperbutton.setStyleSheet("background-color:red")
#

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 18)
        self.display.setFont(font)

        self.grid.addWidget(self.display, 0, 0, 1, 4)


        self.ACButton = self.createButton('AC')
        self.grid.addWidget(self.ACButton, 1, 0)
        self.PMButton = self.createButton('+/-')
        self.grid.addWidget(self.PMButton, 1, 1)
        self.ModButton = self.createButton('%')
        self.grid.addWidget(self.ModButton, 1, 2)
        self.divisionButton = self.createButton(u"\N{DIVISION SIGN}")
        self.grid.addWidget(self.divisionButton, 1, 3)

        self.sevenButton = self.createButton('7')
        self.eightButton = self.createButton('8')
        self.nineButton = self.createButton('9')
        self.fourButton = self.createButton('4')
        self.fiveButton = self.createButton('5')
        self.sixButton = self.createButton('6')
        self.oneButton = self.createButton('1')
        self.twoButton = self.createButton('2')
        self.threeButton = self.createButton('3')
        self.zeroButton = self.createButton('0')

        self.grid.addWidget(self.sevenButton, 2, 0)
        self.grid.addWidget(self.eightButton, 2, 1)
        self.grid.addWidget(self.nineButton, 2, 2)
        self.multButton = self.createButton('X')
        self.grid.addWidget(self.multButton, 2, 3)

        self.grid.addWidget(self.fourButton, 3, 0)
        self.grid.addWidget(self.fiveButton, 3, 1)
        self.grid.addWidget(self.sixButton, 3, 2)

        self.minusButton = self.createButton("-")
        self.grid.addWidget(self.minusButton, 3, 3)

        self.grid.addWidget(self.oneButton, 4, 0)
        self.grid.addWidget(self.twoButton, 4, 1)
        self.grid.addWidget(self.threeButton, 4, 2)

        self.plusButton = self.createButton('+')
        self.grid.addWidget(self.plusButton, 4, 3)

        self.grid.addWidget(self.zeroButton, 5, 0, 1, 2)

        self.dotButton = self.createButton('.')
        self.grid.addWidget(self.dotButton, 5, 2)

        self.eqlButton = self.oppButton('=')
        self.grid.addWidget(self.eqlButton, 5, 3)


        #self.grid.addWidget(self.timesButton, 3, 4)

        #self.grid.addWidget(self.plusButton, 5, 4)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def createButton(self, text):
        button = Button(text)
        return button

    def oppButton(self, text):
        button = opperButton(text)
        return button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())