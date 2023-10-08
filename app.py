from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget, QVBoxLayout, QListWidget, QListWidgetItem

from database import database as db
from database import LocalDatabase as ldb
# from database import connected as connected_database

import login_layout
import register_layout
import main_layout
import setting_layout
import mysend_layout

agent_url = 'http://31.129.111.98/assets'

import json

def loadTranslations():
    translations = {}

    with open('language/ru_RU.json','r', encoding='utf-8') as f:
        translations['ru_RU'] = json.load(f)

    with open('language/en_US.json','r', encoding='utf-8') as f:
        translations['en_US'] = json.load(f)

    return translations


class CommonApp(QWidget):
    change_language = pyqtSignal(str)
    switch_window = pyqtSignal()   # Signal

    def __init__(self, parent=None) -> None:
        super(CommonApp, self).__init__(parent)
        self.translations = loadTranslations()
        self.current_language = 'en_US'

        try:
            with open('language/settings.json', 'r') as settings_file:
                settings = json.load(settings_file)
                self.current_language = settings.get('language', 'en_US')
        except FileNotFoundError:
            print("FAIL")
            self.current_language = 'en_US'

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    
    def setLanguage(self, lang: str):
        """ Устанавливает язык приложения """
        with open('language/settings.json', 'w') as settings_file:
            json.dump({'language': lang}, settings_file)
    
        self.current_language = lang
        translations = self.translations[self.current_language]

        if isinstance(self, LoginApp):
            #Перевод для LoginApp
            self.ClinicBook.setText(translations["System"]["programlogo"])
            self.SIGNUP.setText(translations["SignUp"]["title"])
            self.UserName.setText(translations["SignUp"]["labellogin"])
            self.GetUserName.setPlaceholderText(translations["System"]["placeholderlogin"])
            self.Password.setText(translations["SignUp"]["labelpassword"])
            self.GetPassword.setPlaceholderText(translations["System"]["placeholderlogin"])
            self.SignUpButton.setText(translations["SignUp"]["signupbutton"])
            self.RegisterButton.setText(translations["SignUp"]["registerbutton"])

        elif isinstance(self, RegisterApp):
            #Перевод для RegisterApp
            self.ClinicBook.setText(translations["System"]["programlogo"])
            self.SIGNUP.setText(translations["Register"]["title"])
            self.UserName.setText(translations["Register"]["labellogin"])
            self.GetUserName.setPlaceholderText(translations["System"]["placeholderlogin"])
            self.Password.setText(translations["Register"]["labelpassword"])
            self.GetPassword.setPlaceholderText(translations["System"]["placeholderpassword"])
            self.Password_2.setText(translations["Register"]["labelconfirmpassword"])
            self.GetPassword_2.setPlaceholderText(translations["System"]["placeholderpassword"])
        
            link_text = translations["Register"]["offer"]
            text = " ".join(link_text.split(' ')[:3])
            link_message = " ".join(link_text.split(' ')[3:])
            self.label.setText(f'{text} <a href="{agent_url}">{link_message}</a>')
            
            self.RegisterButton.setText(translations["SignUp"]["registerbutton"])
            self.SignUpButton.setText(translations["SignUp"]["signupbutton"])
        elif isinstance(self, MainLayoutApp):
            #Перевод для MainLayoutApp
            self.HomeButton.setText(translations["System"]["Panel1"])
            self.SettingButton.setText(translations["System"]["Panel2"])
            self.MySend.setText(translations["System"]["Panel3"])
            self.TextLogoType.setText(translations["System"]["programlogo"])
            self.SIGNUP.setText(translations["Main"]["title"])
            self.UserFullName.setText(translations["Main"]["labelfullname"])
            self.GetUserFullName.setPlaceholderText(translations["Main"]["placeholfullname"])
            self.DateUser.setText(translations["Main"]["labeldateuser"])
            self.SignUpClinicButton.setText(translations["Main"]["sendbutton"])
        elif isinstance(self, SettingLayoutApp):
            #Перевод для SettingLayoutApp
            self.HomeButton.setText(translations["System"]["Panel1"])
            self.SettingButton.setText(translations["System"]["Panel2"])
            self.MySend.setText(translations["System"]["Panel3"])
            self.TextLogoType.setText(translations["System"]["programlogo"])
            self.Setting.setText(translations["Setting"]["title"])

            self.GetNunbmer.setText(translations["Setting"]["labelfnumber"])
            self.DateUser.setText(translations["Setting"]["labelexit"])
            self.ThemeChange.setText(translations["Setting"]["exit"])
        elif isinstance(self, MySendLayoutApp):
            #Перевод для SettingLayoutApp
            self.HomeButton.setText(translations["System"]["Panel1"])
            self.SettingButton.setText(translations["System"]["Panel2"])
            self.MySend.setText(translations["System"]["Panel3"])
            self.TextLogoType.setText(translations["System"]["programlogo"])
            self.title.setText(translations["MySend"]["title"])

    def en_US(self) -> None:
        self.change_language.emit('en_US')

    def ru_RU(self) -> None:
        self.change_language.emit('ru_RU')

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
    switch_window = pyqtSignal()
    switch_window_main = pyqtSignal()

    """Главное меню login_layout"""
    def __init__(self, parent=None) -> None:
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)
        self.setLanguage(self.current_language)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.rubutton.clicked.connect(self.ru_RU)
        self.rubutton_2.clicked.connect(self.en_US)

        self.connected()
    
    def connected(self) -> None:
        """Подключение кнопок"""
        self.RegisterButton.clicked.connect(self.switchToRegister)
        
        self.GetUserName.textChanged.connect(self.getTextUser)
        self.GetPassword.textChanged.connect(self.getTextPassword)

        self.user_text: bool = False
        self.password_text: bool = False

        self.user_name: str = None
        self.password_1: str = None

        self.button_enable() # Проверка состояния полей и флажка при запуске приложения
        self.SignUpButton.setEnabled(False)

        self.SignUpButton.clicked.connect(self.signup)
    
    def signup(self) -> None:
        status = db().selectLoginPassword(login=self.user_name, password=self.password_1)
        if status:
            ldb().joins(login=self.user_name, password=self.password_1)
            self.switch_window_main.emit()
        else:
            msg_box = QMessageBox()
            msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: #fff;
                    color: black;
                }
                QMessageBox QLabel {
                    color: black;
                }
                QMessageBox QPushButton {
                    background-color: red;
                    color: white;
                    padding: 6px;
                    border-radius: 4px;
                }
            """)
            msg_box.setWindowTitle(self.translations[self.current_language]['System']['titleerror'])
            msg_box.setText(self.translations[self.current_language]['System']['texterror1'])
            msg_box.exec_()
    
    def switchToRegister(self) -> None:
        """Переключение между окнами"""
        self.switch_window.emit()
    
    def button_enable(self) -> None:
        """Проверка на поля(выключение кнопки)"""
        if len(self.GetUserName.text()) >= 2 and len(self.GetPassword.text()) >= 7:
            self.SignUpButton.setEnabled(True)
        else:
            self.SignUpButton.setEnabled(False)

    def getTextUser(self, text) -> None:
        """Что ввёл пользователь в поле User Name?"""
        self.user_text = bool(text)
        self.user_name = text
        self.button_enable()

    def getTextPassword(self, text) -> None:
        """Что ввёл пользователь в поле Password?"""
        self.password_text = bool(text)
        self.password_1 = text
        self.button_enable()


class RegisterApp(CommonApp, register_layout.Ui_MainWindow):
    switch_window = pyqtSignal() # Сигнал

    """Окно register_layout"""
    def __init__(self, parent=None) -> None:
        super(RegisterApp, self).__init__(parent)
        self.setupUi(self)

        style_str = '''
        QLabel
        {
            background-color: transparent;
            color: #ca3767;
            font: 400 7pt "Montserrat Medium";
        }
        '''
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet(style_str)
        self.label.setGeometry(QtCore.QRect(309, 321, 400, 17))  # Согласуйте с макетом
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setText('')
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setOpenExternalLinks(True)

        self.setLanguage(self.current_language)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.rubutton.clicked.connect(self.ru_RU)
        self.rubutton_2.clicked.connect(self.en_US)

        self.connected()

    def connected(self) -> None:
        """Подключение кнопок"""
        self.SignUpButton.clicked.connect(self.switchToLogin)

        self.GetUserName.textChanged.connect(self.getTextUser)
        self.GetPassword.textChanged.connect(self.getTextPassword)
        self.GetPassword_2.textChanged.connect(self.getTextPassword_2)
        self.AgreeCond.toggled.connect(self.checkBoxChecked)

        self.user_text: bool = False
        self.password_text: bool = False
        self.password_text_2: bool = False
        self.check_box_status: bool = False

        self.user_name: str = None
        self.password_1: str = None
        self.password_2: str = None

        self.button_enable() # Проверка состояния полей и флажка при запуске приложения
        self.RegisterButton.setEnabled(False)

        self.RegisterButton.clicked.connect(self.register)

    def register(self) -> None:
        status_list = db().selectAllLogin(nick=self.user_name)
        if not status_list:
            db().writeNewLogin(nick=self.user_name, password=self.password_1)
            self.switch_window.emit()
        else:
            msg_box = QMessageBox()
            msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: #fff;
                    color: black;
                }
                QMessageBox QLabel {
                    color: black;
                }
                QMessageBox QPushButton {
                    background-color: red;
                    color: white;
                    padding: 6px;
                    border-radius: 4px;
                }
            """)
            msg_box.setWindowTitle(self.translations[self.current_language]['System']['titleerror'])
            msg_box.setText(self.translations[self.current_language]['System']['texterror2'])
            msg_box.exec_()

    
    def switchToLogin(self) -> None:
        """Переключение между окнами"""
        self.switch_window.emit()

    def button_enable(self) -> None:
        """Проверка на поля(выключение кнопки)"""
        if len(self.GetUserName.text()) >= 2 and len(self.GetPassword.text()) >= 7 \
                        and self.AgreeCond.isChecked() and self.password_1 == self.password_2:
            self.RegisterButton.setEnabled(True)
        else:
            self.RegisterButton.setEnabled(False)

    def getTextUser(self, text) -> None:
        """Что ввёл пользователь в поле User Name?"""
        self.user_text = bool(text)
        self.user_name = text
        self.button_enable()

    def getTextPassword(self, text) -> None:
        """Что ввёл пользователь в поле Password?"""
        self.password_text = bool(text)
        self.password_1 = text
        self.button_enable()
    
    def getTextPassword_2(self, text) -> None:
        """Что ввёл пользователь в поле Password?"""
        self.password_text_2 = bool(text)
        self.password_2 = text
        self.button_enable()
    
    def checkBoxChecked(self, state):
        """Что ввёл пользователь в поле CheckBox?"""
        if state:
            self.check_box_status = True
        else:
            self.check_box_status = False
        self.button_enable()

