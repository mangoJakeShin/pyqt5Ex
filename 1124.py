# #push button
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#
#
# class MyApp(QWidget):
#     clicked = 0
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.btn1 = QPushButton('&Power On', self)
#         self.btn1.setCheckable(True)
#         self.btn1.toggle()
#
#         self.btn1.clicked.connect(self.btnOffToggle)
#         self.btn1.clicked.connect(self.btnOnToggle)
#         self.btn2 = QPushButton(self)
#         self.btn2.setText('Button&2')
#
#         self.btn3 = QPushButton('Button3', self)
#         self.btn3.setEnabled(False)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.btn1)
#         vbox.addWidget(self.btn2)
#         vbox.addWidget(self.btn3)
#
#         self.setLayout(vbox)
#         self.setWindowTitle('QPushButton')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#
#     def btnOffToggle(self):
#
#         if (self.btn1.isChecked() and ((self.clicked % 2) == 0)):
#             self.btn1.toggle()
#             self.btn1.setText('Power OFF')
#             self.btn1.setStyleSheet("Background-Color : Red")
#             self.clicked = self.clicked + 1
#
#     def btnOnToggle(self):
#         if (self.btn1.isChecked() and ((self.clicked % 2) == 1)):
#             self.btn1.toggle()
#             self.btn1.setText('Power On')
#             self.btn1.setStyleSheet('Background-color : yellow')
#             self.clicked = self.clicked + 1
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


## 라디오버튼
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.rbtn1 = QRadioButton('First Button', self)
#         self.rbtn1.move(50, 50)
#         self.rbtn1.setChecked(True)
#         #rbtn1.setChecked(False)
#
#         self.rbtn2 = QRadioButton(self)
#         self.rbtn2.move(50, 70)
#         self.rbtn2.setText('Second Button')
#         self.rbtn1.toggled.connect((self.radiobtn1Select))
#         self.rbtn2.toggled.connect((self.radiobtn2Select))
#         self.radiobtn2Select()
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QRadioButton')
#         self.show()
#
#
#         #group화 과정도 추가 필요함
#
#     def radiobtn1Select(self):
#         if (self.rbtn1.isChecked() == 1):
#             print('rbtn1 selected')
#
#     def radiobtn2Select(self):
#         if self.rbtn2.isChecked() == 1:
#             print('rbtn2 selected')
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
#
## Ex 5-5. QComboBox.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.lbl = QLabel('Option1', self)
#         self.lbl.move(50, 150)
#
#         cb = QComboBox(self)
#         cb.addItem('Option1')
#         cb.addItem('Option2')
#         cb.addItem('Option3')
#         cb.addItem('Option4')
#         cb.move(50, 50)
#
#         cb.activated[str].connect(self.onActivated)
#
#         self.setWindowTitle('QComboBox')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#     def onActivated(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

## Ex 5-7. QProgressBar.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
# from PyQt5.QtCore import QBasicTimer
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#
#         self.btn = QPushButton('Start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.timer = QBasicTimer()
#         self.step = 0
#
#         self.setWindowTitle('QProgressBar')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#     def timerEvent(self, e):
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#             return
#
#         self.step = self.step + 1
#         self.pbar.setValue(self.step)
#
#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# #digital clock
# from PyQt5.QtCore import QTime, QTimer
# from PyQt5.QtWidgets import QApplication, QLCDNumber
#
#
# class DigitalClock(QLCDNumber):
#     def __init__(self, parent=None):
#         super(DigitalClock, self).__init__(parent)
#
#         self.setSegmentStyle(QLCDNumber.Filled)
#         self.setDigitCount(8)
#         timer = QTimer(self)
#         timer.timeout.connect(self.showTime)
#         timer.start(100)
#
#         self.showTime()
#
#         self.setWindowTitle("Digital Clock")
#         self.resize(150, 60)
#
#     def showTime(self):
#         time = QTime.currentTime()
#         text = time.toString('hh:mm.ss')
#
#         if (time.msec() > 500 ) == 0:
#             text = text[:2] + ' ' + text[3:5] + '.' + text[6:]
#         #
#         # if (time.second() % 2) == 0:
#         #     text = text[:2] + ' ' + text[3:]
#
#         self.display(text)
#
#
# if __name__ == '__main__':
#
#     import sys
#
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())

##analog clock
#
# from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
# from PyQt5.QtGui import QColor, QPainter, QPolygon
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# class AnalogClock(QWidget):
#     hourHand = QPolygon([
#         QPoint(7, 8),
#         QPoint(-7, 8),
#         QPoint(0, -40)
#     ])
#
#     minuteHand = QPolygon([
#         QPoint(7, 8),
#         QPoint(-7, 8),
#         QPoint(0, -70)
#     ])
#
#     hourColor = QColor(127, 0, 127)
#     minuteColor = QColor(0, 127, 127, 191)
#
#     def __init__(self, parent=None):
#         super(AnalogClock, self).__init__(parent)
#
#         timer = QTimer(self)
#         timer.timeout.connect(self.update)
#         timer.start(1000)
#
#         self.setWindowTitle("Analog Clock")
#         self.resize(200, 200)
#
#     def paintEvent(self, event):
#         side = min(self.width(), self.height())
#         time = QTime.currentTime()
#
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.translate(self.width() / 2, self.height() / 2)
#         painter.scale(side / 200.0, side / 200.0)
#
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(AnalogClock.hourColor)
#
#         painter.save()
#         painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
#         painter.drawConvexPolygon(AnalogClock.hourHand)
#         painter.restore()
#
#         painter.setPen(AnalogClock.hourColor)
#
#         for i in range(12):
#             painter.drawLine(88, 0, 96, 0)
#             painter.rotate(30.0)
#
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(AnalogClock.minuteColor)
#
#         painter.save()
#         painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
#         painter.drawConvexPolygon(AnalogClock.minuteHand)
#         painter.restore()
#
#         painter.setPen(AnalogClock.minuteColor)
#
#         for j in range(60):
#             if (j % 5) != 0:
#                 painter.drawLine(92, 0, 96, 0)
#             painter.rotate(6.0)
#
#
# if __name__ == '__main__':
#
#     import sys
#
#     app = QApplication(sys.argv)
#     clock = AnalogClock()
#     clock.show()
#     sys.exit(app.exec_())























