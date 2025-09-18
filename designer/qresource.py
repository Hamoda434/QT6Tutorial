import sys

from PySide6 import QtGui, QtWidgets

import resources

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        b = QtWidgets.QPushButton("My button")

        icon = QtGui.QIcon(":/icons/land.jpg")
        b.setIcon(icon)
        self.setCentralWidget(b)

        self.show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()