from datetime import datetime, timedelta
import requests as req

class MainLayoutApp(CommonApp, main_layout.Ui_MainWindow):
    switch_window = pyqtSignal()
    switch_window_to_mysend_1 = pyqtSignal()
    request_added = pyqtSignal()

    """Окно register_layout"""
    def __init__(self, parent=None) -> None:
        super(MainLayoutApp, self).__init__(parent)
        self.setupUi(self)
        self.setLanguage(self.current_language)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.rubutton.clicked.connect(self.ru_RU)
        self.rubutton_2.clicked.connect(self.en_US)

        self.connected()

    def connected(self) -> None:
        """Подключение кнопок"""
        self.SettingButton.clicked.connect(self.switch_on_setting)
        self.MySend.clicked.connect(self.switchToMysend)

        self.GetUserFullName.textChanged.connect(self.validateUserFullName)
        self.DateEditUser.dateChanged.connect(self.validateUserDate)
        self.SignUpClinicButton.setEnabled(False)
        self.SignUpClinicButton.clicked.connect(self.send)
        self.DateEditUser.setMinimumDate(QtCore.QDate(1950, 9, 14))
        self.DateEditUser.setDate(QtCore.QDate(1950, 9, 14))

        self.DateEditUser_2.setDate(QtCore.QDate.currentDate())
        self.DateEditUser_2.setMinimumDate(QtCore.QDate.currentDate())     
        current_time = QtCore.QTime.currentTime()
        if current_time.hour() >= 21:
            next_day = QtCore.QDate.currentDate().addDays(1)
            self.DateEditUser_2.setDate(next_day) 
            self.DateEditUser_2.setMinimumDate(next_day)
        self.timeEdit.setMinimumTime(QtCore.QTime(8, 0))
        self.timeEdit.setMaximumTime(QtCore.QTime(21, 0))

        self.DateEditUser_2.dateChanged.connect(self.validateUserDateSend)

        self.fullName: list = None
        self.Date_of_birth: str = None
        self.Date_of_recording: str = None

        self.SignUpClinicButton.setEnabled(False)
        self.get_current_date_time()


    def get_current_date_time(self):
        response = req.get('http://worldtimeapi.org/api/timezone/europe/moscow')
        data = response.json()
        current_datetime = datetime.strptime(data['datetime'], "%Y-%m-%dT%H:%M:%S.%f%z")
        year = current_datetime.year
        month = current_datetime.month
        day = current_datetime.day
        hour = current_datetime.hour
        minute = current_datetime.minute
        second = current_datetime.second
        microsecond = current_datetime.microsecond
        return [year, month, day, hour, minute, second, microsecond]

    def validateUserDateSend(self, value: QtCore.QDate) -> None:
        """Проверяет дату на возможность активации кнопки"""
        curret_datetime = self.get_current_date_time()
        if value.year() >= int(curret_datetime[0]) and value.month() >= int(curret_datetime[1]) and \
              value.day() >= int(curret_datetime[2]) and value.year() <= int(curret_datetime[0])+1:
            self.SignUpClinicButton.setEnabled(True)
        else:
            self.SignUpClinicButton.setEnabled(False)

    def switch_on_setting(self) -> None:
        """Вход в настройки"""
        self.switch_window.emit()
    
    def switchToMysend(self) -> None:
        """Переключение между окнами"""
        self.switch_window_to_mysend_1.emit()
    
    def send(self) -> None:
        value_birth: QtCore.QDate = self.DateEditUser.date()
        value_recording: QtCore.QDate = self.DateEditUser_2.date()
        time_recording: QtCore.QTime = self.timeEdit.time()

        self.Date_of_birth = f"{value_birth.day()}-{value_birth.month()}-{value_birth.year()}"
        self.Date_of_recording = f"{value_recording.day()}-{value_recording.month()}-{value_recording.year()}"
        self.Time_of_recording = f"{time_recording.hour()}-{time_recording.minute()}-{time_recording.second()}"



        print(self.fullName)
        print(self.Date_of_birth)
        print(self.Date_of_recording)
        print(self.Time_of_recording)

        login = ldb().select_my_login()[0]
        db().regSend(
            login=login,
            surname=self.fullName[0],
            middlename=self.fullName[1],
            fullname=self.fullName[2],
            time_recording=self.Time_of_recording,
            date_recording=self.Date_of_recording,
            date_birth=self.Date_of_birth
        )
        msg_box = QMessageBox()
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #fff;
                color: black;
            }
            QMessageBox QLabel {
                color: black;
            }
            QMessageBox QPushButton {
                background-color: green;
                color: white;
                padding: 6px;
                border-radius: 4px;
            }
        """)
        msg_box.setWindowTitle(self.translations[self.current_language]['System']['titilesuccessfully'])
        msg_box.setText(self.translations[self.current_language]['System']['textsuccessfully'])
        msg_box.exec_()
        self.request_added.emit()


    def validateUserFullName(self, value: str) -> None:
        """Проверяет поле на возможность активации кнопки"""
        split_value = value.split()
        if len(split_value) < 3:
            self.SignUpClinicButton.setEnabled(False)
        else:
            self.SignUpClinicButton.setEnabled(True)
            self.fullName = split_value

    def validateUserDate(self, value: QtCore.QDate) -> None:
        """Проверяет дату на возможность активации кнопки"""
        curret_datetime = self.get_current_date_time()
        if value.year() <= int(curret_datetime[0])-6:
            self.SignUpClinicButton.setEnabled(True)
        else:
            self.SignUpClinicButton.setEnabled(False)


class SettingLayoutApp(CommonApp, setting_layout.Ui_MainWindow):
    switch_window = pyqtSignal()
    switch_window_exit = pyqtSignal()
    switch_window_to_mysend_1 = pyqtSignal()

    """Окно register_layout"""
    def __init__(self, parent=None) -> None:
        super(SettingLayoutApp, self).__init__(parent)
        self.setupUi(self)
        self.setLanguage(self.current_language)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.rubutton.clicked.connect(self.ru_RU)
        self.rubutton_2.clicked.connect(self.en_US)

        self.connected()

    def connected(self) -> None:
        """Подключение кнопок"""
        self.HomeButton.clicked.connect(self.switch_on_setting)
        self.MySend.clicked.connect(self.switch_on_MySend)
        self.ThemeChange.clicked.connect(self.exit_system)

    def switch_on_setting(self) -> None:
        """Вход в настройки"""
        self.switch_window.emit()
    
    def switch_on_MySend(self) -> None:
        """Вход в настройки"""
        self.switch_window_to_mysend_1.emit()

    def exit_system(self) -> None:
        """Вход в настройки"""
        if ldb().exits() == False:
            exit()
        else:
            self.switch_window_exit.emit()


class MySendLayoutApp(CommonApp, mysend_layout.Ui_MainWindow):
    switch_window_to_mysend_3 = pyqtSignal()
    switch_window_to_mysend_2 = pyqtSignal()

    """Окно mysend_layout"""
    def __init__(self, parent=None) -> None:
        super(MySendLayoutApp, self).__init__(parent)
        self.setupUi(self)
        self.setLanguage(self.current_language)

        self.setFixedSize(self.size())
        self.m_drag = False
        self.m_DragPosition = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.HideProgram.clicked.connect(self.hideWindow)
        self.CloseProgram.clicked.connect(self.closeWindow)

        self.rubutton.clicked.connect(self.ru_RU)
        self.rubutton_2.clicked.connect(self.en_US)

        self.connected()
        self.addItemsToWidget()

    def connected(self) -> None:
        """Подключение кнопок"""
        self.HomeButton.clicked.connect(self.switch_on_main)
        self.SettingButton.clicked.connect(self.switch_on_setting)

    def switch_on_main(self) -> None:
        """Вход в настройки"""
        self.switch_window_to_mysend_3.emit()
    
    def switch_on_setting(self) -> None:
        """Вход в настройки"""
        self.switch_window_to_mysend_2.emit()
    
    def addItemsToWidget(self):
        self.widgets = dict()
        for widget in self.widgets.values():
           widget.clear()

        while self.tabWidget.count() > 0:
            self.tabWidget.removeTab(0)

        requests = db().select_send(login=ldb().select_my_login())
        requests = sorted(requests, key=lambda x: (x[0], x[1], x[2]))
        
        labelStyle = """
        * {
            border: 0;
            background-color: 0;
            width: 0;
            height: 0;
            color: #ca3767;
            font: 200 9pt 'Montserrat Medium';
        }
        """

        for request in requests:
            fullname = f"{request[0]} {request[1]} {request[2]}"

            # Проверяем, есть ли уже вкладка для данного пользователя
            if fullname not in self.widgets:
                # Если нет, то создайте новую вкладку и виджет
                widget_with_scroll = QListWidget()
                widget_with_scroll.setStyleSheet(labelStyle)
                self.tabWidget.addTab(widget_with_scroll, fullname)

                # Добавить виджет в словарь
                self.widgets[fullname] = widget_with_scroll

            # Теперь добавляем данные на вкладку
            time_label = QListWidgetItem("Время записи: " + request[3])
            time_label.setTextAlignment(Qt.AlignHCenter)
            widget_with_scroll.addItem(time_label)

            date_label = QListWidgetItem("Дата записи: " + request[4])
            date_label.setTextAlignment(Qt.AlignHCenter)
            widget_with_scroll.addItem(date_label)
            
            birth_year_label = QListWidgetItem("Год рождения: " + request[5])
            birth_year_label.setTextAlignment(Qt.AlignHCenter)
            widget_with_scroll.addItem(birth_year_label)

            birth_year_label = QListWidgetItem("                   ")
            birth_year_label.setTextAlignment(Qt.AlignHCenter)
            widget_with_scroll.addItem(birth_year_label)


class MainApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.login = LoginApp()
        self.register = RegisterApp()
        self.main = MainLayoutApp()
        self.setting = SettingLayoutApp()
        self.mysend = MySendLayoutApp()

        self.main.request_added.connect(self.mysend.addItemsToWidget)

        self.login.switch_window.connect(self.show_register)
        self.register.switch_window.connect(self.show_login)
        self.login.switch_window_main.connect(self.show_main)
        self.main.switch_window.connect(self.show_setting)
        self.setting.switch_window.connect(self.show_main_2)
        self.setting.switch_window_exit.connect(self.show_login_2)
        self.main.switch_window_to_mysend_1.connect(self.show_mysend_1)
        self.setting.switch_window_to_mysend_1.connect(self.show_mysend_2)
        self.mysend.switch_window_to_mysend_3.connect(self.show_main_3)
        self.mysend.switch_window_to_mysend_2.connect(self.show_setting_2)

        self.login.change_language.connect(self.updateLanguage)
        self.register.change_language.connect(self.updateLanguage)
        self.main.change_language.connect(self.updateLanguage)
        self.setting.change_language.connect(self.updateLanguage)

        self.mysend.change_language.connect(self.updateLanguage)

        if ldb().select_join():
            self.main.show()
        else:
            self.login.show()
        
    """---------------"""
    
    def updateLanguage(self, lang: str) -> None:
        self.login.setLanguage(lang)
        self.register.setLanguage(lang)
        self.main.setLanguage(lang)
        self.setting.setLanguage(lang)
        self.mysend.setLanguage(lang)

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
    
    def show_mysend_1(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.mysend.move(window_pos)
        self.mysend.show()
        self.main.close()
    
    def show_mysend_2(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.mysend.move(window_pos)
        self.mysend.show()
        self.setting.close()
        
    def show_login(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.login.move(window_pos)
        self.login.show()
        self.register.close()
    
    def show_main(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.main.move(window_pos)
        self.main.show()
        self.login.close()
    
    def show_setting(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.setting.move(window_pos)
        self.setting.show()
        self.main.close()
    
    def show_main_2(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.main.move(window_pos)
        self.main.show()
        self.setting.close()
    
    def show_login_2(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.login.move(window_pos)
        self.login.show()
        self.setting.close()
    
    def show_main_3(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.main.move(window_pos)
        self.main.show()
        self.mysend.close()
    
    def show_setting_2(self):
        """Switch between windows"""
        window_pos = self.get_position()
        self.setting.move(window_pos)
        self.setting.show()
        self.mysend.close()


if __name__ == "__main__":
    import sys
    ldb().create_table()
    db().createTable()
    app = MainApp(sys.argv)
    sys.exit(app.exec())

