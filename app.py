import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer
from PyQt5.QtCore import QRunnable, QThreadPool
from database import database as db
from database import connected as connected_database
import login_layout
import register_layout
import notconnected_layout




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
    
    def switchToRegister(self) -> None:
        """Переключение между окнами"""
        self.switch_window.emit()




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




class NotConnectedApp(CommonApp, notconnected_layout.Ui_MainWindow):
    switch_window = pyqtSignal() # Сигнал

    """Окно register_layout"""
    def __init__(self, main_app, parent=None) -> None:
        super(NotConnectedApp, self).__init__(parent)
        self.setupUi(self)

        self.main_app = main_app

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
        self.ReloadButton.clicked.connect(self.reloadConnect)

    def reloadConnect(self) -> None:
        """Переключение между окнами"""
        self.main_app.check_database_connection_thread() 




class MainApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.login = LoginApp()
        self.register = RegisterApp()
        self.notconnected = NotConnectedApp(self)
    
        self.login.switch_window.connect(self.show_register)
        self.register.switch_window.connect(self.show_login)
       
        if connected_database():
            self.notconnected.switch_window.connect(self.show_login)
            self.login.show()
        else:
            self.notconnected.switch_window.connect(self.show_login)
            self.notconnected.show()

        self.check_database_timer = QTimer()
        self.check_database_timer.timeout.connect(self.check_database_connection_thread) 
        self.check_database_timer.start(5000)
        self.check_if_connected()
        
        

    """DATABASE"""

    def get_window(self):
        active_win = QApplication.activeWindow()
        if active_win is not None:
            class_name = active_win.metaObject().className()
            print(f"Class of active window: {class_name}")
        else:
            print("No active window")

    def check_if_connected(self):
        worker = Worker(self._check_initial_connection)
        QThreadPool.globalInstance().start(worker)
    
    def _check_initial_connection(self):
        if connected_database():
            self.login.show()
        else:
            self.notconnected.show()
    
    def check_database_connection_thread(self):
        worker = Worker(self.check_database_connection)
        QThreadPool.globalInstance().start(worker)

    def check_database_connection(self):
        try:
            self.get_window()
            if connected_database():
                if isinstance(self.activeWindow(), type(self.notconnected)):
                    self.show_login()
            else:
                if not isinstance(self.activeWindow(), type(self.notconnected)):
                    self.show_notconnected()
        except Exception as e:
            print(e)

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
    
    def show_notconnected(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.notconnected.move(window_pos)
        self.notconnected.show()
        self.login.close()

class Worker(QRunnable):
    def __init__(self, function):
        super(Worker, self).__init__()
        self.function = function

    def run(self):
        self.function()








if __name__ == "__main__":
    import sys
    app = MainApp(sys.argv)
    sys.exit(app.exec())

