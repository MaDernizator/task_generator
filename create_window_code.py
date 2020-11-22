from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.CreateWindowGUI import CreateWindowGUI
from task_widget_code import TaskWidget
from docx import Document
from PyQt5.QtWidgets import QHBoxLayout, QWidget
from task_cod import TaskGenerator
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDial
import os
import sys


sys.excepthook = lambda *a: sys.__excepthook__(*a)


class CreateWindow(QWidget, CreateWindowGUI):
    def __init__(self):
        self.task_widgets = []
        super().__init__()
        self.setupUi(self)
        # self.tasks_layout = QHBoxLayout()
        self.add_button.clicked.connect(self.add)
        self.generate_button.clicked.connect(self.generate)
        self.generate_button.setEnabled(False)
        # self.add()

    def initUI(self):
        pass
        # self.wid1 = TaskWidget(self)
        #
        # hbox = QHBoxLayout()
        # hbox.addWidget(self.wid1)
        # self.setLayout(hbox)
        #
        # self.setGeometry(300, 300, 1000, 1000)




    def add(self):
        self.wid1 = TaskWidget(self)

        # hbox = QHBoxLayout()
        # hbox.addWidget(self.wid1)
        # self.setLayout(hbox)
        #
        # self.setGeometry(300, 300, 1000, 1000)
        # self.task = TaskWidget(self)
        # self.task_widgets.append(self.task)
        # self.tasks_layout.addWidget(self.task)
        # self.setLayout(self.tasks_layout)
        # self.generate_button.setEnabled(True)
        # self.wid1 = TaskWidget(self)
        # wid1 = TaskWidget(self)
        # hbox = QHBoxLayout()
        # hbox.addWidget(wid1)
        # self.setLayout(hbox)
        #
        # self.setGeometry(300, 300, 1000, 1000)
        # self.show()


    def generate(self):
        def generate_document():

            tasks = Document()
            tasks.add_heading(self.name_edit.text() + f' Вариант-{variant}', 0)
            number = 1
            for task_widget in self.task_widgets:
                for _ in range(task_widget.get_count()):
                    task_gen = TaskGenerator(task_widget.get_pattern())
                    p = tasks.add_paragraph(f'№{number} ' + task_gen.get_text()[0])
                    p.alignment = 3
                    par.add_run(f'\n№{number} - ' + str(task_gen.get_text()[1]))
                    number += 1
            tasks.save(directory + '/' + self.name_edit.text() + f'_вариант-{variant}.docx')

        file_dialog = QFileDialog()

        directory = \
            file_dialog.getSaveFileName(self, self.name_edit.text(), 'имя работы',
                                        'Все файлы (*)')[0]
        print(directory)
        os.mkdir(directory)

        answers = Document()
        for variant in range(1, int(self.variants_count_edit.text()) + 1):
            answers.add_heading(f'Вариант-{variant}', 0)
            par = answers.add_paragraph()
            generate_document()
        answers.save(directory + '/' + self.name_edit.text() + '_ответы.docx')

# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.wid1 = TaskWidget(self)
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.wid1)
#         self.setLayout(hbox)
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
