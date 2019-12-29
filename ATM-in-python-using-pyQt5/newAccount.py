# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newAccount.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
class Ui_newAccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400,300)
        self.line_pin = QtWidgets.QLineEdit(Dialog)
        self.line_pin.setGeometry(QtCore.QRect(210, 110, 113, 25))
        self.line_pin.setObjectName("line_pin")
        self.line_username = QtWidgets.QLineEdit(Dialog)
        self.line_username.setGeometry(QtCore.QRect(210, 70, 113, 25))
        self.line_username.setObjectName("line_username")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 331, 31))
        self.label_3.setObjectName("label_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(110, 230, 177, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 111, 31))
        self.label.setObjectName("label")
        self.b_create = QtWidgets.QPushButton(Dialog)
        self.b_create.setGeometry(QtCore.QRect(230, 160, 111, 31))
        self.b_create.setObjectName("b_create")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 131, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 351, 31))
        self.label_5.setObjectName("label_5")
        self.b_create_2 = QtWidgets.QPushButton(Dialog)
        self.b_create_2.setGeometry(QtCore.QRect(110, 160, 111, 31))
        self.b_create_2.setObjectName("b_create_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#2e3436;\">Contact us in case of any Qurary</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Dialog", "www.easylife-coding.com"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">PIN code</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Username</span></p></body></html>"))
        self.b_create.setText(_translate("Dialog", "Create Account"))
        self.b_create.clicked.connect(self.createNew)
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#555753;\">20, May 2018</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#555753;\">Welcome to State Bank of Pakistan</span></p></body></html>"))
        self.b_create_2.setText(_translate("Dialog", "Help"))
        self.b_create_2.clicked.connect(self.showHelp)

    def createNew(self):
           newUser = self.line_username.text()
           newPin = self.line_pin.text()
           with open('Data/usersdata.csv','a') as f:
               writer = csv.writer(f)
               writer.writerow((newUser,newPin,0))
               f.close()
           print("Account successfully activated.")
           
    def showHelp(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Help")
        messageBox.setText("If you are having problems in creating new account, you can get help online at www.easylife-conding.com or you can contact our agent by 24/7.")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()
        
        