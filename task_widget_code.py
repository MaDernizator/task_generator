from PyQt5.QtWidgets import QWidget
from gui.NewTaskWidgetGUI import TaskWidgetGUI
import sqlite3

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from edit_db_code import EditWindow
import sys
sys.excepthook = lambda *a: sys.__excepthook__(*a)


class TaskWidget(QWidget, TaskWidgetGUI):

    def __init__(self, form):
        super().__init__(form)
        self.setupUi(self)
        pixmap = QPixmap('view.png')
        icon = QIcon(pixmap)
        self.view_button.setIcon(icon)
        self.view_button.clicked.connect(self.view)
        self.subject_edit.currentTextChanged.connect(self.subject_changed)
        self.type_edit.currentTextChanged.connect(self.type_changed)
        self.set_parameters()
        self.edit_window = EditWindow(only_view=True)

    def view(self):
        self.edit_window.set_id(self.get_id())
        self.edit_window.show()


    def set_parameters(self):
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        subjects = cur.execute("""SELECT subject FROM subjects""").fetchall()
        for subject in subjects:
            self.subject_edit.addItem(subject[0])
        con.close()
        self.subject_changed()

    def subject_changed(self):
        self.type_edit.clear()
        self.name_edit.clear()
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        types = cur.execute(f"""SELECT type FROM types WHERE subject = (SELECT id FROM subjects WHERE subject = '{self.subject_edit.currentText()}')""").fetchall()
        for type in types:
            self.type_edit.addItem(type[0])
        con.close()
        self.type_changed()

    def type_changed(self):
        self.name_edit.clear()
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        names = cur.execute(
            f"""SELECT name FROM patterns WHERE type in (SELECT id FROM types WHERE type = '{self.type_edit.currentText()}')""").fetchall()
        for name in names:
            self.name_edit.addItem(name[0])
        con.close()


    def get_id(self):
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        id = cur.execute(f"""SELECT id FROM patterns WHERE name = '{self.name_edit.currentText()}' AND type = (SELECT id FROM types WHERE type = '{self.type_edit.currentText()}' AND subject = (SELECT id from subjects WHERE subject = '{self.subject_edit.currentText()}'))""").fetchall()[0][0]
        return id

    def get_count(self):
        return int(self.count_edit.text())

    def get_pattern(self):

        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        pattern = cur.execute(f"""SELECT pattern FROM patterns WHERE id = {self.get_id()}""").fetchall()[0][0]
        con.close()

        return pattern

    # def set_type(self, type_):
    #     self.count_edit.setText(type_)

#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.wid1 = TaskWidget(self)
#         self.resize(500, 500)
#
#         # hbox = QHBoxLayout()
#         # hbox.addWidget(self.wid1)
#         # self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 1000, 1000)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec_())
