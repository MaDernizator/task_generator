from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from gui.ViewWindowGUI import ViewWindowGUI
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from add_code import AddWindow
from edit_db_code import EditWindow
import sqlite3
import sys
from PyQt5 import QtWidgets
sys.excepthook = lambda *a: sys.__excepthook__(*a)


class ViewWindow(QMainWindow, ViewWindowGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table.cellClicked.connect(self.clicked)
        self.add_action.triggered.connect(self.add)
        self.reload_button.clicked.connect(self.reload)
        pixmap = QPixmap('reload.png')
        icon = QIcon(pixmap)
        self.reload_button.setIcon(icon)
        self.reload()
        self.add_window = AddWindow()
        self.edit = EditWindow()

    def clicked(self, row, column):
        self.edit.set_id(self.table.item(row, 0).text())
        self.edit.show()
        self.reload()


    def reload(self):
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM patterns""").fetchall()
        self.table.setRowCount(len(data))

        for i, row in enumerate(data):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(cur.execute(f"""SELECT subject FROM 
                subjects WHERE id = (SELECT id FROM types WHERE id = {row[1]})""").fetchall()[0][0]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(cur.execute(f"""SELECT type FROM 
                                        types WHERE id = {row[1]}""").fetchall()[0][0]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(row[2]))
            # self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(row[3]))

        con.close()

    def add(self):
        self.add_window.show()
        self.reload()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewWindow()
    ex.show()
    sys.exit(app.exec_())
