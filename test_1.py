import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def show_notification():
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
    msg_box.setWindowTitle("Ошибка!")
    msg_box.setText("Такой никнейм уже существует.")
    msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Пример с кнопкой и уведомлением")
    button = QPushButton("Нажми меня", window)
    button.clicked.connect(show_notification)
    
    window.resize(250, 150)
    window.show()

    sys.exit(app.exec_())
