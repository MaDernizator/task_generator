from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.StartWindowGUI import StartWindowGUI
from create import CreateWindow
from view import ViewWindow

import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class StartWindow(QMainWindow, StartWindowGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_button.clicked.connect(self.create_)
        self.open_button.clicked.connect(self.open)
        self.edit_button.clicked.connect(self.edit)

        self.view_window = ViewWindow()

    def create_(self):
        self.create_window = CreateWindow()
        self.create_window.show()

    def open(self):
        self.create_window = CreateWindow()
        self.create_window.open_file()
        self.create_window.show()

    def edit(self):
        self.view_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
