import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QToolButton, QSizePolicy

from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        grid.addWidget(self.display,0, 0, 1,4)

        grid.addWidget(QPushButton('AC'), 1, 0)
        grid.addWidget(QPushButton('+/-'),1, 1)
        grid.addWidget(QPushButton('%'),1, 2)
        grid.addWidget(QPushButton('/'),1, 3)

        grid.addWidget(QPushButton('7'),2, 0)
        grid.addWidget(QPushButton('8'),2, 1)
        grid.addWidget(QPushButton('9'),2, 2)
        grid.addWidget(QPushButton('X'),2, 3)

        grid.addWidget(QPushButton('4'),3, 0)
        grid.addWidget(QPushButton('5'),3, 1)
        grid.addWidget(QPushButton('6'),3, 2)
        grid.addWidget(QPushButton('-'),3, 3)

        grid.addWidget(QPushButton('1'),4, 0)
        grid.addWidget(QPushButton('2'),4, 1)
        grid.addWidget(QPushButton('3'),4, 2)
        grid.addWidget(QPushButton('+'),4, 3)

        grid.addWidget(QPushButton('0'),5, 0, 1,2)
        grid.addWidget(QPushButton('.'),5, 2)
        grid.addWidget(QPushButton('='),5, 3)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())