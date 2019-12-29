from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from  PyQt5.QtWidgets import QToolTip
import sys

class Ui_Withdrawal(object):
    def setupUi(self, Form):
        Form.setObjectName("ATM Official Project")
        # Form.resize(400, 300)
        Form.setFixedSize(400,300)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 80, 331, 51))
        self.label.setObjectName("label")
        self.line_withDrawal = QtWidgets.QLineEdit(Form)
        self.line_withDrawal.setGeometry(QtCore.QRect(80, 150, 261, 41))
        self.line_withDrawal.setObjectName("line_withDrawal")
        self.line_withDrawal.setToolTip("Enter amount in multiple of 500 only")
        self.b_okWith = QtWidgets.QPushButton(Form)
        # self.b_done = QtWidgets.QPushButton(Form)
        self.b_okWith.setGeometry(QtCore.QRect(140, 210, 131, 41))
        self.b_okWith.setObjectName("b_okWith")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 381, 31))
        self.label_2.setGeometry(QtCore.QRect(10, 260, 381, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ATM Official Project"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">State Bank of Pakistan</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Enter amount to be Withdrawal</span></p></body></html>"))
        self.b_okWith.setText(_translate("Form", "Withdrawal"))
        self.b_okWith.clicked.connect(self.amt)
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#5c3566;\">Contact us in case of any issue at: easylife-coding.com</span></p></body></html>"))

    def withdrawal_warning(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        messageBox.exec_()
    def withdrawal_information(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Save)
        messageBox.exec_()

    def amt(self):
        txt = self.line_withDrawal.text()
        if txt.isdigit() == True and self.mult(txt) == True:
            txt = int(txt)
            a = self.mult(txt)
            self.withdrawal_information("Success!!!","You've successfully withdrawal amount. You will shortly receive confirmation message.")
        else:
            self.withdrawal_warning("ValueError", "You have entered wrong amount. Please enter correct amount")

    def mult(self,x):
        x = int(x)
        if x%500==0:
            return True
        else:
            return False
