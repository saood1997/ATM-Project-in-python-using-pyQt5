
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Deposite(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(400, 300)
        Dialog.setFixedSize(400,300)
        # Dialog.setStyleSheet("background-color:rgb(238, 238, 236)")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 261, 31))

        self.line_amount = QtWidgets.QLineEdit(Dialog)
        self.line_amount.setGeometry(QtCore.QRect(90, 150, 261, 41))
        # self.line_amount.setStyleSheet("background-color:rgb(186, 189, 182)")
        # self.line_amount.setObjectName("line_amount")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 80, 331, 51))
        # self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 361, 31))
        # self.label_3.setObjectName("label_3")
        self.b_okAmt = QtWidgets.QPushButton(Dialog)
        self.b_okAmt.setGeometry(QtCore.QRect(150, 210, 131, 41))
        # self.b_okAmt.setObjectName("b_okAmt")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 381, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ATM Official Project"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Enter amount to be deposited</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">State Bank of Pakistan</span></p></body></html>"))
        self.b_okAmt.setText(_translate("Dialog", "Deposit"))

        self.b_okAmt.clicked.connect(self.amt)
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#5c3566;\">In case of any issue/query Contact us</span></p></body></html>"))



    def amount_warning(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        messageBox.exec_()
    def amount_information(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Save)
        messageBox.exec_()
    def amt(self):
        txt = self.line_amount.text()
        if txt.isdigit() == True:
            # txt = float(txt)
            self.amount_information("Success!!!","Your amount was added, You will shortly receive confirmation message")
        else:
            self.amount_warning("ValueError","Enter some handsome amount")
