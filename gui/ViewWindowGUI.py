# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ViewWindowGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 781, 761))
        self.table.setSizeIncrement(QtCore.QSize(0, 0))
        self.table.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.table.setFont(font)
        self.table.setLineWidth(0)
        self.table.setMidLineWidth(0)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table.setIconSize(QtCore.QSize(0, 0))
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.horizontalHeader().setDefaultSectionSize(100)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.add_action = QtWidgets.QAction(MainWindow)
        self.add_action.setObjectName("add_action")
        self.delete_action = QtWidgets.QAction(MainWindow)
        self.delete_action.setObjectName("delete_action")
        self.menu.addAction(self.add_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("", ""))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "предмет"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "тип"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "имя"))
        self.menu.setTitle(_translate("MainWindow", "Действия"))
        self.add_action.setText(_translate("MainWindow", "Добавить"))
        self.delete_action.setText(_translate("MainWindow", "Удалить"))
