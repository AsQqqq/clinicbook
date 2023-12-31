# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 479)
        self.MainBackground = QtWidgets.QFrame(MainWindow)
        self.MainBackground.setEnabled(True)
        self.MainBackground.setGeometry(QtCore.QRect(20, 10, 571, 441))
        font = QtGui.QFont()
        font.setBold(False)
        self.MainBackground.setFont(font)
        self.MainBackground.setStyleSheet("QFrame {\n"
"    height:100%; margin:0;\n"
"    background-color: #ca3767;\n"
"    border-radius: 30px;\n"
"}")
        self.MainBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBackground.setObjectName("MainBackground")
        self.WhiteColor = QtWidgets.QFrame(self.MainBackground)
        self.WhiteColor.setEnabled(True)
        self.WhiteColor.setGeometry(QtCore.QRect(260, 0, 311, 441))
        self.WhiteColor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.WhiteColor.setMouseTracking(False)
        self.WhiteColor.setTabletTracking(False)
        self.WhiteColor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.WhiteColor.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.WhiteColor.setAcceptDrops(False)
        self.WhiteColor.setStyleSheet("QFrame {\n"
"    border: 0;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 30px; \n"
"}")
        self.WhiteColor.setInputMethodHints(QtCore.Qt.ImhNone)
        self.WhiteColor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.WhiteColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WhiteColor.setObjectName("WhiteColor")
        self.frame = QtWidgets.QFrame(self.WhiteColor)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, -10, 281, 481))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border: 0;\n"
