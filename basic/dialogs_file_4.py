import sys
from mimetypes import inited

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
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

        layout = QVBoxLayout()

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ""
        initial_dir  = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption,  # caption
            initial_dir,  # starting directory
            filters,  # name filters
            initial_filter, # initial filter (positional)
        )

        print("Result:", filename, selected_filter)

    def get_filenames(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Initial filter: ", initial_filter)

        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption,  # caption
            initial_dir,  # starting directory
            filters,  # name filters
            initial_filter,  # initial filter (positional)
        )

        print("Result:", filenames, selected_filter)

    def get_save_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[2]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Initial filter: ", initial_filter)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption,  # caption
            initial_dir,  # starting directory
            filters,  # name filters
            initial_filter,  # initial filter (positional)
        )

        print("Result:", filename, selected_filter)

    def get_folder(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
