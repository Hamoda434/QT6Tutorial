import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QVBoxLayout


class Thread(QThread):
    """
    Worker thread
    """

    result = Signal(str)

    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        self.data = None
        self.is_running = True
        print("Thread start")
        counter = 0
        while self.is_running:
            time.sleep(0.1)
            #Output the number as a formatted string.
            self.result.emit(f"The number is {counter}")
            counter += 1
    def stop(self):
        self.is_running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Create thread adn start it.
        self.thread = Thread()
        self.thread.start()
        
        label = QLabel("Output will appear here")
        button = QPushButton("Shutdown thread")
        #Shut down the thread nicely.
        button.pressed.connect(self.thread.stop)

        #Connect signal, so output appears on label
        self.thread.result.connect(label.setText)
        self.thread.result.connect(self.thread_has_finished)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

    def thread_has_finished(self):
        print("Thread has finished.")
        print(
            self.thread,
            self.thread.isRunning(),
            self.thread.isFinished(),
        )

app = QApplication(sys.argv)
window = MainWindow()
app.exec()