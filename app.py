import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer
from PyQt5.QtCore import QRunnable, QThreadPool
from database import database as db
from database import connected as connected_database
import login_layout
import register_layout


from PyQt5.QtCore import QMetaObject


class CommonApp(QWidget):
    switch_window = pyqtSignal()   # Signal

    def __init__(self, parent=None) -> None:
        super(CommonApp, self).__init__(parent)
        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def hideWindow(self) -> None:
        """To minimize the window"""
        self.showMinimized()

    def closeWindow(self) -> None:
        """To close the window"""
        self.close()

    def mousePressEvent(self, event):
        """When the mouse is pressed on the layers"""
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """When the mouse is moving"""
        if event.buttons() and Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)  # moving the window with the mouse
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False




class LoginApp(CommonApp, login_layout.Ui_MainWindow):
    switch_window = pyqtSignal() # Сигнал

    """Главное меню login_layout"""
    def __init__(self, parent=None) -> None:
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.connected()
    
    def connected(self) -> None:
        """Подключение кнопок"""
        self.RegisterButton.clicked.connect(self.switchToRegister)
        
        self.GetUserName.textChanged.connect(self.getTextUser)
        self.GetPassword.textChanged.connect(self.getTextPassword)
        self.AgreeCond.toggled.connect(self.checkBoxChecked)

        self.SignUpButton.setDisabled(True)

        self.user_text: bool = False
        self.password_text: bool = False
        self.check_box_status: bool = False

        self.button_enable() # Проверка состояния полей и флажка при запуске приложения
        self.SignUpButton.setEnabled(False)
    
    def switchToRegister(self) -> None:
        """Переключение между окнами"""
        self.switch_window.emit()
    
    def button_enable(self) -> None:
        """Проверка на поля(выключение кнопки)"""
        if len(self.GetUserName.text()) >= 2 and len(self.GetPassword.text()) >= 7 and self.AgreeCond.isChecked():
            self.SignUpButton.setEnabled(True)
        else:
            self.SignUpButton.setEnabled(False)

    def getTextUser(self, text) -> None:
        """Что ввёл пользователь в поле User Name?"""
        self.user_text = bool(text)
        self.button_enable()

    def getTextPassword(self, text) -> None:
        """Что ввёл пользователь в поле Password?"""
        self.password_text = bool(text)
        self.button_enable()
    
    def checkBoxChecked(self, state):
        """Что ввёл пользователь в поле CheckBox?"""
        if state:
            self.check_box_status = True
        else:
            self.check_box_status = False
        self.button_enable()




class RegisterApp(CommonApp, register_layout.Ui_MainWindow):
    switch_window = pyqtSignal() # Сигнал

    """Окно register_layout"""
    def __init__(self, parent=None) -> None:
        super(RegisterApp, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.connected()

    def connected(self) -> None:
        """Подключение кнопок"""
        self.SignUpButton.clicked.connect(self.switchToLogin)

    def switchToLogin(self) -> None:
        """Переключение между окнами"""
        self.switch_window.emit()


class MainApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.login = LoginApp()
        self.register = RegisterApp()
    
        self.login.switch_window.connect(self.show_register)
        self.register.switch_window.connect(self.show_login)
       
        self.login.show()
        
    """---------------"""

    def get_position(self):
        """Get the position of the currently active window"""
        if self.activeWindow() is not None:
            return self.activeWindow().pos()
        else:
            return QtCore.QPoint(0, 0)


    def show_register(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.register.move(window_pos)
        self.register.show()
        self.login.close()
        
    def show_login(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.login.move(window_pos)
        self.login.show()
        self.register.close()








if __name__ == "__main__":
    import sys
    app = MainApp(sys.argv)
    sys.exit(app.exec())

