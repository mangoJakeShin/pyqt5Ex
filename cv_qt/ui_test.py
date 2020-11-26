# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(755, 470)
        self.openFile = QPushButton(Form)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(30, 20, 141, 91))
        self.grayChk = QCheckBox(Form)
        self.grayChk.setObjectName(u"grayChk")
        self.grayChk.setGeometry(QRect(380, 30, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.grayChk.setFont(font)
        self.ivtChk = QCheckBox(Form)
        self.ivtChk.setObjectName(u"ivtChk")
        self.ivtChk.setGeometry(QRect(380, 70, 131, 41))
        self.ivtChk.setFont(font)
        self.applyBtn = QPushButton(Form)
        self.applyBtn.setObjectName(u"applyBtn")
        self.applyBtn.setGeometry(QRect(560, 20, 71, 91))
        self.orgImg = QLabel(Form)
        self.orgImg.setObjectName(u"orgImg")
        self.orgImg.setGeometry(QRect(40, 180, 341, 221))
        self.orgImg.setAlignment(Qt.AlignCenter)
        self.tgtImg = QLabel(Form)
        self.tgtImg.setObjectName(u"tgtImg")
        self.tgtImg.setGeometry(QRect(380, 180, 341, 221))
        self.tgtImg.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(220, 30, 112, 23))
        self.radioButton_2 = QRadioButton(Form)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(220, 60, 112, 23))
        self.radioButton_3 = QRadioButton(Form)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(220, 90, 112, 23))
        self.saveBtn = QPushButton(Form)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(640, 20, 71, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.openFile.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c \uc120\ud0dd", None))
        self.grayChk.setText(QCoreApplication.translate("Form", u"Gray Scale", None))
        self.ivtChk.setText(QCoreApplication.translate("Form", u"Invert", None))
        self.applyBtn.setText(QCoreApplication.translate("Form", u"\uc801\uc6a9", None))
        self.orgImg.setText(QCoreApplication.translate("Form", u"ORG IMAGE", None))
        self.tgtImg.setText(QCoreApplication.translate("Form", u"TARGET IMAGE", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Blur", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Shrpen", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"None", None))
        self.saveBtn.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
    # retranslateUi

