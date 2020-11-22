# # from docx import Document
# # from docx.shared import Inches
# #
# # document = Document()
# #
# # document.add_heading('Заголовок документа', 0)
# #
# # p = document.add_paragraph('Абзац без форматированияАбзац без форматированияАбзац без форматированияАбзац без форматированияАбзац без форматированияАбзац без форматированияАбзац без форматирования')
# # p.alignment = 3
# #
# #
# # document.save('test.docx')
# import sys, time
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtSql import *
# from PyQt5.QtCore import *
# import sqlite3
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # db = QSqlDatabase.addDatabase('QPSQL')
#         # db.setDatabaseName('postgres')
#         # db.setHostName('localhost')
#         # db.setUserName('postgres')
#         # db.setPassword('masterkey')
#         # db.open()
#
#         view = QTableView(self)
#         model = QSqlQueryModel(self)
#         con = sqlite3.connect('pattern_db.db')
#         cur = con.cursor()
#         model.setQuery("""SELECT type AS "тип", name AS "имя", pattern AS "текст" FROM patterns""")
#         view.setModel(model)
#         con.close()
#         view.move(10, 10)
#         view.resize(617, 315)
#
#         # Buttons:
#         button1 = QPushButton('Exit', self)
#         button1.resize(button1.sizeHint())
#         button1.move(50, 400)
#
#         # def But1Click():
#         #     if db.close():
#         #         print('close')
#         #     else:
#         #         print('db dont close')
#         #         sys.exit()
#
#         # button1.clicked.connect(But1Click)
#
#         # Window:
#         self.setGeometry(300, 100, 650, 450)
#         self.setWindowTitle('Icon')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('pattern_db.sqlite')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('films')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Пример работы с QtSql')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())