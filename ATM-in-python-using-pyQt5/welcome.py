
from PyQt5 import QtCore, QtGui, QtWidgets
from Data.deposite import *
from Data.withdrawal import *
from Data.transfer import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(572,395)
 

        self.centralwidget = QtWidgets.QWidget(MainWindow) # Here' we created a object
        
        self.b_withdrawal = QtWidgets.QPushButton(self.centralwidget)  # here, withdrawal button is created
        self.b_withdrawal.setGeometry(QtCore.QRect(60, 120, 159, 41)) # here its position is defined
        self.b_mini = QtWidgets.QPushButton(self.centralwidget) # here miniStatement button is created
        self.b_mini.setGeometry(QtCore.QRect(60, 190, 159, 41)) # here its positions is defined
        self.b_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.b_transfer.setGeometry(QtCore.QRect(60, 270, 159, 41))
        self.b_balance = QtWidgets.QPushButton(self.centralwidget)
        self.b_balance.setGeometry(QtCore.QRect(390, 190, 149, 41))
        self.b_deposite = QtWidgets.QPushButton(self.centralwidget)
        self.b_deposite.setGeometry(QtCore.QRect(390, 120, 149, 40))
        self.b_other = QtWidgets.QPushButton(self.centralwidget)
        self.b_other.setGeometry(QtCore.QRect(390, 270, 149, 41))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 421, 41))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 211, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) # it will connect and tranlate the functions/names

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sala from Kasur"))
        self.b_withdrawal.setText(_translate("MainWindow", "Withdrawal"))
        self.b_withdrawal.clicked.connect(self.withdrawal_amt)
        self.b_mini.setText(_translate("MainWindow", "Mini Statement"))
        self.b_mini.clicked.connect(self.message_mini)
        self.b_transfer.setText(_translate("MainWindow", "Transfer"))
        self.b_balance.setText(_translate("MainWindow", "Balance"))
        self.b_balance.clicked.connect(self.message_balance)
        self.b_deposite.setText(_translate("MainWindow", "Deposit"))
        self.b_deposite.clicked.connect(self.deposite_amt) # It will connect the button 
        self.b_transfer.clicked.connect(self.transfer_amt)
        self.b_other.setText(_translate("MainWindow", "Other"))
        self.b_other.clicked.connect(self.message_other)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to State Bank of Pakistan</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Select Transcation</span></p></body></html>"))


    def deposite_amt(self):
        self.depositeWindow = QtWidgets.QMainWindow()
        self.ud = Ui_Deposite()
        self.ud.setupUi(self.depositeWindow)
        self.depositeWindow.show()
    # this method for checking balance as well
    def balance_info(self):
        self.balanceWindow = QtWidgets.QDialog()
        self.bu = Ui_confirm()
        self.bu.setupUi(self.balanceWindow)
        self.balanceWindow.show()
    def withdrawal_amt(self):
        self.withdrawal = QtWidgets.QMainWindow()
        self.wd=Ui_Withdrawal() # object of withdrawal class
        self.wd.setupUi(self.withdrawal)
        self.withdrawal.show()

    def transfer_amt(self):
        self.transfer = QtWidgets.QMainWindow()
        self.td = Ui_Transfer()
        self.td.setupUi(self.transfer)
        self.transfer.show()

    def message_balance(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Success!!!")
        messageBox.setText("Your request for checking balance is received. You will shortly receive info through your registered email/phone")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()
    
    def message_mini(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Success!!!")
        messageBox.setText("Your request for Mini-Statement is received. You will shortly receive info through your registered email/phone")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Save)
        messageBox.exec_()

    def message_other(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Question)
        messageBox.setWindowTitle("Suggest ideas")
        messageBox.setText("Please feel free to email us what should be else consisted in the project\nwww.easylife-coding.com")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()
