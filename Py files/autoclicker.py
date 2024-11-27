import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QStyleFactory, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
import pyautogui
import keyboard

class AutoClicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Автокликер")
        self.setWindowIcon(QIcon('C:\photodlaicon\mouse.ico'))
        self.clicks_count = 0
        self.running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.click)
        self.initUI()

    def initUI(self):
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setPalette(palette)
        QApplication.setPalette(palette)

        grid = QGridLayout()

        # Метки с белым текстом
        label_clicks = QLabel("Количество кликов:")
        label_clicks.setStyleSheet("color: white;")
        grid.addWidget(label_clicks, 0, 0)

        label_interval = QLabel("Интервал (сек):")
        label_interval.setStyleSheet("color: white;")
        grid.addWidget(label_interval, 1, 0)

        self.clicks_edit = QLineEdit("10")
        self.clicks_edit.setFixedWidth(100)
        grid.addWidget(self.clicks_edit, 0, 1)

        self.interval_edit = QLineEdit("0.5")
        self.interval_edit.setFixedWidth(100)
        grid.addWidget(self.interval_edit, 1, 1)

        self.start_button = QPushButton("Старт")
        self.start_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.start_button.clicked.connect(self.start_stop)
        self.start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.stop_button = QPushButton("Стоп")
        self.stop_button.setStyleSheet("background-color: #f44336; color: white;")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.start_stop)
        self.stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def start_stop(self):
        sender = self.sender()
        if sender.text() == "Старт":
            try:
                self.clicks_count = int(self.clicks_edit.text())
                self.interval = float(self.interval_edit.text())
                if self.interval <= 0:
                    QMessageBox.warning(self, "Ошибка", "Интервал должен быть больше 0.")
                    return
                self.running = True
                self.start_button.setEnabled(False)
                self.stop_button.setEnabled(True)
                self.timer.start(int(self.interval * 1000))
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Неверный формат ввода.")
        else:
            self.running = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.timer.stop()

    def click(self):
        if self.running and self.clicks_count > 0 and not keyboard.is_pressed("esc"):
            pyautogui.click()
            self.clicks_count -= 1
        else:
            self.running = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoClicker()
    window.show()
    sys.exit(app.exec_())
