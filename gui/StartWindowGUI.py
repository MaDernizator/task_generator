from PyQt5 import QtCore, QtGui, QtWidgets


class StartWindowGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 124)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(10, 10, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(220, 10, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(430, 10, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_button.setFont(font)
        self.edit_button.setObjectName("edit_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_button.setText(_translate("MainWindow", "Создать"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.edit_button.setText(_translate("MainWindow", "Редактировать шаблоны"))
