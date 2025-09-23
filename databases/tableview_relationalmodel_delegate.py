import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from pandas.core.interchange import column

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))
        db.open()

        self.table = QTableView()

        self.model = QSqlRelationalTableModel(db=db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.setRelation(
            2, QSqlRelation("Album", "AlbumId", "Title")
        )
        self.model.setRelation(
            3, QSqlRelation("MediaType", "MediaTypeId", "Name")
        )
        self.model.setRelation(
            4, QSqlRelation("Genre", "GenreId", "Name")
        )

        delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(delegate)

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()