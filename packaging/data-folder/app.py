from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QWidget,
)

from PySide6.QtGui import QIcon
import sys, os

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        layout = QVBoxLayout()
        label = QLabel("My simple app.")
        label.setMargin(10)
        layout.addWidget(label)

        button_close = QPushButton("Close")
        button_close.setIcon(
            QIcon(os.path.join(basedir, "icons", "bug.png"))
        )
        button_close.pressed.connect(self.close)
        layout.addWidget(button_close)

        button_maximize = QPushButton("Maximize")
        button_maximize.setIcon(
            QIcon(os.path.join(basedir, "icons", "stick.png"))
        )
        button_maximize.pressed.connect(self.showMaximized)
        layout.addWidget(button_maximize)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.show()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "land.jpg")))
w = MainWindow()
app.exec()