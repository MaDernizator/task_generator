from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.AddWindowGUI import AddWindowGUI
from task_cod import TaskGenerator
import sqlite3
from error_code import ErrorWindow
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class EditWindow(QMainWindow, AddWindowGUI):
    def __init__(self, view, only_view=False):
        self.view = view
        super().__init__()
        self.setupUi(self)
        self.add_edit_type.hide()
        self.add_edit_subject.hide()
        if not only_view:
            self.save_button.setText('Изменить')
            self.clear_button.setText('Удалить')
            self.save_button.clicked.connect(self.save)
            self.clear_button.clicked.connect(self.delete)
            self.name_edit.textChanged.connect(self.changed)
            self.pattern_text.textChanged.connect(self.changed)
            self.save_button.setEnabled(False)
            self.error_window = ErrorWindow()
        if only_view:
            self.save_button.hide()
            self.clear_button.hide()
            self.name_edit.setEnabled(False)
            self.pattern_text.setEnabled(False)

    def error(self, message):
        self.error_window.show()
        self.error_window.display(message)

    def changed(self):
        self.save_button.setEnabled(True)

    def delete(self):
        if self.save_button.isEnabled():
            self.error('Есть несохранённые изменения')
        else:
            con = sqlite3.connect('pattern_db.db')
            cur = con.cursor()
            cur.execute(f'''DELETE FROM patterns WHERE id = {self.id}''')
            con.commit()
            con.close()
            self.close()
        self.view.reload()

    def set_id(self, id):
        self.type_edit.clear()
        self.subject_edit.clear()
        self.id = id
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        subject = cur.execute(f"""SELECT subject FROM subjects WHERE id = (SELECT subject FROM types WHERE id = (SELECT type FROM patterns WHERE id = {self.id}))""").fetchall()[0][0]
        self.subject_edit.addItem(subject)
        type = cur.execute(
            f"""SELECT type FROM types WHERE id = (SELECT type FROM patterns WHERE id = {self.id})""").fetchall()[
            0][0]
        self.type_edit.addItem(type)
        name = cur.execute(f"""SELECT name FROM patterns WHERE id = {self.id}""").fetchall()[0][0]
        self.name_edit.setText(name)
        pattern = \
            cur.execute(f"""SELECT pattern FROM patterns WHERE id = {self.id}""").fetchall()[0][0]
        self.pattern_text.setText(pattern)
        con.close()
        self.subject_edit.setEnabled(False)
        self.type_edit.setEnabled(False)
        self.save_button.setEnabled(False)

    def check_name_and_type_and_subject(self):
        if not self.name_edit.text().strip():
            self.error('Пустое название')
            return False
        if not self.pattern_text.toPlainText():
            self.error('Пустой текст шаблона')
            return False
        return True

    def check_pattern(self):
        try:
            TaskGenerator(self.pattern_text.toPlainText())
        except Exception:
            self.error('Неверный шаблон')
            return False
        return True

    def save(self):
        self.statusbar.clearMessage()
        if self.check_name_and_type_and_subject() and self.check_pattern():
            self.save_button.setEnabled(False)
            con = sqlite3.connect('pattern_db.db')
            cur = con.cursor()
            cur.execute(
                f"""UPDATE patterns SET name = '{self.name_edit.text()}', pattern  = '{self.pattern_text.toPlainText()}' WHERE id = {self.id}""")
            con.commit()
            con.close()
        self.view.reload()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditWindow()
    ex.show()
    sys.exit(app.exec_())