"    border-radius: 0;\n"
"}")
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.frame.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SIGNUP = QtWidgets.QLabel(self.frame)
        self.SIGNUP.setGeometry(QtCore.QRect(18, 30, 201, 31))
        self.SIGNUP.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    font: 500 16pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.SIGNUP.setObjectName("SIGNUP")
        self.UserName = QtWidgets.QLabel(self.frame)
        self.UserName.setGeometry(QtCore.QRect(19, 80, 131, 21))
        self.UserName.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    font: 500 9pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLabel(self.frame)
        self.Password.setGeometry(QtCore.QRect(20, 160, 151, 21))
        self.Password.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    font: 500 9pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.Password.setObjectName("Password")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(15, 123, 190, 3))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("QFrame {\n"
"    background-color: #ca3767;\n"
"}\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(16, 204, 190, 3))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet("QFrame {\n"
"    background-color: #ca3767;\n"
"}\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.GetPassword = QtWidgets.QLineEdit(self.frame)
        self.GetPassword.setGeometry(QtCore.QRect(20, 180, 181, 22))
        self.GetPassword.setTabletTracking(False)
        self.GetPassword.setAutoFillBackground(False)
        self.GetPassword.setStyleSheet("QLineEdit {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    border: 0;\n"
"    font: 500 9pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.GetPassword.setInputMask("")
        self.GetPassword.setMaxLength(20)
        self.GetPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.GetPassword.setCursorPosition(0)
        self.GetPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GetPassword.setDragEnabled(False)
        self.GetPassword.setReadOnly(False)
        self.GetPassword.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.GetPassword.setClearButtonEnabled(False)
        self.GetPassword.setObjectName("GetPassword")
        self.GetUserName = QtWidgets.QLineEdit(self.frame)
        self.GetUserName.setGeometry(QtCore.QRect(20, 100, 181, 22))
        self.GetUserName.setTabletTracking(False)
        self.GetUserName.setAutoFillBackground(False)
        self.GetUserName.setStyleSheet("QLineEdit {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    border: 0;\n"
"    font: 500 9pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.GetUserName.setInputMask("")
        self.GetUserName.setMaxLength(10)
        self.GetUserName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.GetUserName.setCursorPosition(0)
        self.GetUserName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GetUserName.setDragEnabled(False)
        self.GetUserName.setReadOnly(False)
        self.GetUserName.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.GetUserName.setClearButtonEnabled(False)
        self.GetUserName.setObjectName("GetUserName")
        self.SignUpButton = QtWidgets.QPushButton(self.frame)
        self.SignUpButton.setEnabled(False)
        self.SignUpButton.setGeometry(QtCore.QRect(10, 240, 251, 24))
        self.SignUpButton.setStyleSheet("QPushButton {\n"
"    background-color: #ca3767;\n"
"    color: white;\n"
"    border: 0;\n"
"    font: 500 10pt \"Montserrat Medium\";    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CA378A;\n"
"}\n"
"\n"
"QPushButton:disabled,\n"
"QPushButton[disabled]{\n"
"  background-color: #c298a6;\n"
"  color: white;\n"
"}\n"
"")
        self.SignUpButton.setObjectName("SignUpButton")
        self.RegisterButton = QtWidgets.QPushButton(self.frame)
        self.RegisterButton.setGeometry(QtCore.QRect(10, 280, 251, 24))
        self.RegisterButton.setStyleSheet("QPushButton {\n"
"    background-color: #ca3767;\n"
"    color: white;\n"
"    border: 0;\n"
"    font: 500 10pt \"Montserrat Medium\";    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CA378A;\n"
"}\n"
"")
        self.RegisterButton.setObjectName("RegisterButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 10, 51, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rubutton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rubutton_2.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    color: #ca3767;\n"
"    font: 9pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CA378A;\n"
"    border-radius: 2px;\n"
"    color: white;\n"
"}")
        self.rubutton_2.setObjectName("rubutton_2")
        self.horizontalLayout.addWidget(self.rubutton_2)
        self.rubutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rubutton.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    color: #ca3767;\n"
"    font: 9pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CA378A;\n"
"    border-radius: 2px;\n"
"    color: white;\n"
"}")
        self.rubutton.setObjectName("rubutton")
        self.horizontalLayout.addWidget(self.rubutton)
        self.line.raise_()
        self.SIGNUP.raise_()
        self.UserName.raise_()
        self.Password.raise_()
        self.line_2.raise_()
        self.GetPassword.raise_()
        self.GetUserName.raise_()
        self.SignUpButton.raise_()
        self.RegisterButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.frame_2 = QtWidgets.QFrame(self.MainBackground)
        self.frame_2.setGeometry(QtCore.QRect(55, 96, 151, 171))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/appIcon.png);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ClinicBook = QtWidgets.QLabel(self.MainBackground)
        self.ClinicBook.setGeometry(QtCore.QRect(23, 246, 221, 81))
        self.ClinicBook.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: white;\n"
"    font: 500 28pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.ClinicBook.setObjectName("ClinicBook")
        self.CloseProgram = QtWidgets.QPushButton(self.MainBackground)
        self.CloseProgram.setGeometry(QtCore.QRect(25, 1, 31, 31))
        self.CloseProgram.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    color: white;\n"
"    font: 15pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius: 7px;\n"
"    background-color: #a85973;\n"
"}\n"
"")
        self.CloseProgram.setObjectName("CloseProgram")
        self.HideProgram = QtWidgets.QPushButton(self.MainBackground)
        self.HideProgram.setGeometry(QtCore.QRect(60, 1, 31, 31))
        self.HideProgram.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.HideProgram.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.HideProgram.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    color: white;\n"
"    font: 900 15pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius: 7px;\n"
"    background-color: #a85973;\n"
"}")
        self.HideProgram.setCheckable(False)
        self.HideProgram.setChecked(False)
        self.HideProgram.setAutoRepeat(False)
        self.HideProgram.setAutoExclusive(False)
        self.HideProgram.setAutoDefault(False)
        self.HideProgram.setObjectName("HideProgram")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.SIGNUP.setText(_translate("MainWindow", "Sign Up"))
        self.UserName.setText(_translate("MainWindow", "User Name:"))
        self.Password.setText(_translate("MainWindow", "Password:"))
        self.GetPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.GetUserName.setPlaceholderText(_translate("MainWindow", "User name"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.RegisterButton.setText(_translate("MainWindow", "Register"))
        self.rubutton_2.setText(_translate("MainWindow", "EN"))
        self.rubutton.setText(_translate("MainWindow", "RU"))
        self.ClinicBook.setText(_translate("MainWindow", "КлиникБук"))
        self.CloseProgram.setText(_translate("MainWindow", "🞬"))
        self.HideProgram.setText(_translate("MainWindow", "–"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
