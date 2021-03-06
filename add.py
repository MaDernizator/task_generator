from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.AddWindowGUI import AddWindowGUI
from task import TaskGenerator
import sqlite3
from error import ErrorWindow
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class AddWindow(QMainWindow, AddWindowGUI):
    def __init__(self, view):
        super().__init__()
        self.setupUi(self)
        self.view = view
        self.add_edit_subject.stateChanged.connect(self.subject_checkbox_changed)
        self.add_edit_type.stateChanged.connect(self.type_checkbox_changed)
        self.save_button.clicked.connect(self.save)
        self.clear_button.clicked.connect(self.clear)
        self.subject_edit.currentTextChanged.connect(self.change_type)
        self.change_subject()
        self.change_type()
        self.save_button.setEnabled(False)
        self.type_edit.currentTextChanged.connect(self.changed)
        self.subject_edit.currentTextChanged.connect(self.changed)
        self.name_edit.textChanged.connect(self.changed)
        self.pattern_text.textChanged.connect(self.changed)
        self.error_window = ErrorWindow()

    def error(self, message):
        self.error_window.show()
        self.error_window.display(message)

    def changed(self):
        self.save_button.setEnabled(True)

    def clear(self):
        self.add_edit_type.setChecked(True)
        self.add_edit_subject.setChecked(True)
        self.name_edit.clear()
        self.pattern_text.clear()

    def change_subject(self):
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()
        subjects = cur.execute("""SELECT subject FROM subjects""").fetchall()
        for subject in subjects:
            self.subject_edit.addItem(subject[0])
        con.close()

    def change_type(self):
        if not self.add_edit_type.isChecked():
            self.type_edit.clear()
            con = sqlite3.connect('pattern_db.db')
            cur = con.cursor()
            types = cur.execute(f"""SELECT type FROM types WHERE subject = 
        (SELECT id FROM subjects WHERE subject = '{self.subject_edit.currentText()}')""").fetchall()
            for type in types:
                self.type_edit.addItem(type[0])
            con.close()

    def subject_checkbox_changed(self):
        if self.add_edit_subject.isChecked():
            self.subject_edit.clear()
            self.subject_edit.setEditable(True)
            self.add_edit_type.setChecked(True)
            self.add_edit_type.setEnabled(False)
        else:
            self.subject_edit.clear()
            self.change_subject()
            self.subject_edit.setEditable(False)
            self.add_edit_type.setEnabled(True)

    def type_checkbox_changed(self):
        if self.add_edit_type.isChecked():
            self.type_edit.clear()
            self.type_edit.setEditable(True)
        else:
            self.type_edit.clear()
            self.change_type()
            self.type_edit.setEditable(False)

    def check_name_and_type_and_subject(self):
        if not self.subject_edit.currentText().strip():
            self.error('???????????? ??????????????')
            return False
        if not self.type_edit.currentText().strip():
            self.error('???????????? ??????')
            return False
        if not self.name_edit.text().strip():
            self.error('???????????? ????????????????')
            return False
        if not self.pattern_text.toPlainText():
            self.error('???????????? ?????????? ??????????????')
            return False
        con = sqlite3.connect('pattern_db.db')
        cur = con.cursor()

        if self.add_edit_subject.isChecked() and (self.subject_edit.currentText().strip(),) in \
                cur.execute('''SELECT subject FROM subjects''').fetchall():
            self.error('?????????? ?????????????? ?????? ????????????????????')
            return False
        if not self.add_edit_subject.isChecked() and self.add_edit_type.isChecked() and \
                (self.type_edit.currentText().strip(),) in cur.execute(f'''SELECT type FROM types 
                    WHERE subject = (SELECT id FROM subjects WHERE subject 
                    = '{self.subject_edit.currentText().strip()}')''').fetchall():
            self.error('?????????? ?????? ?????? ????????????????????')
            return False
        if not self.add_edit_type.isChecked() and not self.add_edit_subject.isChecked():
            if (self.name_edit.text(),) in cur.execute(f'''SELECT name FROM patterns WHERE type 
                    = (SELECT id FROM types WHERE type = '{self.type_edit.currentText().strip()}' 
                    AND subject = (SELECT id FROM subjects WHERE subject 
                    = '{self.subject_edit.currentText().strip()}'))'''):
                self.error('?????????? ???????????? ?????? ????????????????????')
                return False
        con.close()
        return True

    def check_pattern(self):
        for _ in range(5):
            try:
                task = TaskGenerator(self.pattern_text.toPlainText(), test_mode=True)
                if not task.get_text():
                    self.error('?????????????? ?????????? ???????????????????????????? ??????????????')
                    return False
            except Exception:
                self.error('???????????????? ????????????')
                return False
        return True

    def save(self):
        self.statusbar.clearMessage()
        if self.check_name_and_type_and_subject() and self.check_pattern():
            con = sqlite3.connect('pattern_db.db')
            cur = con.cursor()
            if self.add_edit_subject.isChecked():
                cur.execute(f"""INSERT INTO subjects(subject) 
                    VALUES('{self.subject_edit.currentText()}')""")
                con.commit()
            if self.add_edit_type.isChecked():
                cur.execute(f"""INSERT INTO types(subject, type) VALUES((SELECT id FROM subjects 
                    WHERE subject = '{self.subject_edit.currentText()}'), 
                    '{self.type_edit.currentText()}')""")
                con.commit()
            type = cur.execute(f"""SELECT id FROM types WHERE type 
                = '{self.type_edit.currentText()}'""").fetchall()[0][0]
            name = self.name_edit.text()
            pattern = self.pattern_text.toPlainText()
            cur.execute(f"""INSERT INTO patterns(type, name, pattern) 
                            VALUES({type}, '{name}', '{pattern}')""")
            con.commit()
            con.close()
            self.save_button.setEnabled(False)
            self.view.reload()
            self.subject_edit.clear()
            self.type_edit.clear()
            self.name_edit.clear()
            self.pattern_text.clear()
            self.close()
