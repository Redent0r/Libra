# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_modificar.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(227, 379)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/edit_write_pencil_pen_page-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.leditName = QtGui.QLineEdit(Dialog)
        self.leditName.setObjectName(_fromUtf8("leditName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.leditName)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.spnboxAvailable = QtGui.QSpinBox(Dialog)
        self.spnboxAvailable.setObjectName(_fromUtf8("spnboxAvailable"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spnboxAvailable)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spnboxMin = QtGui.QSpinBox(Dialog)
        self.spnboxMin.setMinimum(1)
        self.spnboxMin.setMaximum(99999)
        self.spnboxMin.setObjectName(_fromUtf8("spnboxMin"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.spnboxMin)
        self.spnboxMax = QtGui.QSpinBox(Dialog)
        self.spnboxMax.setMaximum(999999)
        self.spnboxMax.setProperty("value", 100)
        self.spnboxMax.setObjectName(_fromUtf8("spnboxMax"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.spnboxMax)
        self.cmboxCategory = QtGui.QComboBox(Dialog)
        self.cmboxCategory.setEditable(True)
        self.cmboxCategory.setObjectName(_fromUtf8("cmboxCategory"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.cmboxCategory)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.leditCode = QtGui.QLineEdit(Dialog)
        self.leditCode.setReadOnly(True)
        self.leditCode.setObjectName(_fromUtf8("leditCode"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leditCode)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spnboxCost = QtGui.QDoubleSpinBox(Dialog)
        self.spnboxCost.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spnboxCost.setMaximum(99999.0)
        self.spnboxCost.setObjectName(_fromUtf8("spnboxCost"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.spnboxCost)
        self.spnboxPrice = QtGui.QDoubleSpinBox(Dialog)
        self.spnboxPrice.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spnboxPrice.setObjectName(_fromUtf8("spnboxPrice"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.spnboxPrice)
        self.spnboxMargin = QtGui.QDoubleSpinBox(Dialog)
        self.spnboxMargin.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spnboxMargin.setObjectName(_fromUtf8("spnboxMargin"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.spnboxMargin)
        self.cmboxGroup = QtGui.QComboBox(Dialog)
        self.cmboxGroup.setEditable(False)
        self.cmboxGroup.setObjectName(_fromUtf8("cmboxGroup"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmboxGroup)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnModify = QtGui.QPushButton(Dialog)
        self.btnModify.setObjectName(_fromUtf8("btnModify"))
        self.horizontalLayout.addWidget(self.btnModify)
        self.btnUndo = QtGui.QPushButton(Dialog)
        self.btnUndo.setObjectName(_fromUtf8("btnUndo"))
        self.horizontalLayout.addWidget(self.btnUndo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Modify Item", None))
        self.label.setText(_translate("Dialog", "Code:", None))
        self.label_4.setText(_translate("Dialog", "Name:", None))
        self.label_5.setText(_translate("Dialog", "Maximum Quantity:", None))
        self.label_6.setText(_translate("Dialog", "Available Quantity:", None))
        self.label_2.setText(_translate("Dialog", "Suggested Price:", None))
        self.label_7.setText(_translate("Dialog", "Category:", None))
        self.label_8.setText(_translate("Dialog", "Margin: ", None))
        self.label_9.setText(_translate("Dialog", "Group:", None))
        self.label_10.setText(_translate("Dialog", "Cost: ", None))
        self.spnboxCost.setPrefix(_translate("Dialog", "$ ", None))
        self.spnboxPrice.setPrefix(_translate("Dialog", "$ ", None))
        self.spnboxMargin.setPrefix(_translate("Dialog", "% ", None))
        self.label_3.setText(_translate("Dialog", "Minimum Quantity:", None))
        self.btnModify.setText(_translate("Dialog", "Modifiy", None))
        self.btnUndo.setText(_translate("Dialog", "Undo", None))

import res_rc
