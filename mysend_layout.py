# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mysend-layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 504)
        self.MainBackground = QtWidgets.QFrame(MainWindow)
        self.MainBackground.setEnabled(True)
        self.MainBackground.setGeometry(QtCore.QRect(20, 10, 571, 441))
        self.MainBackground.setStyleSheet("QFrame {\n"
"    height:100%; margin:0;\n"
"    background-color: #ca3767;\n"
"    border-radius: 30px;\n"
"}")
        self.MainBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBackground.setObjectName("MainBackground")
        self.MainFrame_2 = QtWidgets.QFrame(self.MainBackground)
        self.MainFrame_2.setEnabled(True)
        self.MainFrame_2.setGeometry(QtCore.QRect(510, 0, 61, 441))
        self.MainFrame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MainFrame_2.setMouseTracking(False)
        self.MainFrame_2.setTabletTracking(False)
        self.MainFrame_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MainFrame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.MainFrame_2.setAcceptDrops(False)
        self.MainFrame_2.setStyleSheet("QFrame {\n"
"    border: 0;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 30px; \n"
"}")
        self.MainFrame_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.MainFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame_2.setObjectName("MainFrame_2")
        self.LogoType = QtWidgets.QFrame(self.MainBackground)
        self.LogoType.setGeometry(QtCore.QRect(10, 390, 31, 31))
        self.LogoType.setStyleSheet("QFrame {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/appIcon.png);\n"
"}")
        self.LogoType.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoType.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoType.setObjectName("LogoType")
        self.TextLogoType = QtWidgets.QLabel(self.MainBackground)
        self.TextLogoType.setGeometry(QtCore.QRect(47, 395, 101, 21))
        self.TextLogoType.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: white;\n"
"    font: 500 12pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.TextLogoType.setObjectName("TextLogoType")
        self.MainFrame = QtWidgets.QFrame(self.MainBackground)
        self.MainFrame.setEnabled(True)
        self.MainFrame.setGeometry(QtCore.QRect(150, 0, 391, 481))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border: 0;\n"
"    border-radius: 0;\n"
"}")
        self.MainFrame.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.MainFrame.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.title = QtWidgets.QLabel(self.MainFrame)
        self.title.setGeometry(QtCore.QRect(23, 17, 191, 31))
        self.title.setStyleSheet("QFrame {\n"
"    background-color: 0;\n"
"    color: #ca3767;\n"
"    font: 500 16pt \"Montserrat Medium\";    \n"
"}\n"
"")
        self.title.setObjectName("title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 0, 51, 31))
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
        self.tabWidget = QtWidgets.QTabWidget(self.MainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(19, 51, 371, 391))
        self.tabWidget.setStyleSheet("* {\n"
"    background-color: white;\n"
"    border: 0;\n"
"    margin: 0;\n"
"    color: black;\n"
"    width: 170px;\n"
"    height: 30px;\n"
"    font: 7pt \"Montserrat\";\n"
"}\n"
"\n"
"*::tab {\n"
"    color: white;\n"
"    background-color: rgb(202, 55, 103);\n"
"    width: 170px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"*::tab:selected {\n"
"    background-color: rgb(249, 67, 128);\n"
"    border: 1px solid black;\n"
"    width: 170px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"*::tab:hover {\n"
"    background-color: rgb(202, 55, 138);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.MainBackground)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 151, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.HomeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.HomeButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 0;\n"
"    height: 40;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"")
        self.HomeButton.setObjectName("HomeButton")
        self.verticalLayout.addWidget(self.HomeButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.MySend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MySend.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: white;\n"
"    height: 40;\n"
"    border: 0;\n"
"}\n"
"")
        self.MySend.setObjectName("MySend")
        self.verticalLayout.addWidget(self.MySend)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.SettingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SettingButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border: 0;\n"
"    height: 40;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"")
        self.SettingButton.setObjectName("SettingButton")
        self.verticalLayout.addWidget(self.SettingButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
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
        self.TextLogoType.setText(_translate("MainWindow", "КлиникБук"))
        self.title.setText(_translate("MainWindow", "Мои записи"))
        self.rubutton_2.setText(_translate("MainWindow", "EN"))
        self.rubutton.setText(_translate("MainWindow", "RU"))
        self.HomeButton.setText(_translate("MainWindow", "Главная"))
        self.MySend.setText(_translate("MainWindow", "Мои записи"))
        self.SettingButton.setText(_translate("MainWindow", "Настройки"))
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
