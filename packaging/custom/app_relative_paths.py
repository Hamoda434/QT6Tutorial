import os
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QIcon

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.setIcon(QIcon(os.path.join(basedir, "stick.png")))
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "stick.png")))
w = MainWindow()
app.exec()