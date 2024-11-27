import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class Clicker(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.setWindowTitle("Simple Clicker")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(str(self.count), self)
        self.label.setFont(QFont('Arial', 24))
        self.label.setGeometry(100, 50, 100, 50)

        self.button = QPushButton("Click Me!", self)
        self.button.setFont(QFont('Arial', 14))
        self.button.setGeometry(80, 120, 140, 40)
        self.button.clicked.connect(self.increment_count)


    def increment_count(self):
        self.count += 1
        self.label.setText(str(self.count))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clicker = Clicker()
    clicker.show()
    sys.exit(app.exec_())
