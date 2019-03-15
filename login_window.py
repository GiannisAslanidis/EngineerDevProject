
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import re


class Ui_Login(object):
    def messagebox(self,title,message):
        
        mess=QtWidgets.QMessageBox()
        
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def warning(self,title,message):
        
        mess=QtWidgets.QMessageBox()
        
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")
        mess.exec_()
        
    def checkemail(self,email):
        pattern=r'[\w.-]+@[\w.-]+\.\w{2,6}?'
        match=re.search(pattern,email)
        
        if match:
            return True
        else:
            return False
        
    def checknames(self,nametext):
        pattern=r'^[A-z]+(?=[a-z]*)([a-z]$)'
        match=re.search(pattern,nametext)
        
        if match:
            return True
        else:
            return False
    
    def checklogin(self,usernametext):
        pattern=r'^[a-zA-z0-9]+(?=[a-zA-z0-9]+)([a-zA-z0-9]$)'
        match=re.search(pattern,usernametext)
        
        if match:
            return True
        else:
            return False
    
    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        conn=pymysql.connect(host="localhost",user="root",password="",database="my_database")
        cur=conn.cursor()
        query="select * from users_info where username=%s and password=%s"
        data=cur.execute(query,(username,password))
        
        if(len(cur.fetchall())>0):
           self.messagebox("Success","You are now logged in!")
        else:
           self.warning("Failed to Connect","Please check your credentials: Invalid Username or Password.")
        
    def signup(self):
        username=self.lineEdit_3.text()
        password=self.lineEdit_4.text()
        email=self.lineEdit_5.text()
        phone_number=self.lineEdit_6.text()
        first_name=self.lineEdit_7.text()
        last_name=self.lineEdit_8.text()
        
        if (username=="" or password=="" or email=="" or phone_number=="" or first_name=="" or last_name==""):
            self.warning("Failed to Sign up","Please check your credentials: Empty Fields.")
        elif(self.checklogin(username)==False):
            self.warning("Failed to Sign up","Please check your credentials: Invalid Username Format.")
        elif(self.checklogin(password)==False):
             self.warning("Failed to Sign up","Please check your credentials: Invalid Password Format.")
        elif(self.checkemail(email)==False):
            self.warning("Failed to Sign up","Please check your credentials: Invalid Email Format.")
        elif (phone_number.isdigit()==False or len(phone_number)<10):
            self.warning("Failed to Sign up","Please check your credentials: Invalid Phone Number.")
        elif(self.checknames(first_name)==False):
            self.warning("Failed to Sign up","Please check your credentials: Invalid First Name.")
        elif(self.checknames(last_name)==False): 
            self.warning("Failed to Sign up","Please check your credentials: Invalid Last Name.")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",database="my_database")
            cur=conn.cursor()
            query="insert into users_info(Username,Password,Email,Phone_Number,First_Name,Last_Name)" \
                  "values (%s,%s,%s,%s,%s,%s)"
            idquery1="ALTER TABLE users_info DROP id"
            idquery2="ALTER TABLE  `users_info` ADD `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST"
            data=cur.execute(query,(username,password,email,phone_number,first_name,last_name))
            idfix=cur.execute(idquery1)
            idfix=cur.execute(idquery2)
            conn.commit()
            if (data):
                self.messagebox("Success","You are now signed up!")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")
                self.lineEdit_7.setText("")
                self.lineEdit_8.setText("")
    
    
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setToolTipDuration(-5)
        Login.setAutoFillBackground(False)
        Login.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 240, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 290, 111, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 350, 81, 31))
        self.pushButton.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 601, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 180, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 240, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 320, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 360, 131, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(410, 400, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(410, 440, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 500, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signup)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 240, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(590, 280, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(590, 320, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(590, 360, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(590, 400, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(590, 440, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Username:"))
        self.label_2.setText(_translate("Login", "Password:"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Διαχείριση Υλικού Χώρων Εκπαιδευτικού Ιδρύματος"))
        self.label_4.setText(_translate("Login", "Παρακαλώ εισάγετε τα στοιχεία σας στα παρακάτω πεδία."))
        self.label_5.setText(_translate("Login", "Εαν δεν έχετε λογαριασμό,πραγματοποιήστε εγγραφή."))
        self.label_6.setText(_translate("Login", "Username:"))
        self.label_7.setText(_translate("Login", "Password:"))
        self.label_8.setText(_translate("Login", "Email:"))
        self.label_9.setText(_translate("Login", "Phone Number:"))
        self.label_10.setText(_translate("Login", "First Name:"))
        self.label_11.setText(_translate("Login", "Last Name:"))
        self.pushButton_2.setText(_translate("Login", "Sign up"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())




