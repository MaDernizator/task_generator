from PyQt5.QtWidgets import QMainWindow
from gui.ErrorWindowGUI import ErrorWindowGUI
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class ErrorWindow(QMainWindow, ErrorWindowGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def display(self, message):
        self.error_label.setText(message)
        self.error_label.setGeometry(200 - self.error_label.sizeHint().width() / 2, 40, 300, 100)
        self.error_label.resize(self.error_label.sizeHint())
