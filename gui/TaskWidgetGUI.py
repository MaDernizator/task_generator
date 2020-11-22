from PyQt5 import QtCore, QtGui, QtWidgets


class TaskWidgetGUI(object):
    def initUI(self):
        self.setMinimumSize(400, 95)
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 381, 51))
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
        self.type_edit = QtWidgets.QComboBox(self.formLayoutWidget)
        self.type_edit.setObjectName("type_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.type_edit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.count_edit = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.count_edit.setMinimum(1)
        self.count_edit.setObjectName("count_edit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.count_edit.setFont(font)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.count_edit)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Тип"))
        self.label_2.setText(_translate("Form", "Количество"))
