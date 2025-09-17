import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel, QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

    def onMyOwnToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
