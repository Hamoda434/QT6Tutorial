import sys

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow

class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        #Connect the button.
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        #self.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.todoEdit.text()
        text = text.strip()
        if text: #Don't add empty strings.
            #Access the list via the model.
            self.model.todos.append((False, text))
            #Trigger refresh.
            self.model.layoutChanged.emit()
            #Empty the input
            self.todoEdit.setText("")

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            #Clear the selection (as it is no longer valid)
            self.todoView.clearSelection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()