import sys
import time

from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool, Signal
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Worker(QRunnable):
    """
    Worker thread

    :param args: Arguments to make available to the run  code
    :param kwargs: Keywords arguments to make available to the run
    :code
    :
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """
        Initialize the runner function with passed self.args,
        self.kwargs
        """
        print(self.args, self.kwargs)

    def oh_no(self):
        worker = Worker("some", "arguments", keywords=2)
        self.threadpool.start(worker)


class MainWindow(QMainWindow):

    custom_signal = Signal()

    def __init__(self):
        super().__init__()

        #Connect our custom signal to a handler.
        self.custom_signal.connect(self.signal_handler)
        #etc.

        self.threadpool = QThreadPool()

        print(
            "Multithreading with maximum %d threads"
            % self.threadpool.maxThreadCount()
        )

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("Danger!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        self.threadpool.start(self.do_some_work)

    @Slot()
    def do_some_work(self):
        print("Thread start")
        #Emit our custom signal.
        self.custom_signal.emit()
        for n in range(5):
            time.sleep(1)
        self.counter = self.counter - 10
        print("Thread complete")

    def signal_handler(self):
        print("Signal received!")

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

app = QApplication(sys.argv)
window = MainWindow()
app.exec()