## 01 opening window
# import sys
# # from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('My First Application')
#         self.move(130, 130)
#         self.center()
#         # self.resize(400, 200)
#         self.show()
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MyApp()
#    sys.exit(app.exec_())

# # putting icon
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
#
#
# class MyApp(QWidget):
#
#   def __init__(self):
#       super().__init__()
#       self.initUI()
#
#   def initUI(self):
#       self.setWindowTitle('Icon')
#       self.setWindowIcon(QIcon('web.png'))
#       #png = alpha channel
#       self.setGeometry(300, 300, 300, 200)
#                        좌표  좌표 사이즈 사이즈
#       self.show()
#
#
# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   ex = MyApp()
#   sys.exit(app.exec_())
#
# ## Ex 3-3. 창 닫기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtCore import QCoreApplication
#
#
# class MyApp(QWidget):
#
#   def __init__(self):
#       super().__init__()
#       self.initUI()
#
#   def initUI(self):
#       btn = QPushButton('Quit', self)
#       btn.move(150, 150)
#       btn.resize(btn.sizeHint())
#       btn.clicked.connect(QCoreApplication.instance().quit)
#
#       self.setWindowTitle('Quit Button')
#       self.setGeometry(300, 300, 300, 200)
#       self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
#
# #
# ## Ex 3-4. 툴팁 나타내기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
# from PyQt5.QtGui import QFont
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))
#         self.setToolTip('This is a <b>QWidget</b> widget')
#
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.move(50, 50)
#         btn.resize(btn.sizeHint())
#
#         self.setWindowTitle('Tooltips')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
#
#
# ## Ex 3-5. 상태바 만들기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
#
# class MyApp(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.statusBar().showMessage('Ready')
#
#         self.setWindowTitle('Statusbar')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
#
## Ex 3-6. 메뉴바 만들기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
# from PyQt5.QtGui import QIcon
#
#
# class MyApp(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction = QAction(QIcon('exit.png'), '&Exit', self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         menubar.setNativeMenuBar(False)
#         filemenu = menubar.addMenu('&File')
#         #&기호가 있는 문자를 통해 바로가기키 지정 가능
#         filemenu.addAction(exitAction)
#
#         self.setWindowTitle('Menubar')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        btn3 = QPushButton('3')
        btn4 = QPushButton('4')
        btn5 = QPushButton('5')
        btn6 = QPushButton('6')
        btn7 = QPushButton('7')
        btn8 = QPushButton('8')
        btn9 = QPushButton('9')
        btn0 = QPushButton('0')
        btnplus = QPushButton('+')
        btnminus = QPushButton('-')
        btndiv = QPushButton('/')
        btnmult = QPushButton('*')
        btneql = QPushButton('=')
        btnplmi = QPushButton('+/-')
        btndot = QPushButton('.')

        font1 = label1.font()
        font1.setPointSize(20)


        label1.setFont(font1)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        layout.addWidget(btn7)
        layout.addWidget(btn8)
        layout.addWidget(btn9)
        layout.addWidget(btn0)
        layout.addWidget(btnplmi)
        layout.addWidget(btnplus)
        layout.addWidget(btnminus)
        layout.addWidget(btnmult)
        layout.addWidget(btndiv)
        layout.addWidget(btndot)
        layout.addWidget(btneql)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # def setupUI(self):
    #     grid = QGridLayout()
    #     self.setLayout(grid)
    #
    #     self.display = QLineEdit('0')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())













