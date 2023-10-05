import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTranslator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Switcher")
        self.layout = QVBoxLayout()
        
        self.label = QLabel()
        self.layout.addWidget(self.label)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(["English", "Русский"])
        self.combo_box.currentIndexChanged.connect(self.switch_language)
        self.layout.addWidget(self.combo_box)
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.translator = QTranslator(self)
        self.translator.load("translations.json")
        QApplication.instance().installTranslator(self.translator)

        self.retranslate_ui()

    def switch_language(self, index):
        if index == 0:
            self.translator.load("translations.json")
        elif index == 1:
            self.translator.load("translations.json", "ru")
        QApplication.instance().installTranslator(self.translator)
        self.retranslate_ui()
        
    def retranslate_ui(self):
        self.label.setText(self.tr("hello"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())