import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

FILE_FILTERS = [
    "Portable Network Graphics files (*png)",
    "Text files (*txt)",
    "Commma Seperated Values (*.csv)",
    "All Files (*)",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            "Select a file",  # caption
            "",  # starting directory
            filters,  # name filters
            initial_filter  # initial filter (positional)
        )

        print("Result:", filename, selected_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
