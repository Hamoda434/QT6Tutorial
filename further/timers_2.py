import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QDial, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.setStyleSheet(
            # Make the check state red so easier to see.
            "QPushButton:checked {background: red; }"
        )

        self.button.toggled.connect(self.button_checked)

        self.setCentralWidget(self.button)

    def button_checked(self):
        print("Button checked")
        QTimer.singleShot(1000, self.uncheck_button)

    def uncheck_button(self):
        print("Button unchecked")
        self.button.setChecked(False)

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()
