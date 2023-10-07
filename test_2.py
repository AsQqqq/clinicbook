import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget


class LocalDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Локальная БД в PyQt5")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Создаем и подключаемся к базе данных SQLite
        self.connection = sqlite3.connect("local_db.sqlite")
        self.cursor = self.connection.cursor()

        # Создаем таблицу (если она не существует)
        self.create_table()

        # Создаем виджеты для ввода данных
        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()
        self.add_button = QPushButton("Добавить запись")
        self.add_button.clicked.connect(self.add_record)

        # Добавляем виджеты в макет
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.add_button)

        # Создаем главный виджет и устанавливаем макет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_table(self):
        # Создаем таблицу, если она не существует
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS records (name TEXT)''')
        self.connection.commit()

    def add_record(self):
        # Получаем имя из QLineEdit
        name = self.name_input.text()

        # Вставляем запись в таблицу
        self.cursor.execute("INSERT INTO records (name) VALUES (?)", (name,))
        self.connection.commit()

        # Очищаем поле ввода
        self.name_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LocalDatabaseApp()
    window.show()
    sys.exit(app.exec_())
