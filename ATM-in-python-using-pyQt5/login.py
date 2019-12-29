import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Data.welcome import *
from Data.newAccount import *
from Data.deposite import *
from Data.userData import *

# Dialog <--- QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("ATM OFFICAL PROJECT") # we've set the title of window
        # Dialog.resize(400, 300)
        Dialog.setFixedSize(400,300) # we've fixed the size of window
        # Dialog.setStyleSheet("") 
        self.lb_cardNo = QtWidgets.QLabel(Dialog)
        self.lb_cardNo.setGeometry(QtCore.QRect(90, 70, 66, 17)) # this is built-in class for positioning
        # self.lb_cardNo.setTextFormat(QtCore.Qt.PlainText) # this will set the format of label
        icon = QtGui.QIcon()  # We're object for icon
        icon.addPixmap(QtGui.QPixmap("../../atm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # this is adding the icon
        Dialog.setWindowIcon(icon) # Finally set icon to main window
        
        # self.lb_cardNo.setObjectName("lb_cardNo")
        self.lb_pin = QtWidgets.QLabel(Dialog) # It will create a label of userpin/ object of label
        self.lb_pin.setGeometry(QtCore.QRect(80, 110, 81, 16))
        # self.lb_pin.setGeometry(QtCore.QRect(200, 10, 81, 16))
        # self.lb_pin.setObjectName("lb_pin")
        self.line_cardNo = QtWidgets.QLineEdit(Dialog)
        self.line_cardNo.setGeometry(QtCore.QRect(180, 70, 113, 27))
        # self.line_cardNo.setObjectName("line_cardNo")
        self.line_pin = QtWidgets.QLineEdit(Dialog) # It will create a Line Edit/ object of lineEdit
        self.line_pin.setGeometry(QtCore.QRect(180, 110, 113, 27))
        # self.line_pin.setObjectName("line_pin")
        self.b_new = QtWidgets.QPushButton(Dialog) # It will create a button/object of button
        self.b_new.setGeometry(QtCore.QRect(240, 160, 111, 27)) # It will set the position
        # self.b_new.setObjectName("b_new")
        self.b_login = QtWidgets.QPushButton(Dialog)
        self.b_login.setGeometry(QtCore.QRect(110, 160, 111, 27))
        # self.b_login.setCheckable(False)
        # self.b_login.setFlat(True)
        # self.b_login.setObjectName("b_login")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 200, 211, 27)) # It is Exit button
        # self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 31)) ####kk
        # self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 301, 31))
        # self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 331, 31))
        # self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog) # It is the other method/function
        QtCore.QMetaObject.connectSlotsByName(Dialog) # It will connect the both of function

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate # It will rename all the button, label and lineEdit
        Dialog.setWindowTitle(_translate("Dialog", "ATM Official Project"))
        # Dialog.setWhatsThis(_translate("Dialog", "ATM Project"))
        self.lb_cardNo.setText(_translate("Dialog", "   Name")) # It will set the name of label/ username
        self.lb_pin.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">PIN Code</p></body></html>"))
        self.line_cardNo.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter Card No, given by the bank</span></p></body></html>"))
        self.line_pin.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Enter 4-Digin PIN</p></body></html>"))
        self.b_new.setToolTip(_translate("Dialog", "<html><head/><body><p>Contact the Bank in order to be part of State Bank of Pakistan</p></body></html>"))
        self.b_new.setText(_translate("Dialog", "Create Account"))
        self.b_login.setText(_translate("Dialog", "Login"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))
        #### We've set all the names of labels, button and line
        
        ## Here' We've connected the function with the buttons #####
        self.b_login.clicked.connect(self.loginCheck)
        self.b_new.clicked.connect(self.newAccount) # When butthon will clicked, newAccount function will run
        self.pushButton_3.clicked.connect(self.exit)
        ## Here' We've connected the function with the buttons #####
        
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to State Bank of Pakistan</span></p></body></html>"))
        # self.label.setText(_translate("Dialog","Welcome to State Bank of Pakistan"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">A Project prepared by the team --&gt; DareDevils Please be patience as we\'re updating our ATM regularly.</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ahmed Arshad , Saood , Hasnain Kazmi</span></p></body></html>"))
        self.label_3.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Please report any issue to the email. Don\'t call at peak times</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#2e3436;\">Manager: P17-6133@nu.edu.pk , +923464646629</span></p></body></html>"))
    def newAccount(self):
        self.newAccountWindow = QtWidgets.QMainWindow() # built-in class's object
        self.newAccountObject = Ui_newAccount() # user defined class's object
        self.newAccountObject.setupUi(self.newAccountWindow)
        self.newAccountWindow.show()
    def userWelcome(self):
        self.welcomeWindow = QtWidgets.QMainWindow() # We've create an object of mainwindow
        self.ui = Ui_MainWindow() # user defined class's object
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
    def messageFailure(self,title,message):
        messageBox = QtWidgets.QMessageBox() # this is a object
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        messageBox.exec_()

    ### authenticate use and pin
    # It will be called by login button as well
    def loginCheck(self):
        username = self.line_cardNo.text()
        pin  = self.line_pin.text()
        d = data() # It is placed in useData file.
        if username in d.keys() and pin in d[username]:
            print("Access Granted:")
            self.userWelcome()
        else:
            self.messageFailure("Access Not Granted","Contact bank in case of forgot PIN")

    def message_createAccount(self):
        messageBox = QtWidgets.QMessageBox() # object of message box
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.setWindowTitle("Contact Bank")
        messageBox.setText("Please contact bank for activating new account or visit bank website\nwww.easylife-coding.com")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Abort)
        messageBox.exec_()
    def exit(self):
        print("GoodBye")
        sys.exit()

 # def createNew(self):
 #        newUser = self.line_username.text()
 #        newPin = self.line_pin.text()
 #        directory = '/atm/Data'
 #        filename = 'usersdata.csv'
 #        with open(filename,'a') as f:
 #            writer = csv.writer(f)
 #            writer.writerow((newUser,newPin,0))
 #            f.close()
 #        print("Account successfully activated.")
 #        



app = QtWidgets.QApplication(sys.argv) # one applicationn is created here
Dialog = QtWidgets.QDialog() # pyqt built-in class , object
ui = Ui_Dialog() # user defined classs, object
ui.setupUi(Dialog) # built-in object passed in user defined class method
Dialog.show() # built-in object of Graphics --> to display
sys.exit(app.exec_()) # this is just like a loop
