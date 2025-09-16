import sys
import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

basedir = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())
print("Paths are relative to:", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(basedir, "land.jpg")))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
