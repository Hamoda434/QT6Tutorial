import os
import sys
from datetime import datetime

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

basedir = os.path.dirname(__file__)

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        COLORS = ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7', '#d1e5f0', '#92c5de', '#4393c3',
                  '#2166ac', '#053061']
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            return value

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QtGui.QIcon(
                    os.path.join(basedir, "calendar.png")
                )
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon(os.path.join(basedir,"tick.png"))

                return QtGui.QIcon(os.path.join(basedir,"cross.png"))
            if isinstance(value, int) or isinstance(value, float):
                value = int(value) #Convert to integer for indexing

                #Limit to range -5...+5, then convert to 0...10
                value = max(-5, value) # values < -5 become -5
                value = min(5, value) # values > +5 become +5
                value = value + 5 # -5 becomes 0, +5 becomes +10

                return QtGui.QColor(COLORS[value])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [True,9,2],
            [1,0,-1],
            [3, 5, False],
            [3,3, 2],
            [datetime(2017, 5, 4), 8, 9]
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()