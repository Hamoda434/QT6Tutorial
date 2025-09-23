import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))
        db.open()

        self.table = QTableView()

        self.model = QSqlTableModel(db=db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Album (ID)")
        self.model.setHeaderData(3, Qt.Horizontal, "Media Type (ID)")
        self.model.setHeaderData(4, Qt.Horizontal, "Genre (ID)")
        self.model.setHeaderData(5, Qt.Horizontal, "Composer")
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()