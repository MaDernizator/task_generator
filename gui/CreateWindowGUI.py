# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CreateWindowGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 643)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        self.name_edit = QtWidgets.QLineEdit(self)
        self.name_edit.setGeometry(QtCore.QRect(10, 10, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_edit.setFont(font)
        self.name_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_edit.setObjectName("name_edit")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 771, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.variants_count_edit = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.variants_count_edit.setFont(font)
        self.variants_count_edit.setMinimum(1)
        self.variants_count_edit.setObjectName("variants_count_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.variants_count_edit)
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setGeometry(QtCore.QRect(10, 100, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_butoon")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 771, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.tasks_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.tasks_layout.setContentsMargins(0, 0, 0, 0)
        self.tasks_layout.setObjectName("tasks_layout")
        self.generate_button = QtWidgets.QPushButton(self)
        self.generate_button.setGeometry(QtCore.QRect(14, 582, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generate_button.setFont(font)
        self.generate_button.setObjectName("generate_button")
        # MainWindow.setCentralWidget(self)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_edit.setText(_translate("MainWindow", "Имя работы"))
        self.label.setText(_translate("MainWindow", "Количество вариантов:"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.generate_button.setText(_translate("MainWindow", "Сгенерировать"))
