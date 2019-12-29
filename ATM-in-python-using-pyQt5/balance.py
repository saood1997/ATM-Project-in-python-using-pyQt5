
amt = '1000'
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Balance(object):
    amt = 10000
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(400, 300)
        Dialog.setFixedSize(400,300)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../atm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 251, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 120, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(amt)
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ATM official Project"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#3465a4;\">Your current amount is</span></p></body></html>"))
    