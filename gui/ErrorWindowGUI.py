from PyQt5 import QtCore, QtGui, QtWidgets


class ErrorWindowGUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 110)
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(150, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.error_label.setFont(font)
        self.error_label.setAutoFillBackground(False)
        self.error_label.setObjectName("error_label")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(310, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.error_label.setText(_translate("Dialog", "TextLabel"))
        self.ok_button.setText(_translate("Dialog", "Ok"))
