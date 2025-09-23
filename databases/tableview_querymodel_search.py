import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QTableView,
    QVBoxLayout,
    QWidget,
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup database connection
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))
        if not db.open():
            raise Exception("Failed to open database")

        # Create widgets
        container = QWidget()
        layout_search = QHBoxLayout()

        self.track = QLineEdit()
        self.track.setPlaceholderText("Track name...")
        self.track.textChanged.connect(self.update_query)

        self.composer = QLineEdit()
        self.composer.setPlaceholderText("Composer name...")
        self.composer.textChanged.connect(self.update_query)

        self.album = QLineEdit()
        self.album.setPlaceholderText("Album title...")
        self.album.textChanged.connect(self.update_query)

        layout_search.addWidget(self.track)
        layout_search.addWidget(self.composer)
        layout_search.addWidget(self.album)

        layout_view = QVBoxLayout()
        layout_view.addLayout(layout_search)

        self.table = QTableView()
        layout_view.addWidget(self.table)

        container.setLayout(layout_view)
        self.setCentralWidget(container)

        # Setup model
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        # Load initial data
        self.update_query()

        self.setMinimumSize(QSize(1024, 600))
        self.setWindowTitle("Track Search")

    def update_query(self, s=None):
        # Get user input
        track_name = self.track.text()
        track_composer = self.composer.text()
        album_title = self.album.text()

        # Prepare and execute query
        query = QSqlQuery()
        query.prepare(
            """
            SELECT Track.Name AS "Track", 
                   Track.Composer AS "Composer", 
                   Album.Title AS "Album"
            FROM Track
            INNER JOIN Album ON Track.AlbumId = Album.AlbumId
            WHERE Track.Name LIKE '%' || :track_name || '%'
              AND Track.Composer LIKE '%' || :track_composer || '%'
              AND Album.Title LIKE '%' || :album_title || '%'
            """
        )

        query.bindValue(":track_name", track_name)
        query.bindValue(":track_composer", track_composer)
        query.bindValue(":album_title", album_title)

        query.exec()
        self.model.setQuery(query)

        if self.model.lastError().isValid():
            print("Query Error:", self.model.lastError().text())

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
