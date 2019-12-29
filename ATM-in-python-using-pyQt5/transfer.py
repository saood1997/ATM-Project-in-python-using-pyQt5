# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from  PyQt5.QtWidgets import QToolTip
import sys


class Ui_Transfer(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(400, 300)
        Form.setFixedSize(400,300) 
        self.line_withDrawal = QtWidgets.QLineEdit(Form)
        self.line_withDrawal.setGeometry(QtCore.QRect(80, 140, 261, 41))
        self.line_withDrawal.setStyleSheet("background-color:rgb(186, 189, 182)")
        self.line_withDrawal.setText("")
        self.line_withDrawal.setObjectName("line_withDrawal")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 361, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 381, 31))
        self.label_2.setObjectName("label_2")
        self.b_okWith = QtWidgets.QPushButton(Form)
        self.b_okWith.setGeometry(QtCore.QRect(140, 200, 121, 41))
        self.b_okWith.setObjectName("b_okWith")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 331, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ATM Official Project"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">State Bank of Pakistan</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#5c3566;\">Contact us in case of any issue at: easylife-coding.com</span></p></body></html>"))
        self.b_okWith.setText(_translate("Form", "Transfer"))
        self.b_okWith.clicked.connect(self.amt)
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Enter amount to be Transfer</span></p></body></html>"))



    def tranfser_warning(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        messageBox.exec_()
    def transfer_information(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Save)
        messageBox.exec_()
    def amt(self):
        txt = self.line_withDrawal.text()
        if txt.isdigit() == True:
            # txt = float(txt)
            self.transfer_information("Success!!!","Your amount was added, You will shortly receive confirmation message")
        else:
            self.tranfser_warning("ValueError","Enter some handsome amount")
