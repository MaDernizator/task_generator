from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.StartWindowGUI import StartWindowGUI
from create_window_code import CreateWindow
from view_code import ViewWindow
import create_window_code

import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class StartWindow(QMainWindow, StartWindowGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_button.clicked.connect(self.create_)
        self.open_button.clicked.connect(self.open)
        self.edit_button.clicked.connect(self.edit)
        self.create_window = CreateWindow()
        self.view_window = ViewWindow()

    def create_(self):  # метод create уже существует
        self.create_window.show()

    def open(self):
        pass


    def edit(self):
        self.view_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
